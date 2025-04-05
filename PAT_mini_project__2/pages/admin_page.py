# pages/admin_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AdminPage:
    """
    Page Object Model for the Admin section (User Management)
    """
    def __init__(self, driver):

        """
                Initializing the web elements used across Admin page operations.
        """
        self.driver = driver
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.user_role_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.status_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        self.username_input = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.password_input = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password_input = (By.XPATH, "(//input[@type='password'])[2]")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
        self.search_input = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.user_cell = lambda username: (By.XPATH, f"//div[contains(text(),'{username}')]")

    def go_to_admin(self):

        """
                Clicks on the Admin menu to navigate to the Admin section.
                Waits until the Admin menu item is clickable.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()

    def add_user(self, employee_name, username, password, role="ESS", status="Enabled"):

        """
              Adds a new user with specified parameters:
              role, status, employee name, username, and password.
        """
        # Click Add button
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

        # Select the user role from dropdown
        role_dropdown = self.driver.find_element(By.XPATH,
                                                 "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        role_dropdown.click()
        self.driver.find_element(By.XPATH, f"//div[@role='listbox']//span[text()='{role}']").click()

        # Enter employee name and select from auto-suggest
        emp_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        emp_input.send_keys(employee_name)
        time.sleep(1)  # Optional: wait for suggestions to load
        self.driver.find_element(By.XPATH, f"//span[contains(text(),'{employee_name.split()[0]}')]").click()

        # Select user status from dropdown
        status_dropdown = self.driver.find_element(By.XPATH,
                                                   "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        status_dropdown.click()
        self.driver.find_element(By.XPATH, f"//div[@role='listbox']//span[text()='{status}']").click()

        # Set Username
        self.driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div//input").send_keys(
            username)

        # Set Password
        self.driver.find_element(By.XPATH, "//label[text()='Password']/../following-sibling::div//input").send_keys(
            password)

        # Confirm Password
        self.driver.find_element(By.XPATH,
                                 "//label[text()='Confirm Password']/../following-sibling::div//input").send_keys(
            password)

        # Save
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)  # wait for user creation to complete

    def search_user(self, username):

        """
                Searches for a user by username.
                Returns True if user is found in search results, False otherwise.
        """
        # Enter username into search input and click 'Search'
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        ).send_keys(username)
        self.driver.find_element(*self.search_button).click()
        time.sleep(2)
        try:
            self.driver.find_element(*self.user_cell(username))
            return True
        except Exception:
            return False
