from .BasePage import BasePage
from .Locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        count_of_basket_items = len(basket_items)
        assert (
            count_of_basket_items == 0
        ), f"Корзина должна быть пустой, а она не пустая. Товаров в корзине {count_of_basket_items}"

    def should_be_message_of_empty_basket_(self):
        empty_basket_message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ).text
        assert (
            empty_basket_message == "Ваша корзина пуста Продолжить покупки"
        ), f"Корзина должна быть пустой, а она не пустая"
