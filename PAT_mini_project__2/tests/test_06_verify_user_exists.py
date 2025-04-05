# tests/test_search_user.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


@pytest.mark.usefixtures("setup_browser")
class TestSearchUser:
    def test_search_existing_user(self):
        """
               Steps:
               1. Log in as Admin
               2. Navigate to the Admin section
               3. Search for a specific user by username
               4. Validate that the user is found in the results
               5. Logout
               """
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        admin_page = AdminPage(self.driver)

        # Login as Admin
        login_page.login("Admin", "admin123")
        assert dashboard_page.is_dashboard_loaded(), "Dashboard should be loaded"

        # Go to Admin and search for user
        admin_page.go_to_admin()
        assert admin_page.search_user("ILAKKIYA_CS") is True, "ILAKKIYA_CS user should be found in search"
        #logout
        dashboard_page.logout()
