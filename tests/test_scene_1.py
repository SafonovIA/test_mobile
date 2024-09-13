from pages.login_page import LoginPage
from pages.cart_page import CartPage
import allure


@allure.feature("scene_1")
def test_scene_1(browser):
    login_page = LoginPage(browser)
    cart_page = CartPage(browser)

    with allure.step("Open page"):
        login_page.open()
        assert browser.current_url == "https://www.saucedemo.com/"

    with allure.step("Login"):
        login_page.username_fild().send_keys("standard_user")
        login_page.password_fild().send_keys("secret_sauce")
        login_page.login_button().click()
        assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    with allure.step("Add product"):
        cart_page.add_button().click()
        cart_page.cart_button().click()
        assert cart_page.check_product_in_cart()

    with allure.step("Offer"):
        cart_page.checkout_button().click()

        cart_page.firstname_fild().send_keys("some_name")
        cart_page.lastname_fild().send_keys("some_lastname")
        cart_page.postal_code_fild().send_keys("some_post")

        cart_page.continue_button().click()
        cart_page.finish_button().click()

        assert cart_page.checkout_complite()
