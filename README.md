#  Legal Document Simplifier

**AI-powered tool to turn complex legal documents into clear, readable summaries.**

---
## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  


##  Overview

Many legal documents—rental agreements, contracts, terms of service—are written in complicated, technical language. This makes them hard to understand, especially for non-lawyers.

**Legal Document Simplifier** solves that by:

- Extracting key clauses and responsibilities  
- Summarizing obligations and terms in plain English  
- Highlighting potential risks and financial commitments  

The goal is to empower people to understand what they are agreeing to—without needing legal training.

---

##  Features

-  Upload PDF or TXT files  
-  Extract text from legal documents  
-  Generate simplified summaries that focus on:  
  - Parties involved  
  - Term / Duration  
  - Rent, Fees & Financials  
  - Obligations & Responsibilities  
  - Termination clauses  
  - Risks & Recommendations  
-  User-friendly interface with structured output  
-  Built with **Streamlit** for fast and interactive UI  

---

## Getting Started

### Prerequisites

- Python **3.8+**  
- `pip` or `pipenv` for dependencies  

### Setup

```bash
# Clone the repository
git clone https://github.com/himanshu-1812/legal_simplifier.git
cd legal_simplifier

# Optional: create a virtual environment
python -m venv venv
# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
### Usage
## Install dependencies
pip install -r requirements.txt

- Run the Streamlit app:
```
- streamlit run app.py
```

- The app will open in your browser.
- Upload a PDF or text file.
- Click “Simplify Document”.
- The simplified summary appears, showing key clauses, terms, and risks in a clean format.

### Project Structure
- File / Folder	Description
app.py	Main Streamlit app UI
simplifier.py	Core logic for simplifying legal text (AI or rule-based processing)
requirements.txt	Python dependencies
venv/	Virtual environment (should be .gitignored, not pushed to GitHub)
.env	(Optional) API keys or environment variables

### Contributing

- Contributions are welcome!
If you'd like to improve the summarization, UI, or support more document types, feel free to:

  1.Fork the repo

  2.Create your feature branch (git checkout -b feature-name)

  3.Commit changes (git commit -m "Add feature")

  4.Push to your branch (git push origin feature-name)

  5.Open a pull request 

### License

- This project is provided as-is for educational/demo purposes.
- It does not constitute legal advice. Always consult a qualified legal professional for actual contracts or agreements.

