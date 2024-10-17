from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "#btn.btn-lg.btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini .price_color")