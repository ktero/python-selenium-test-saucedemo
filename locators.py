from selenium.webdriver.common.by import By


class HeaderLocators(object):
    """A class for header locators. All header locators are found here"""

    HEADER_TITLE = (By.CSS_SELECTOR, "div#header_container > div.header_secondary_container > span.title")


class LoginPageLocators(object):
    """A class for login page locators. All login locators are here"""

    LOGIN_BUTTON        = (By.CSS_SELECTOR, 'input#login-button')
    USERNAME_INPUT_BOX  = (By.CSS_SELECTOR, 'input#user-name')
    PASSWORD_INPUT_BOX  = (By.CSS_SELECTOR, 'input#password')
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.error-message-container > h3')


class HamburgerMenuLocators(object):
    """A class for hamburger menu locators. All hamburger menu locators are here"""

    ALL_ITEMS_LINK       = (By.CSS_SELECTOR, 'div.bm-menu > nav.bm-item-list > a#inventory_sidebar_link')
    ABOUT_LINK           = (By.CSS_SELECTOR, 'div.bm-menu > nav.bm-item-list > a#about_sidebar_link')
    LOGOUT_LINK          = (By.CSS_SELECTOR, 'div.bm-menu > nav.bm-item-list > a#logout_sidebar_link')
    RESET_APP_STATE_LINK = (By.CSS_SELECTOR, 'div.bm-menu > nav.bm-item-list > a#reset_sidebar_link')

    
class HomePageLocators(object):
    """A class for home page locators. All home page locators are here"""

    # Item locators
    INVENTORY_LIST_ITEMS     = (By.CSS_SELECTOR, 'div#inventory_container > div.inventory_list > div.inventory_item')
    INVENTORY_LIST_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    ITEM_ACTION_BUTTON       = (By.CSS_SELECTOR, 'div.pricebar > button')

    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    HAMBURGER_MENU     = (By.CSS_SELECTOR, 'div.bm-burger-button > button#react-burger-menu-btn')


class YourCartPageLocators(object):
    """A class for cart page locators. All cart page locators are here."""

    CART_LIST           = (By.CSS_SELECTOR, "div.cart_list")
    CART_LIST_ITEM_NAME = (By.CSS_SELECTOR, "div.cart_item > div.cart_item_label > a")
    CHECKOUT_BUTTON     = (By.CSS_SELECTOR, "button#checkout")


class CheckoutPageLocators(object):
    """A class for checkout page locators. All checkout page locators are here."""

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input#continue")


class CheckoutReviewPageLocators(object):
    """A class for checkout review page locators. All checkout review page locators are here."""

    CART_LIST           = (By.CSS_SELECTOR, "div.cart_list")
    CART_LIST_ITEM_NAME = (By.CSS_SELECTOR, "div.cart_item > div.cart_item_label > a")
    SUMMARY_INFO        = (By.CSS_SELECTOR, "div.summary_info")
    FINISH_BUTTON       = (By.CSS_SELECTOR, "button#finish")
    CANCEL_BUTTON       = (By.CSS_SELECTOR, "button#cancel")


class CheckoutCompletePageLocators(object):
    """A class for checkout complete page locators. All checkout complete page locators are here."""

    BACK_HOME_BUTTON = (By.CSS_SELECTOR, "button#back-to-products")

