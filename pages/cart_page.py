from helps import (
    add_selector,
    cart_selector,
    product_selector,
    checkout_selector,
    firstname_selector,
    lastname_selector,
    postalcode_selector,
    continue_selector,
    finish_selector,
    complite_selector
)
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def add_button(self):
        return self.find_element(add_selector)

    def cart_button(self):
        return self.find_element(cart_selector)

    def check_product_in_cart(self):
        return self.find_element(product_selector).is_displayed()

    def checkout_button(self):
        return self.find_element(checkout_selector)

    def firstname_fild(self):
        return self.find_element(firstname_selector)

    def lastname_fild(self):
        return self.find_element(lastname_selector)

    def postal_code_fild(self):
        return self.find_element(postalcode_selector)

    def continue_button(self):
        return self.find_element(continue_selector)

    def checkout_complite(self):
        return self.find_element(complite_selector).is_displayed()

    def finish_button(self):
        return self.find_element(finish_selector)
