from helps import (
    password_selector,
    username_selector,
    submit_selector
)
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://www.saucedemo.com/"

    def __init__(self, browser) -> None:
        super().__init__(browser)

    def username_fild(self):
        return self.find_element(username_selector)

    def password_fild(self):
        return self.find_element(password_selector)

    def login_button(self):
        return self.find_element(submit_selector)
