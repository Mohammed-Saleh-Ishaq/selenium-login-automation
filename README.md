# Selenium-Login-automation

This is a **Selenium-based automation project** for testing the **login and logout functionality** of the [OrangeHRM demo application].
It follows the **Page Object Model (POM)** design pattern and uses **unittest** as the testing framework with optional HTML reports.


---

## 🌐 Website used for Under Test

[https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)

---

## 🧰 Tools & Technologies

- **Python**
- **Selenium WebDriver**
- **unittest (built-in Python framework)**
- **ChromeDriver**
- **HtmlTestRunner (optional for reports)**

---

## 📁 Project Structure

selenium_project/

├── venv/ # Virtual environment

├── reports/ # test

│ └── Test Report for Test 1

│ └── Test Report for Test 1 & Test 2

├── sample_project/

│ └── page_object_model_project/   (POM)

│ └── locators/

│ └── locator.py

│ ├── Drivers/ # ChromeDriver goes here

│ ├── Pages/ # Page Object files (optional)

│ └── Tests/

│ └── login.py # Your test script

├── requirements.txt

└── README.md

---

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git@github.com:Mohammed-Saleh-Ishaq/selenium-login-automation.git

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

---
📑 Test Cases
1. ✅ Valid Login & Logout
   -- Enters correct username/password.
   -- Verifies successful login and logout.
2. ❌ Invalid Username
   -- Enters invalid username with valid password.
   -- Verifies error message: "Invalid credentials".

---
📊 Sample Reports
Reports are generated using HtmlTestRunner:
   -- Test 1: Only valid login test
   -- Test 2: Valid + Invalid login tests

   
