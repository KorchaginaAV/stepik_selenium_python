from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT_WAS_ADDED_TO_BASKET = (
        By.CSS_SELECTOR,
        ".alert:nth-child(1) strong",
    )
    SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) div")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")