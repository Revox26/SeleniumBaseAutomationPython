from seleniumbase import BaseCase
import random
from configuration_files.config_reader import Readconfig


class DirectorAccountDetailsPage(BaseCase):
    email_account = "//input[@name='email']"
    password_account = "//input[@name='password']"
    confirm_password = "//input[@name='password_confirmation']"
    auth_1 = "//input[@id='authtype1_val']"
    auth_2 = "//input[@id='authtype2_val']"
    auth_3 = "//input[@id='authtype3_val']"
    i_confirm = "//input[@name='tos']"
    continue_button = "//button[contains(.,'Continue')]"
    yes_continue_button = "//button[@id='is-duplicate-yes']"

    def director_account_details(self):
        with open("..//data//first_name.txt", "r") as file:
            email = file.read().strip()
            random_number = random.randint(100, 999)
            result = str(random_number) + "@automation.com"
        with open("..//data//email.txt", "w") as file:
            file.write(email + result)

        self.type(self.email_account, email + result)
        self.type(self.password_account, Readconfig.get_director_password())
        self.type(self.confirm_password, Readconfig.get_director_password())
        self.type(self.auth_1, "123")
        self.type(self.auth_2, "123")
        self.type(self.auth_3, "abc")
        self.click(self.i_confirm)
        self.click(self.continue_button)
        self.click(self.yes_continue_button, timeout=60)
