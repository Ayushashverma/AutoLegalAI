# ⚖️ AutoLegal AI – Autonomous Legal Contract Assistant

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**AutoLegal AI** is an intelligent AI assistant for legal contracts. It allows you to:

- Upload PDF/DOCX contracts
- Automatically summarize contract text
- Detect potential risks in clauses
- Visualize risk distributions
- Send alerts via email
- Work through a **professional Streamlit dashboard**

---

## 🛠️ Tech Stack

- **Backend / AI:** Python, Transformers, PyTorch, LangChain (future enhancement)
- **Frontend:** Streamlit
- **Data Handling:** Pandas, NumPy, PyMuPDF, python-docx, pdfplumber
- **Visualization:** Matplotlib, Seaborn
- **Notifications:** SMTP email integration
- **Environment:** .env for secure credentials

---

## 🚀 Features

1. **Contract Upload & Parsing**
   - Supports PDF and DOCX formats
   - Full text extraction using `PyMuPDF` and `python-docx`

2. **AI Summarization**
   - Uses Transformers summarization pipeline
   - Generates concise summaries of contracts

3. **Risk Detection**
   - Zero-shot classification with `facebook/bart-large-mnli`
   - Labels clauses with: `high liability`, `moderate risk`, `low risk`, `missing clause`

4. **Visual Risk Analysis**
   - Generates bar charts for risk distribution per clause
   - Easy-to-read charts embedded in Streamlit dashboard

5. **Alerts & Notifications**
   - Send email alerts with summary and risk report
   - Secure credentials stored in `.env`

6. **Professional Streamlit Frontend**
   - Sidebar navigation: Upload → Summary → Risk Analysis → Send Alerts
   - Expandable sections for contract text, summary, and JSON risk reports
   - Status messages and interactive workflow

---

## 📁 Folder Structure

AutoLegalAI/
│
├── main.py # Streamlit frontend
├── data/
│ └── sample_contract.pdf # Sample contract
├── modules/
│ ├── document_loader.py # PDF/DOCX loading
│ ├── analyzer.py # Risk detection
│ ├── summarizer.py # Summarization
│ ├── notifier.py # Email alerts
│ └── visualizer.py # Charts
├── assets/
│ ├── header.gif # Optional GIF header
│ └── risk_plot.png # Risk chart
├── requirements.txt # Dependencies
└── README.md


---

## 📂 Installation

1. Clone the repo:

```bash
git clone https://github.com/Ayushashverma/AutoLegalAI.git
cd AutoLegalAI
pip install -r requirements.txt
Set up .env file with your email credentials:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

Usage

Run the Streamlit dashboard:

streamlit run main.py


Navigate through sidebar:

Upload & Analyze: Upload a contract

Summary: Generate contract summary

Risk Analysis: Detect and visualize clause risks

Send Alerts: Send email notifications

View interactive charts and reports directly in the dashboard.

🌟 Future Enhancements

Download summary and risk report as PDF

Dark/light mode toggle for dashboard

Integrate LangChain/AutoGPT for autonomous recommendations

Multi-contract dashboard for analytics over time

Slack or mobile push notifications for alerts

📫 Connect / Contact

GitHub: Ayushashverma

Portfolio: ayushashverma.github.io

Email: ayushvermaash@gmail.com
