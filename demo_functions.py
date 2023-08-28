import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# So we don't have to download and install a Chrome Webdriver file
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def demo_login():

    try:
        # Initialize the Chrome webdriver
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        driver.maximize_window()  # Just a nicety
        driver.get('https://www.saucedemo.com')

        username_field = driver.find_element(By.ID, 'user-name')
        password_field = driver.find_element(By.ID, 'password')

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Allow the page time to load
        time.sleep(10)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser window, regardless of success or failure
        driver.quit()

def get_fleece_jacket_price():

    try:

        # Initialize the Chrome webdriver
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        driver.maximize_window()  # Just a nicety
        driver.get('https://www.saucedemo.com')

        username_field = driver.find_element(By.ID, 'user-name')
        password_field = driver.find_element(By.ID, 'password')

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Allow the page time to load
        time.sleep(3)

        # This is a brute force approach!
        items = driver.find_elements(By.CLASS_NAME, 'inventory_item_description')
        for item in items:
            if "Sauce Labs Fleece Jacket" in item.text:
                tokens = item.text.split()

                for item in tokens:
                    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                    try:
                        if int(item[-1]) in integers:
                            return item
                    except ValueError:
                        pass

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser window, regardless of success or failure
        driver.quit()

def add_first_item_to_cart():

    try:

        # Initialize the Chrome webdriver
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        driver.maximize_window()  # Just a nicety
        driver.get('https://www.saucedemo.com')

        username_field = driver.find_element(By.ID, 'user-name')
        password_field = driver.find_element(By.ID, 'password')

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Allow the page time to load
        time.sleep(3)

        try:
            button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
            button.click()
            time.sleep(5)

        except Exception as e:
            print(e)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser window, regardless of success or failure
        driver.quit()
