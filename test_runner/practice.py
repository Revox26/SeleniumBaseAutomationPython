from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.click("button#checkout")
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Automation")
        self.type("#postal-code", "77123")
        self.click("input#continue")
        self.click("button#finish")
        self.assert_exact_text("Thank you for your order!", "h2")
        self.js_click("a#logout_sidebar_link")
        self.assert_element("div#login_button_container")
