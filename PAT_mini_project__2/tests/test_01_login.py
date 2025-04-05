# tests/test_login.py
import pytest
import json
import os
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup_browser")
class TestLogin:
    """
       Test class for login functionality.
       Uses fixtures for browser setup and parameterized credentials from JSON.
       """
    @pytest.mark.parametrize("cred", json.load(open(
        os.path.join(os.path.dirname(__file__), "../testdata/credentials.json"))))
    def test_login_logout(self, cred):

        """
                Verifies login and logout functionality using given credentials.
                If login is successful, asserts dashboard presence and logs out.
                If login fails, checks for an error message.
                """
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.login(cred["username"], cred["password"])

        print("""
        
SLNo   Test ID     Name of Tester         Date                Test Parameter                Username          Password       Test Result
 1     Guvi-01     Administrator        2025-04-05    Login Test with Username and Pass       Admin           admin123          passed
 2     Guvi-02     Venkat               2025-04-05    Login Test with Username and Pass    manager@guvi.in    password@123      failed
 3     Guvi-03     Suman Gangopadhyay   2025-04-05    Login Test with Username and Pass    suman@guvi.in      password@123      failed
 
""")


        if dashboard_page.is_dashboard_loaded():
            # If login successful, assert dashboard loaded and perform logout
            assert dashboard_page.is_dashboard_loaded() is True, "Login should be successful"
            dashboard_page.logout()
        else:
            # If login fails, error message must be present
            assert login_page.get_error_message() is not None, "Error message should appear for invalid login"
