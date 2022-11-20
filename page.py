from element import BasePageElement
from locators import HeaderLocators, HamburgerMenuLocators, HomePageLocators, LoginPageLocators, YourCartPageLocators, CheckoutPageLocators, CheckoutReviewPageLocators, CheckoutCompletePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self, expected_title):
        """Verifies that the hardcoded text "Swag Labs" appears in page title"""
        return expected_title in self.driver.title

    def is_page_header_title_matches(self, expected_title):
        element = self.driver.find_element(*HeaderLocators.HEADER_TITLE)
        print("Header title: " + element.text)
        return expected_title in element.text


class LoginPage(BasePage):
    """Login page action methods come here"""

    
    def enter_username(self, username):
        """Enter username"""
        element = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT_BOX)
        element.send_keys(username)

    def enter_password(self, password):
        """Enter password"""
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_BOX)
        element.send_keys(password)

    def click_login_button(self):
        """Click login"""
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

    def login_error_displayed(self, message):
        """The username error message display status"""
        element = self.driver.find_element(*LoginPageLocators.LOGIN_ERROR_MESSAGE)
        actual_message_displayed = element.get_attribute("textContent")

        return message in actual_message_displayed


class HomePage(BasePage):
    """Home page action methods are here"""


    def open_hamburger_menu(self):
        """Open hamburger menu"""
        element = self.driver.find_element(*HomePageLocators.HAMBURGER_MENU)
        element.click()
         # Improve this wait statement
        self.driver.implicitly_wait(10)


    def click_logout(self):
        """Click logout link in the hamburger menu"""
        element = self.driver.find_element(*HamburgerMenuLocators.LOGOUT_LINK)
        element.click()

        # Check if login button exist
        login_button_exist = True
        try:
            login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        except NoSuchElementException:
            login_button_exist = False

        return login_button_exist

    
    def click_about(self):
        """Click about link in the hamburger menu"""
        element = self.driver.find_element(*HamburgerMenuLocators.ABOUT_LINK)
        element.click()
        # Check if current page is now https://saucelabs.com/
        current_url = self.driver.current_url
        print("Current URL: " + current_url)
        return current_url in "https://saucelabs.com/"

    
    def click_cart_button(self):
        element = self.driver.find_element(*HomePageLocators.SHOPPING_CART_LINK)
        element.click()


    def add_to_cart_item(self, target_item_name):
        """Add to cart a specific item"""
        inventory_items = self.driver.find_elements(*HomePageLocators.INVENTORY_LIST_ITEMS) 
        print("Number of items: " + str(len(inventory_items)))
        
        for item in inventory_items:
            item_name = item.find_element(*HomePageLocators.INVENTORY_LIST_ITEM_NAME)
            print("Item name: " + item_name.text)
            if item_name.text == target_item_name:
                item_button_element = item.find_element(*HomePageLocators.ITEM_ACTION_BUTTON)
                print("Button text before clicking: " + item_button_element.text)

                if item_button_element.text != "ADD TO CART":
                    return False

                item_button_element.click()
                self.driver.implicitly_wait(10)
                item_button_element = item.find_element(*HomePageLocators.ITEM_ACTION_BUTTON)
                print("Button text after clicking: " + item_button_element.text)

                if item_button_element.text != "REMOVE":
                    return False

                break

        return True


class YourCartPage(BasePage):
    """Cart page action methods are here"""

    def check_if_item_is_in_cart(self, target_item_name):
        cart_items = self.driver.find_elements(*YourCartPageLocators.CART_LIST) 
        print("Number of items: " + str(len(cart_items)))

        for item in cart_items:
            item_name = item.find_element(*YourCartPageLocators.CART_LIST_ITEM_NAME)
            print("Item name in cart list: " + item_name.text)
            if item_name.text == target_item_name:
                return True
        
        return False


    def click_checkout_button(self):
        element = self.driver.find_element(*YourCartPageLocators.CHECKOUT_BUTTON)
        element.click()


class enterFirstNameCheckoutInformation(BasePageElement):
    """Uses name attribute to locate element"""
    locator = "firstName"

class enterLastNameCheckoutInformation(BasePageElement):
    """Uses name attribute to locate element"""
    locator = "lastName"

class enterPostalCodeCheckoutInformation(BasePageElement):
    """Uses name attribute to locate element"""
    locator = "postalCode"


class CheckoutPage(BasePage):
    """Checkout page action methods are here"""
    enter_first_name_checkout_information = enterFirstNameCheckoutInformation()
    enter_last_name_checkout_information = enterLastNameCheckoutInformation()
    enter_postal_code_checkout_information = enterPostalCodeCheckoutInformation()

    def click_continue_button(self):
        element = self.driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON)
        element.click()


class CheckoutReviewPage(BasePage):
    """Checkout review page action methods are here"""

    def check_if_item_is_in_cart(self, target_item_name):
        cart_items = self.driver.find_elements(*CheckoutReviewPageLocators.CART_LIST) 
        print("Number of items: " + str(len(cart_items)))

        for item in cart_items:
            item_name = item.find_element(*CheckoutReviewPageLocators.CART_LIST_ITEM_NAME)
            print("Item name in checkout list: " + item_name.text)
            if item_name.text == target_item_name:
                return True
        
        return False

    def click_finish_button(self):
        element = self.driver.find_element(*CheckoutReviewPageLocators.FINISH_BUTTON)
        element.click()


class CheckoutCompletePage(BasePage):
    """Checkout complete page action methods are here"""

    def click_back_home_button(self):
        element = self.driver.find_element(*CheckoutCompletePageLocators.BACK_HOME_BUTTON)
        element.click()

    


    