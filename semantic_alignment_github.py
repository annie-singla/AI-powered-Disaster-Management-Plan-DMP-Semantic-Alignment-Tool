#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:38:28 2025

@author: carousell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:45:32 2025

@author: carousell
"""

import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
from openai import AzureOpenAI
from io import BytesIO

# Azure OpenAI setup
client = AzureOpenAI(
    api_version="",
    azure_endpoint="",
    api_key=""
)
deployment = "gpt-35-turbo"

SECTION_TITLES = [
    "Evacuation Plan",
    "Communication Plan",
    "Resource Inventory",
    "Training and Capacity Building",
    "Roles and Responsibilities",
    "Damage Assessment",
    "Search and Rescue",
    "Relief Measures",
    "Early Warning System"
]

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def split_sections(text):
    sections = {}
    for i, title in enumerate(SECTION_TITLES):
        start = text.lower().find(title.lower())
        if start == -1:
            sections[title] = ""
            continue
        end = len(text)
        for j in range(i + 1, len(SECTION_TITLES)):
            next_start = text.lower().find(SECTION_TITLES[j].lower())
            if next_start > start:
                end = next_start
                break
        sections[title] = text[start:end].strip()
    return sections

def truncate(text, max_chars=1500):
    return text[:max_chars] + "..." if len(text) > max_chars else text

def compare_sections(section, state_text, district_text):
    prompt = f"""
You are a disaster management expert.

Compare the following two sections from State and District DMPs.

Respond in 3 bullet points:
- Whether the two are semantically aligned or not
- What content is missing in the district version (if any)
- Suggestions for improvement

### Section: {section}

**State DMP (truncated):** 
{state_text}

**District DMP (truncated):** 
{district_text}
"""

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model=deployment,
        max_tokens=1000,
        temperature=0.2,
    )

    return response.choices[0].message.content


# -------------------- STREAMLIT APP --------------------

st.title("📄 DMP Semantic Alignment Tool")

state_pdf = st.file_uploader("Upload **State DMP** PDF", type="pdf", key="state")
district_pdf = st.file_uploader("Upload **District DMP** PDF", type="pdf", key="district")

if state_pdf and district_pdf:
    with st.spinner("🔍 Extracting and analyzing PDFs..."):
        state_text = extract_text_from_pdf(state_pdf)
        district_text = extract_text_from_pdf(district_pdf)

        state_sections = split_sections(state_text)
        district_sections = split_sections(district_text)

        results = []
        for section in SECTION_TITLES:
            st.subheader(f"📌 Section: {section}")

            s_text = truncate(state_sections.get(section, ""))
            d_text = truncate(district_sections.get(section, ""))

            alignment = compare_sections(section, s_text, d_text)
            results.append({"Section": section, "Alignment Report": alignment})
            st.markdown(f"**GPT Feedback:**\n\n{alignment}")

        df = pd.DataFrame(results)
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Report (CSV)", data=csv_bytes, file_name="alignment_report.csv", mime="text/csv")
