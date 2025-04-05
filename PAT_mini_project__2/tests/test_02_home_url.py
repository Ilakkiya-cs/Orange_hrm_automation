# tests/test_home_url.py
import pytest

@pytest.mark.usefixtures("setup_browser")
class TestHomeURL:
    # Test class to verify the home page URL and title of the OrangeHRM login page.
    def test_home_page_url_and_title(self):
        #Checks if the current URL and title of the page match the expected login page.
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        expected_title = "OrangeHRM"

        actual_url = self.driver.current_url
        actual_title = self.driver.title

        print("The Home URL is working")
        # Assert the current URL contains the expected URL
        assert expected_url in actual_url, f"Expected URL to contain {expected_url}"
        # Assert the title matches the expected title
        assert expected_title in actual_title, f"Expected title to contain {expected_title}"
