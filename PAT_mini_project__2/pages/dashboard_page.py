# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    """
    Page Object Model for the Dashboard Page which
    Encapsulates behavior for verifying the dashboard load, menu visibility, and logout functionality.
    """
    def __init__(self, driver):

        """
               Initializes web elements for the dashboard page.
        """
        self.driver = driver
        self.dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

        # Dictionary of main menu items and their respective locators
        self.menu_items = {
            "Admin": (By.XPATH, "a[@href='/web/index.php/admin/viewAdminModule']"),
            "PIM": (By.XPATH, "//span[text()='PIM']"),
            "Leave": (By.XPATH, "//span[text()='Leave']"),
            "Time": (By.XPATH, "//span[text()='Time']"),
            "Recruitment": (By.XPATH, "//span[text()='Recruitment']"),
            "My Info": (By.XPATH, "//span[text()='My Info']"),
            "Performance": (By.XPATH, "//span[text()='Performance']"),
            "Dashboard": (By.XPATH, "//span[text()='Dashboard']"),
        }
        self.profile_icon = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def is_dashboard_loaded(self):

        """
               Verifies whether the Dashboard heading is visible, indicating page load.
               Returns:
                   bool: True if dashboard is visible, False otherwise.
               """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.dashboard_heading)
            )
            return True
        except Exception:
            return False

    def are_all_menus_visible_and_clickable(self):

        """
              Checks whether all expected menu items are visible and clickable.

              Returns:
                  bool: True if all menus are properly loaded and interactable, False otherwise.
              """
        expected_menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

        for menu in expected_menus:
            try:
                # Locate menu item and verify visibility and clickability
                element = self.driver.find_element(By.XPATH, f"//span[text()='{menu}']")
                if not (element.is_displayed() and element.is_enabled()):
                    print(f" Menu '{menu}' is not visible or clickable")
                    return False
                else:
                    print(f" Menu '{menu}' is visible and clickable")
            except Exception as e:
                print(f" Menu '{menu}' not found: {e}")
                return False

        return True

    def logout(self):

        """
               Logs the current user out of the application via the profile dropdown.

               Raises:
                   RuntimeError: If logout fails due to any exception.
               """
        try:
            # Open user dropdown
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.profile_icon)
            ).click()
            # Click on the Logout link
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.logout_link)
            ).click()
        except Exception as exc:
            raise RuntimeError("Logout failed") from exc
