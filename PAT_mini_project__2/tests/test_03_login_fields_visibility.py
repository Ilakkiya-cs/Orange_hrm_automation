# tests/test_login_fields_visibility.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_browser")
class TestLoginFields:
    """
       Test class to verify that the login fields (username, password, and login button)
       are visible on the OrangeHRM login page.
       """
    def test_login_fields_are_visible(self):
        """
               Waits for the username, password, and login button elements to be visible,
        """
        wait = WebDriverWait(self.driver, 10)

        username_visible = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_visible = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        login_button_visible = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # Verify all three elements are displayed
        assert username_visible.is_displayed(), "Username input should be visible"
        assert password_visible.is_displayed(), "Password input should be visible"
        assert login_button_visible.is_displayed(), "Login button should be visible"
