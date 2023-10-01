from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class BscCreateYOurAccountPage(BaseCase):
    _bsc_acc_first_name = "input[placeholder='First Name']"
    _bsc_acc_last_name = "input[placeholder='Last Name']"
    bsc_acc_email = "input[placeholder='E-mail Address']"
    bsc_acc_password = "input[placeholder='Enter your password']"
    bsc_acc_confirm_password = "input[placeholder='Confirm your password']"
    i_agree_to_the_terms = "div[class='p-3 w-100'] label[for='terms']"
    bsc_proceed_button = "button[type='submit']"

    def create_your_bsc_account(self):
        with open("first_name.txt", "r") as file:
            input_bsc_acc_first_name = file.read().strip()
        with open("last_name.txt", "r") as file:
            input_bsc_acc_last_name = file.read().strip()
        with open("email.txt", "r") as file:
            input_bsc_acc_email = file.read().strip()

        self.type(self._bsc_acc_first_name, input_bsc_acc_first_name)
        self.type(self._bsc_acc_last_name, input_bsc_acc_last_name)
        self.type(self.bsc_acc_email, input_bsc_acc_email)

        self.type(self.bsc_acc_password, Readconfig.get_director_password())
        self.type(self.bsc_acc_confirm_password, Readconfig.get_director_password())
        self.js_click(self.i_agree_to_the_terms)
        self.js_click(self.bsc_proceed_button)
        self.sleep(5)

    def create_account_after_redeem(self):
        with open("first_name.txt", "r") as file:
            random_name = file.read().strip()

        with open("last_name.txt", "r") as file:
            random_last_name = file.read().strip()

        with open("email.txt", "r") as file:
            random_email = file.read().strip()

        self.type(self._bsc_acc_first_name, random_name)
        self.type(self._bsc_acc_last_name, random_last_name)
        self.type(self.bsc_acc_email, random_email)

        self.type(self.bsc_acc_password, Readconfig.get_director_password())
        self.type(self.bsc_acc_confirm_password, Readconfig.get_director_password())
        self.js_click(self.i_agree_to_the_terms)
        self.js_click(self.bsc_proceed_button)
        self.sleep(5)
