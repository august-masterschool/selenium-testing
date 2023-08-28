import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# So we don't have to download and install a Chrome Webdriver file
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestDemoFunctions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        self.driver.maximize_window()  # Just a nicety
        self.driver.get('https://www.saucedemo.com')

    def test_demo_login(self):
        username_field = self.driver.find_element(By.ID, 'user-name')
        password_field = self.driver.find_element(By.ID, 'password')

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Allow the page time to load
        time.sleep(1)

        # Successful login redirects to Products page
        secondary_header = self.driver.find_element(By.CLASS_NAME, "header_secondary_container")
        secondary_header_tokens = secondary_header.text.split()
        self.assertEqual(secondary_header_tokens[0], "Products")

    def test_add_first_item_to_cart(self):
        pass

    def test_get_fleece_jacket_price(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()