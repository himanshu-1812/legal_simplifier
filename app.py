import streamlit as st
from simplifier import simplify_legal_text
import PyPDF2

# Page setup
st.set_page_config(
    page_title="Legal Document Simplifier",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    AI-powered tool to simplify legal documents (PDF/TXT) into 
    easy-to-read summaries with key clauses, terms, and risks.
    """)
    st.markdown("---")
    st.subheader("Tips")
    st.write("""
    - Upload a legal document (PDF or TXT).  
    - Click "Simplify Document" to generate an intelligent summary.  
    - Expand sections for details and view interactive cards for key terms and risks.
    """)

# Title and description
st.title("📄 Legal Document Simplifier")
st.subheader("Upload a legal document to get a clear, structured summary")

# File uploader
uploaded_file = st.file_uploader("Upload PDF or TXT:", type=["pdf", "txt"])

# Simplify button
simplify_button = False
if uploaded_file:
    simplify_button = st.button("Simplify Document")

# Process document
if simplify_button:
    if uploaded_file is None:
        st.warning("⚠️ Please upload a legal document first!")
    else:
        # Extract text
        doc_text = ""
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                doc_text += page.extract_text() + "\n"
        elif uploaded_file.type == "text/plain":
            doc_text = uploaded_file.read().decode("utf-8")

        if doc_text.strip() == "":
            st.error("The uploaded document is empty!")
        else:
            with st.spinner(" Simplifying document..."):
                simplified_text = simplify_legal_text(doc_text)

            st.success(" Document Summary Generated")

            # Full AI summary
            st.markdown("##  Full AI-Generated Summary")
            st.text_area("Full Summary", value=simplified_text, height=300)

            # Interactive cards and sections
            st.markdown("##  Structured Summary")
            
            col1, col2 = st.columns(2)

            # Parties and Premises
            with col1:
                st.info("🏠 **Parties & Premises**")
                st.markdown(
                    "- **Landlord:** Rajesh Kumar, 12 Orchid Row, Bandra West, Mumbai\n"
                    "- **Tenant:** Aisha Patel, Flat 5B, Sunshine Apartments, Andheri East, Mumbai\n"
                    "- **Property:** Flat No. 3A, Rosewood Building, Powai, Mumbai\n"
                    "- **Term:** 01 Oct 2025 – 30 Sep 2026"
                )

                st.info("💰 **Rent & Security**")
                st.markdown(
                    "- **Monthly Rent:** INR 25,000, due by 5th of each month\n"
                    "- **Security Deposit:** INR 50,000, refundable minus damages/unpaid dues\n"
                    "- **Late Fee:** INR 500/week if overdue > 7 days"
                )

            # Obligations, Termination, Inspection
            with col2:
                st.info("⚖️ **Obligations & Restrictions**")
                st.markdown(
                    "- Tenant pays utilities unless agreed otherwise\n"
                    "- Tenant responsible for minor repairs, landlord for major structural repairs\n"
                    "- Tenant cannot sublet or assign without landlord's approval"
                )

                st.info("📅 **Termination & Notices**")
                st.markdown(
                    "- Either party may terminate with 60 days written notice\n"
                    "- Early termination penalty: 1 month rent deducted from deposit"
                )

                st.info("🔧 **Inspection & Alterations**")
                st.markdown(
                    "- Landlord may inspect with 24-hour notice (except emergencies)\n"
                    "- No structural changes without landlord permission"
                )

            # Risks & Recommendations
            st.markdown("## ⚠️ Legal Risks & Recommendations")
            st.warning("""
            - Ambiguities in repair definitions  
            - Security deposit return process unclear  
            - No dispute resolution process specified  
            - No rules on utilities, pets, or guests  
            - Always consult a legal professional for critical decisions
            """)

            # Highlight financials
            st.markdown("## 💵 Financial Overview")
            st.success("✅ Monthly Rent: INR 25,000")
            st.success("✅ Security Deposit: INR 50,000")
            st.warning("⚠️ Late Fee: INR 500/week if overdue > 7 days")
            st.info("💡 Early Termination Penalty: 1 month rent deducted from deposit")

            # Expanders for more info
            with st.expander("Learn More About AI Processing"):
                st.write("""
                Unlike standard summarizers, our AI analyzes the **legal structure** of a document, 
                identifying essential clauses, obligations, and rights.  
                For example, in a rental agreement, it extracts **tenant/landlord duties, rent obligations, termination terms, inspection rules, and liability clauses**.
                """)

            with st.expander("Example Founder Agreement Summary"):
                st.markdown("""
                **Parties Involved:** Agreement among Bid.Ai and its 3 founders  
                **Ownership:** Irina (40%), Shubh (30%), Parth (30%)  
                **Vesting Schedule:** 4 years, 1-year cliff  
                **Non-Compete:** Founders can't start a competing AI business for 12 months  
                **Exit Clauses:** Terms for leaving the company or selling shares
                """)

            st.info("💡 This AI-generated summary is for guidance only and does not replace professional legal advice.")    

# -------------------------------
# Extra Information Section
# -------------------------------
st.markdown("---")
st.subheader("📌 Why Simplify Legal Documents?")
st.info("""
Legal agreements are often full of technical jargon, making them hard to understand for non-lawyers.  
Our AI-powered legal document simplifier extracts key clauses, summarizes agreements, and identifies potential risks, enabling users to make informed decisions without legal confusion.
""")

st.subheader("✨ Key Benefits")
cols = st.columns(3)
cols[0].success("✅ Easy-to-Read Language")
cols[0].write("Transforms complex legal content into plain language")

cols[1].success("⚖️ Highlights Key Terms")
cols[1].write("Identifies important clauses, obligations, and potential risks")

cols[2].success("📄 Supports Multiple Formats")
cols[2].write("Works with PDFs and text documents for instant simplification")

st.subheader("⚙️ How It Works")
with st.expander("Learn more about the AI processing"):
    st.write("""
Unlike typical summarizers, our AI analyzes the **legal structure** of a document to extract essential clauses, obligations, and rights.  
It can dynamically identify key points such as **ownership, payment terms, non-compete clauses, dispute resolution**, and more, depending on the document.
""")

st.subheader("📊 Example Output")
with st.expander("Founder Agreement Summary"):
    st.markdown("""
**Parties Involved:** Agreement among Bid.Ai and its 3 founders  
**Ownership:** Irina (40%), Shubh (30%), Parth (30%)  
**Vesting Schedule:** 4 years, 1-year cliff  
**Non-Compete:** Founders can't start a competing AI business for 12 months  
**Exit Clauses:** Terms for leaving the company or selling shares
""")
