from faker import Faker
from seleniumbase import BaseCase


class BscRedeemPackagePage(BaseCase):
    rp_accept = "//button[contains(text(),'I accept')]"
    redeem_package_next = "//button[.='Next']"
    rp_first_name = "//input[@data-testid='field-First Name']"
    rp_email_address = "//input[@data-testid='field-Email Address']"
    rp_i_agree_1 = "//div[.='Angstrom BPO Package']/following-sibling::div//label[@for='terms']"
    rp_i_agree_2 = "//div[.='Elixir Accounts']/following-sibling::div//label[@for='terms']"
    rp_check_out_button = "(//button[contains(@data-testid,'checkout-button')])[2]"

    # pytest test_bsc_redeem_package.py --slow
    def open_bsc_redeem_package(self):
        self.open("https://uat-web-tbsc.azurewebsites.net/packages/redeem?code=dfc-P-230731-091721")
        self.click(self.rp_accept)
        self.click(self.redeem_package_next)

    def provide_following_information(self):
        fake = Faker()
        random_name = fake.first_name()
        random_last_name = fake.last_name()

        with open("..//data//first_name.txt", "w") as file:
            file.write(random_name)
        with open("..//data//last_name.txt", "w") as file:
            file.write(random_last_name)
        random_email = random_name + random_last_name + "@bsc.com"
        with open("..//data//email.txt", "w") as file:
            file.write(random_email)

        print("\n Name: ", random_name, "\n Last Name: ", random_last_name, "\n Email: ", random_email)

        self.type(self.rp_first_name, random_name)
        self.type(self.rp_email_address, random_email)
        self.scroll_into_view(self.rp_check_out_button)
        self.js_click(self.rp_i_agree_1)
        self.js_click(self.rp_i_agree_2)
        self.click(self.rp_check_out_button)
