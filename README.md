# AI QA Framework (python_practice)

## 📌 Project Overview
The **AI QA Framework** is a Python-based quality engineering solution that leverages Playwright, pytest, and AI-driven test generation. It is designed to automate UI, API, and feature-level regression testing while integrating with external systems like Jira. The framework emphasizes modularity, clean reporting, and scalability toward a future **AI QE Platform**.

---

---

✨ This README shows both the **current structure** and the **future platform roadmap**, making it clear that your repo is not just a framework but a growing platform.  

Would you like me to also add **badges** (Python version, pytest, Playwright, CI/CD status) at the top so the README has those eye‑catching shields? They make repos look polished and professional.


## 📂 Current Project Structure
python_practice/
│
├── ai_engine/              # Core AI-driven test generation and orchestration
│   ├── generators/          # UI, API, feature, and step test generators
│   ├── integrations/        # Jira client integration
│   ├── prompts/             # Prompt templates for test generation
│   ├── utils/               # Utilities (e.g., screenshots)
│   ├── llm_client.py        # LLM interface
│   └── orchestrator.py      # Test orchestration logic
│
├── fixtures/                # Pytest fixtures (e.g., browser setup)
├── pages/                   # Page Object Models (login, dashboard, etc.)
├── tests/                   # Features, step definitions, and UI tests
├── test_intents/            # JSON test intent definitions
├── reports/                 # Allure results, screenshots, traces
├── scripts/                 # Helper scripts (e.g., test generation)
├── conftest.py              # Pytest configuration
├── pytest.ini               # Pytest settings
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md


---

## 🚀 Future Roadmap: AI QE Platform
The framework is evolving into a **platform architecture** for broader scalability and governance:

python_practice/
│
├── ai_qe_platform/
│   ├── ai_engine/           # Generators, prompts, integrations, orchestration, utils
│   ├── execution/           # UI, API, performance, database test execution
│   ├── reporting/           # Allure, traces, screenshots, logs
│   ├── cli/                 # Command-line interface (main.py)
│   ├── config/              # Configurations
│   └── platform/            # Governance, intelligence, analytics
│
├── tests/
├── test_intents/
├── azure-pipelines.yml      # CI/CD pipeline definition
├── requirements.txt
├── setup.py                 # Packaging and distribution
└── README.md


---

## ⚙️ Installation Guide
### Prerequisites
- Python 3.9+
- Node.js (for Playwright)
- Git

### Setup
```bash
git clone https://github.com/Git-Lopez/AI_QA_FRAMEWORK.git
cd AI_QA_FRAMEWORK
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
playwright install
Run all Test: pytest
Run with Allure: "pytest --alluredir=reports/allure-results
allure serve reports/allure-results
"
Run with playwright traces : "pytest --tracing on --screenshots on
"

Key Features
AI-driven test generation (UI, API, feature, step)
Prompt-based orchestration for flexible test design
Page Object Models for maintainable UI automation
Pytest fixtures for modular setup
Jira integration for test management
Allure reporting with screenshots and traces
CI/CD ready with Azure Pipelines

Contributing:
Fork the repository
Create a feature branch (git checkout -b feature-name)
Commit changes (git commit -m "Add feature")
Push to branch (git push origin feature-name)
Open a Pull Request
