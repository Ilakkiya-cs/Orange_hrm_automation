# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup_browser(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Setup ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(10)
    # Navigate to the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    request.cls.driver = driver
    # Yield control to the test and quit browser after execution
    yield
    driver.quit()



@pytest.fixture
def wait_for_element():
    def _wait(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    return _wait
