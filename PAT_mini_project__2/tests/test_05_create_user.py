# tests/test_create_user.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

@pytest.mark.usefixtures("setup_browser")
class TestCreateUser:

    def test_create_and_login_new_user(self):
        """
               Test Flow:
               1. Log in as Admin
               2. Navigate to Admin section and create a new user
               3. Log out as Admin
               4. Log in using the newly created user credentials
               5. Verify successful login for both Admin and the new user
             """
        # Admin credentials
        admin_username = "Admin"
        admin_password = "admin123"
        # New user credentials to be created
        new_username = "ILAKKIYA_CS"
        new_password = "test@2025"

        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        admin_page = AdminPage(self.driver)

        # Step 1: Login as Admin
        login_page.login(admin_username, admin_password)
        assert dashboard_page.is_dashboard_loaded(), "Admin login passed"

        # Step 2: Create new user
        admin_page.go_to_admin()
        admin_page.add_user(
            employee_name="Ranga  Akunuri",
            username=new_username,
            password=new_password,
            role="ESS",
            status="Enabled"
        )

        # Step 3: Log out
        dashboard_page.logout()

        # Step 4: Login with new user
        login_page.login(new_username, new_password)
        assert dashboard_page.is_dashboard_loaded(), "New user login passed"
