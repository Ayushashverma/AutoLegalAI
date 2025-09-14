import streamlit as st
from modules.document_loader import load_pdf, load_docx
from modules.summarizer import summarize_contract
from modules.analyzer import detect_risk
from modules.notifier import send_email
from modules.visualizer import plot_risk_distribution
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AutoLegal AI", page_icon="⚖️", layout="wide")
st.title("⚖️ AutoLegal – AI Legal Assistant")
st.markdown(
    "Analyze contracts, summarize, detect risks, visualize distributions, and send alerts—all in one place."
)

# ------------------ SIDEBAR ------------------
st.sidebar.header("📂 Menu")
menu_options = ["Upload & Analyze", "Summary", "Risk Analysis", "Send Alerts"]
choice = st.sidebar.radio("Navigate", menu_options)

# Optional GIF header
if os.path.exists("assets/header.gif"):
    st.image("assets/header.gif", use_column_width=True)

# ------------------ FILE UPLOAD ------------------
if choice == "Upload & Analyze":
    st.subheader("📤 Upload Contract")
    uploaded_file = st.file_uploader(
        "Upload a PDF or DOCX contract", type=["pdf", "docx"]
    )
    to_email = st.text_input("Enter your email for alerts:")

    if uploaded_file is not None:
        # Load contract
        if uploaded_file.type == "application/pdf":
            text = load_pdf(uploaded_file)
        else:
            text = load_docx(uploaded_file)

        st.success(f"✅ {uploaded_file.name} loaded successfully!")

        # ------------------ EXPANDABLE CONTRACT VIEW ------------------
        with st.expander("📄 View Contract Text"):
            st.text_area("Contract Content", text, height=300)

        # Save loaded text in session for other pages
        st.session_state['contract_text'] = text
        st.session_state['contract_name'] = uploaded_file.name
        st.session_state['email'] = to_email

# ------------------ SUMMARY ------------------
if choice == "Summary":
    if 'contract_text' in st.session_state:
        st.subheader("📝 Contract Summary")
        if st.button("Generate Summary"):
            summary = summarize_contract(st.session_state['contract_text'])
            st.session_state['summary'] = summary
            st.success("✅ Summary generated!")
        if 'summary' in st.session_state:
            with st.expander("View Summary"):
                st.write(st.session_state['summary'])
    else:
        st.warning("⚠️ Upload a contract first from 'Upload & Analyze'.")

# ------------------ RISK ANALYSIS ------------------
if choice == "Risk Analysis":
    if 'contract_text' in st.session_state:
        st.subheader("⚠️ Clause Risk Analysis")
        if st.button("Detect Risks"):
            risk_report = detect_risk(st.session_state['contract_text'])
            st.session_state['risk_report'] = risk_report
            st.success("✅ Risk analysis completed!")

            # Visualize
            plot_path = plot_risk_distribution(risk_report)
            st.image(plot_path, caption="Clause Risk Distribution", use_column_width=True)

        if 'risk_report' in st.session_state:
            with st.expander("View Risk Report JSON"):
                st.json(st.session_state['risk_report'])
    else:
        st.warning("⚠️ Upload a contract first from 'Upload & Analyze'.")

# ------------------ SEND ALERTS ------------------
if choice == "Send Alerts":
    if 'contract_text' in st.session_state and 'risk_report' in st.session_state and 'summary' in st.session_state:
        st.subheader("📧 Send Contract Alert Email")
        if st.button("Send Email"):
            msg = send_email(
                st.session_state['email'],
                f"AutoLegal AI Report: {st.session_state['contract_name']}",
                f"Contract: {st.session_state['contract_name']}\n\nSummary:\n{st.session_state['summary']}\n\nRisk Report:\n{st.session_state['risk_report']}"
            )
            st.success(f"✅ {msg}")
    else:
        st.warning("⚠️ Make sure you have uploaded a contract and generated summary & risk report.")
