# 💬 MiniChat - Real-Time Chat Application & QA Testing Suite

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)


Welcome to **MiniChat**, a real-time web messaging application paired with a comprehensive Quality Assurance (QA) suite. This repository serves as a showcase of software testing standards, incorporating end-to-end (E2E) functional testing, API test coverage, test case design, defect tracking, and automation best practices for **QA Manual, QA Automation, and QA Engineer** roles.

---


---

## 🚀 About the Project

**MiniChat** provides instant messaging capabilities between user clients. The application handles user sessions, real-time message broadcasting via WebSockets/HTTP endpoints, and data validation across common UI edge cases.

### Core Features
* Real-time text messaging between active users.
* Session management and user connectivity status.
* Input validation and responsive chat interface.
* Error handling for network drops and invalid payload deliveries.

### 2. Environment Setup

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/jluisvacan/IssuesGithub-Webhooks.git
cd minichat

# Create and activate virtual environment
python -m venv venv

# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

#Install FastAPI
pip install "fastapi[standard]"

#Execute mini chat
fastapi dev main.py