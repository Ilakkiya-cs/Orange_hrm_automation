# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Model for the Login Page of OrangeHRM
    """
    def __init__(self, driver):
        # Initializes web element locators.
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def enter_username(self, username):
        # Inputs the username into the username field.
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        #Inputs the password into the password field.
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        # Clicks the login button to submit the login form.
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """
               Performs full login operation: enters credentials and clicks login.
                   username (str): Username for login.
                   password (str): Password for login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
#Retrieves the error message displayed on unsuccessful login.
        try:
            return self.driver.find_element(*self.error_message).text
        except Exception:
            return None

    def is_login_successful(self):
        # Checks whether login was successful by waiting for the dashboard to appear.
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return True
        except Exception:
            return False
