

# 📄 DMP Semantic Alignment Tool

An **AI-powered Streamlit application** that compares **State** and **District** Disaster Management Plans (DMPs) section-by-section to ensure semantic alignment.
Using **Azure OpenAI GPT**, it provides concise feedback on missing content, improvements, and alignment status.

---

## 🚀 Features

* **PDF Text Extraction** – Reads State & District DMP PDFs using **PyMuPDF**
* **Section Segmentation** – Automatically splits content into predefined sections:

  * Evacuation Plan
  * Communication Plan
  * Resource Inventory
  * Training and Capacity Building
  * Roles and Responsibilities
  * Damage Assessment
  * Search and Rescue
  * Relief Measures
  * Early Warning System
* **AI-powered Comparison** – Uses Azure OpenAI GPT to:

  * Check semantic alignment
  * Identify missing content in the district plan
  * Suggest improvements
* **Report Export** – Download AI comparison results as **CSV**

---

## 🛠️ Installation

1. **Clone the repo**

```
git clone https://github.com/your-username/dmp-semantic-alignment.git
cd dmp-semantic-alignment
```

2. **Create and activate a virtual environment**

```
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Set Azure OpenAI credentials**
   Update the following in `app.py`:

```
azure_endpoint = "YOUR_AZURE_OPENAI_ENDPOINT"
api_key = "YOUR_AZURE_OPENAI_KEY"
deployment = "YOUR_MODEL_DEPLOYMENT"
```

---

## ▶️ Usage

Run the Streamlit app:

```
streamlit run app.py
```

Upload:

* **State DMP PDF**
* **District DMP PDF**

View:

* AI-generated section-wise feedback directly in the browser
* Download the **Alignment Report (CSV)**

---

## 📂 Output Example

**AI Feedback Example:**

```
- Both plans cover evacuation steps, but district plan lacks details on special needs groups.
- Missing integration with local NGOs in district plan.
- Suggest adding a drill frequency schedule.
```

---

## 📦 Dependencies

* `streamlit`
* `PyMuPDF`
* `pandas`
* `openai` (Azure OpenAI client)

---

## 📜 License

MIT License. You’re free to use, modify, and distribute with attribution.

---
