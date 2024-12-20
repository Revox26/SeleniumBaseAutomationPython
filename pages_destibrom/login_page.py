from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestiBromLoginPage(BaseCase):
    login_menu = "//a[contains(.,'Log in')]"
    email_address_destibrom = "//input[@id='email']"
    password_destibrom = "//input[@id='inputPassword']"
    login_button_destibrom = "//button[contains(.,'LOGIN')]"

    def login(self, username, password):
        self.type(self.email_address_destibrom, username)
        self.type(self.password_destibrom, password)
        self.click(self.login_button_destibrom)

    def navigate_to_login_menu(self):
        self.click(self.login_menu)

    def open_destibrom_page(self):
        self.open(Readconfig.get_destibrom_v1_url())

    def destibrom_login_as_super_admin(self):
        self.login("super_admin@destibrom.test", "Test@12345")

    def destibrom_login_as_admin(self):
        self.login("admin@destibrom.test", "Test@12345")
