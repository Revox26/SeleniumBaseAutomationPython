from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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

    def test(self):
        pass
        # Retrieve the device list from self.variables
        # device_list = self.variables.get("device")
        # # Check if the device_list is "android" or "ios" and print a message accordingly
        # if device_list == "android":
        #     print("The device is:", device_list)
        # elif device_list == "ios":
        #     print("The device is:", device_list)
        # else:
        #     print("not found")

        # device_list = self.var1
        #
        # if device_list == "android":
        #     print("The device is:", device_list)
        # elif device_list == "ios":
        #     print("The device is:", device_list)
