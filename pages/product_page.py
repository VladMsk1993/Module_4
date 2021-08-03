from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_button_to_add_to_basket(self):
        try:
            button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            button.click()
        except():
            assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "There's not the button"

    def should_see_product_page(self):
        current_url = self.browser.current_url
        substring = "promo=newYear"
        assert substring in current_url, "Guest is on wrong page."

    def should_see_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "There's wrong price or there's not price at all."

    def should_see_message_product_is_added(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT), "There's wrong product or there's not product at all."
