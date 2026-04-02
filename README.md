# UI Test Automation Framework (Python + Playwright + Pytest)

This project demonstrates a lightweight UI test automation framework built using Python, Playwright, and Pytest. It was developed to simulate real-world test automation workflows, focusing on validating user interactions, detecting defects, and structuring maintainable test code.

---

## Purpose

The goal of this project is to demonstrate practical automation engineering skills, including:

- Automating user workflows (login, cart, navigation)
- Validating application behavior through assertions
- Structuring reusable and maintainable test components
- Simulating real-world test scenarios and edge cases

---

## Features

- Automated UI testing using Playwright (Chromium)
- Pytest-based test execution
- Reusable fixtures for browser and page setup
- Workflow-based test scenarios (login, add-to-cart, navigation)
- Clean structure designed for scalability

---

## Tech Stack

- Python 3.x  
- Playwright  
- Pytest  
- Chromium browser  

---

## Project Structure

playwright-automation-framework/
│
├── tests/
│   ├── test_add_to_cart.py
│   └── test_login.py
│
├── requirements.txt
└── README.md

---

## Installation

Install dependencies:

```bash
pip install playwright pytest
playwright install
```

---

## Running Tests

Run all tests:
```bash
pytest
```

Run with browser visible:
```bash
pytest --headed
```

Run a specific test:
```bash
pytest tests/test_add_to_cart.py
```

---

## Example Test Coverage

This framework includes tests that validate:

- User login functionality  
- Navigation between pages  
- Add-to-cart workflow  
- UI interaction and expected behavior  

---

## Future Enhancements

- Implement Page Object Model (POM)
- Add test reporting (HTML / Allure)
- Integrate CI pipeline (GitHub Actions)
- Expand test coverage and edge case scenarios

---

## Approach

This framework was designed with a focus on readability, reusability, and scalability. Test logic is separated from setup using fixtures, and workflows are structured to reflect real user behavior rather than isolated actions.

---

## Author

Gregory G. Garland  
GitHub: https://github.com/Initiate64
