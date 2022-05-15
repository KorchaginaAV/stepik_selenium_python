from .BasePage import BasePage
from .Locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ).text
        assert (
            empty_basket_message == "Ваша корзина пуста Продолжить покупки"
        ), f"Корзина должна быть пустой, а она не пустая"
