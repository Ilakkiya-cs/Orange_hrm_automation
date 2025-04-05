# tests/test_dashboard_menus.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup_browser")
class TestDashboardMenus:
    """
       Test class to verify that all expected dashboard menu items are visible and clickable
       after logging into the OrangeHRM system.
       """
    def test_all_dashboard_menus_are_visible(self):
        """- Logs into the application using Admin credentials
        - Verifies that the dashboard page loads successfully
        - Asserts visibility and clickability of each expected dashboard menu
        - Logs out after verification"""

        # Login as Admin
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.login("Admin", "admin123")

        # Verify that the dashboard is displayed
        assert dashboard_page.is_dashboard_loaded(), "Dashboard should be loaded"
        # Verify that all expected menus are visible and clickable
        assert dashboard_page.are_all_menus_visible_and_clickable(), "All menus should be visible and clickable"

        dashboard_page.logout()
