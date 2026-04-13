# 🎭 Playwright Automation Framework

This project is a professional-grade E2E test automation framework built with **Python** and **Playwright**. It follows the **Page Object Model (POM)** to ensure test scripts are readable, maintainable, and scalable.

---

## 🚀 Key Features

* **Page Object Model (POM):** Clean separation between test logic and UI interactions for better maintainability.
* **CI/CD Ready:** Integrated with **GitHub Actions** to trigger automated testing on every push or pull request.
* **Robust Reporting:** Automatic generation of **HTML reports** including execution logs and test summaries.
* **Secure Config:** Securely handles sensitive environment data (URLs, Credentials) using **GitHub Repository Secrets**.
* **Fail-Safe:** Built-in support for screenshot capture and trace logging on test failures.

---

## 🛠 Tech Stack

* **Language:** Python 3.11+
* **Test Runner:** Pytest
* **Automation:** Playwright
* **CI/CD:** GitHub Actions

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Bushra-Rafique/Automation-Testing.git](https://github.com/Bushra-Rafique/Automation-Testing.git)
   cd Playwright-Framework

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Install Playwright Browsers:**
   ```bash
   playwright install chromium

## Running Tests

1. **Run all tests (Headless mode):**
   ```bash
   pytest

2. **Run with Browser UI (Headed mode):**
   ```bash
   pytest --headed

## Generate HTML Report:
The framework is configured to generate a report automatically, typically found in: reports/report.html

## 👤 Author
**Bushra Rafique**