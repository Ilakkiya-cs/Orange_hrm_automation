
#  OrangeHRM Test Automation 

This project automates the testing of the [OrangeHRM Demo Web Application]
(https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using *Python Selenium*, *Pytest*, and the *Page Object Model (POM)* framework. It includes 6 detailed test cases validating various aspects of the application, including login, UI elements, user creation, and more.

# Tools & Technologies


-  *Selenium WebDriver*
-  *Pytest*
-  *Page Object Model (POM)*
-  *Explicit Waits*
-  *Exception Handling*
-  *Pytest HTML Reports*
-  *PyLint Standards* for naming conventions

#Project Structure :

PAT_mini_project__2/
│
├── tests/                      # Test case scripts using Pytest
│   ├── test_01_login.py
│   ├── test_02_home_url.py
│   ├── test_03_login_fields_visibility.py
│   ├── test_04_dashboard_menus.py
│   ├── test_05_create_user.py
│   └── test_06_verify_user_exists.py
│
├── pages/                      # Page Object Model classes
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│  
│
├── reports/                    # HTML reports from test runs
│
├── conftest.py                 # Pytest fixtures and setup
├── requirements.txt            # Project dependencies
└── pytest.ini                  


# Test Cases Covered

### Test Case 1: Login Functionality
- Test with multiple username/passwords.
- Check login success and logout.
- Verify login using cookies.
- Generate Pytest HTML reports.

### Test Case 2: Home URL Verification
- Ensure home URL is accessible.
- Generate HTML report.

### Test Case 3: Input Field Visibility
- Validate visibility of username/password fields.
- Generate HTML report.

### Test Case 4: Dashboard Menus Verification
- Ensure all top menus are visible and clickable post-login.
- Generate HTML report.

### Test Case 5: User Creation and Login
- Create a new user via Admin panel.
- Verify new user can log in successfully.
- Generate HTML report.

### Test Case 6: User Existence Verification
- Check the newly created user exists in Admin records.
- Generate HTML report.


# Notes

- Ensure Chrome WebDriver is installed and added to your system's PATH.
- All test scripts follow **PyLint** naming conventions.
- The project is compatible with **PyCharm** and can be run without any errors if set up correctly.


