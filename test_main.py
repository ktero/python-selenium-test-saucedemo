"""
Using Python Unittesting with Selenium to execute automation testing in https://www.saucedemo.com/
"""

import unittest
import page
from selenium import webdriver


class SauceDemoLogin(unittest.TestCase):
    
    def setUp(self):
        WEB_URL = "https://www.saucedemo.com/" 
        self.driver = webdriver.Chrome()
        self.driver.get(WEB_URL)


    def test_login_successful(self):
        """
        Description: Login with the correct username and password
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user"
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        #Checks if the word "Swag Labs" is in title
        expectedTitle = "Swag Labs"
        self.assertTrue(login_page.is_title_matches(expectedTitle), "saucedemo.com title doesn't match.")

    
    def test_login_unsuccessful(self):
        """
        Description: Login using either the wrong username and/or wrong password
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user1"
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        error_message = "Epic sadface: Username and password do not match any user in this service"
        self.assertTrue(login_page.login_error_displayed(error_message), "Error message: " + error_message + " is not displayed.")


    def test_login_no_username(self):
        """
        Description: Login with no username and correct password
        """
        login_page = page.LoginPage(self.driver)
        username = ""
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        error_message = "Epic sadface: Username is required"
        self.assertTrue(login_page.login_error_displayed(error_message), "Error message: " + error_message + " is not displayed.")


    def test_login_no_password(self):
        """
        Description: Login with correct username and no password
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user"
        password = ""
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        error_message = "Epic sadface: Password is required"
        self.assertTrue(login_page.login_error_displayed(error_message), "Error message: " + error_message + " is not displayed.")


    def tearDown(self):
        self.driver.close()


class SauceDemoHamburgerMenu(unittest.TestCase):


    def setUp(self):
        WEB_URL = "https://www.saucedemo.com/" 
        self.driver = webdriver.Chrome()
        self.driver.get(WEB_URL)


    def test_logout(self):
        """
        Description: Open Hamburger menu and click Logout link
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user"
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        home_page = page.HomePage(self.driver)
        home_page.open_hamburger_menu()
        self.assertTrue(home_page.click_logout(), "Did not go back to login page.")


    def test_about(self):
        """
        Description: Open Hamburger menu and click About link
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user"
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        home_page = page.HomePage(self.driver)
        home_page.open_hamburger_menu()
        self.assertTrue(home_page.click_about(), "Did not navigate to https://saucelabs.com/ page.")


    def tearDown(self):
        self.driver.close()


class SauceDemoPurchase(unittest.TestCase):


    def setUp(self):
        WEB_URL = "https://www.saucedemo.com/" 
        self.driver = webdriver.Chrome()
        self.driver.get(WEB_URL)


    def test_checkout_single_item(self):
        """
        Description: Checkout a single item
        """
        login_page = page.LoginPage(self.driver)
        username = "standard_user"
        password = "secret_sauce"
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        home_page = page.HomePage(self.driver)
        target_item = "Sauce Labs Bike Light"
        # Add to cart
        self.assertTrue(home_page.add_to_cart_item(target_item), "Failed to add to cart item " + target_item + ".")
        home_page.click_cart_button()
        header_title = "YOUR CART"
        self.assertTrue(home_page.is_page_header_title_matches(header_title), "Page did not navigate to " + header_title)
        
        # Check if item is in cart and, if item is present, proceed to checkout
        your_cart_page = page.YourCartPage(self.driver)
        self.assertTrue(your_cart_page.check_if_item_is_in_cart(target_item), "Item " + target_item + " not found in cart list.")
        your_cart_page.click_checkout_button()
        header_title = "CHECKOUT: YOUR INFORMATION"
        self.assertTrue(your_cart_page.is_page_header_title_matches(header_title), "Page did not navigate to " + header_title)

        # Enter checkout information and continue
        checkout_page = page.CheckoutPage(self.driver)
        checkout_page.enter_first_name_checkout_information  = "John"
        checkout_page.enter_last_name_checkout_information   = "Doe"
        checkout_page.enter_postal_code_checkout_information = "1000"
        checkout_page.click_continue_button()
        header_title = "CHECKOUT: OVERVIEW"
        self.assertTrue(checkout_page.is_page_header_title_matches(header_title), "Page did not navigate to " + header_title)
        
        # Review checkout information and finish checkout
        checkout_review_page = page.CheckoutReviewPage(self.driver)
         # Check if item is in cart and, if item is present, proceed to checkout
        self.assertTrue(checkout_review_page.check_if_item_is_in_cart(target_item), "Item " + target_item + " not found in cart list.")
        checkout_review_page.click_finish_button()
        header_title = "CHECKOUT: COMPLETE!"
        self.assertTrue(checkout_review_page.is_page_header_title_matches(header_title), "Page did not navigate to " + header_title)

        # Checkout is complete and will go back to home page
        checkout_complete_page = page.CheckoutCompletePage(self.driver)
        checkout_complete_page.click_back_home_button()

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()