from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[name=registration-email]")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT_WAS_ADDED_TO_BASKET = (
        By.CSS_SELECTOR,
        ".alert:nth-child(1) strong",
    )
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) div")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner div.basket-items")
