🎭 Playwright Automation Framework
This project is a professional-grade E2E test automation framework built with Python and Playwright. It follows the Page Object Model (POM) to ensure test scripts are readable, maintainable, and scalable.

🚀 Key Features
Page Object Model (POM): Clean separation between test logic and UI interactions.

CI/CD Ready: Integrated with GitHub Actions for automated testing on every push.

Robust Reporting: Automatic generation of HTML reports with execution logs.

Secure Config: Handles sensitive environment data using Repository Secrets.

Fail-Safe: Built-in support for screenshot capture on test failure.

🛠 Tech Stack
Language: Python 3.11+

Test Runner: Pytest

Automation: Playwright

CI/CD: GitHub Actions

💻 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/Bushra-Rafique/Automation-Testing.git
cd Playwright-Framework
Install dependencies:

Bash
pip install -r requirements.txt
playwright install chromium
🧪 Running Tests
Run all tests (Headless):

Bash
pytest
Run with Browser UI (Headed):

Bash
pytest --headed