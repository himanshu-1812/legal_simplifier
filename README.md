# Legal Document Simplifier

**AI-powered tool to turn complex legal documents into clear, readable summaries.**

---

## 🚀 Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 📋 Overview

Many legal documents—rental agreements, contracts, terms of service—are written in complicated, technical language. This makes them hard to understand, especially for non-lawyers.

**Legal Document Simplifier** solves that by:

- Extracting key clauses and responsibilities  
- Summarizing obligations and terms in plain English  
- Highlighting potential risks and financial commitments  

The goal is to empower people to understand what they are agreeing to—without needing legal training.

---

## ✨ Features

- Upload PDF or TXT files  
- Extract the text content from documents  
- Generate summaries that focus on **parties**, **term**, **rent / fees**, **obligations**, **termination**, **risks**, etc.  
- User-friendly interface with clear, structured output  
- No legalese—just straight-to-the-point, readable summaries  

---

## 🛠 Getting Started

### Prerequisites

- Python 3.8 or newer  
- *pip* or *pipenv* for dependencies  

### Setup

```bash
# Clone the repository
git clone https://github.com/himanshu-1812/legal_simplifier.git
cd legal_simplifier

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

# Install dependencies
pip install -r requirements.txt
