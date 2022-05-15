import time

from .Base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
        )
        button_add_to_basket.click()

    def should_present_message_add_product_to_basket(self):
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        ).text
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET
        ).text
        product_name_in_success_message = self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT_WAS_ADDED_TO_BASKET
        ).text
        assert (
            product_name_in_success_message == product_title
        ), f'Добавленный товар "{product_name_in_success_message}", a не "{product_title}"'
        assert success_message == f"{product_title} has been added to your basket.", (
            f'Сообщение о добавлении товара в корзину "{success_message}",'
            f' не соответствует - "{product_title} has been added to your basket."'
        )

    def matches_price_in_basket_with_price_of_added_product(self):
        price_in_basket = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_PRICE
        ).text
        price_of_product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        assert (
            price_in_basket == price_of_product
        ), f'Цена товара в корзине "{price_in_basket}", не соответствует цене товара "{price_of_product}"'
