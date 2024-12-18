from faker import Faker
from seleniumbase import BaseCase
from configuration_files.business_centre_config_reader import ReadBusinessCentreConfig


class BusinessCentreLoginPage(BaseCase):
    log_in_to_your_account_label = "//h2[.='Log in to your account']"
    sign_up_for_an_account_label = "//h2[.='Sign up for an account']"
    email_address_business_centre = "//input[@id='email']"
    password_business_centre = "//input[@id='password']"
    login_button_business_centre = "//button[.='Log in']"
    sign_up_button_business_centre = "//button[contains(text(),'Sign Up')]"
    terms_by_creating_an_account = "//input[@id='terms']"

    dont_have_ann_account_sign_up_button = "//a[.='Sign Up']"

    def _generate_and_save_email(self):
        fake = Faker()
        random_email = fake.email()
        with open("..//data//email.txt", "w") as file:
            file.write(random_email)
        print("Email address: ", random_email)
        return random_email

    def signup(self, username, password):
        self.click(self.dont_have_ann_account_sign_up_button)
        self.assert_element(self.sign_up_for_an_account_label)
        self.type(self.email_address_business_centre, username)
        self.type(self.password_business_centre, password)
        self.click(self.terms_by_creating_an_account)
        self.click(self.sign_up_button_business_centre)

    def login(self, username, password):
        self.assert_element(self.log_in_to_your_account_label)
        self.type(self.email_address_business_centre, username)
        self.type(self.password_business_centre, password)
        self.click(self.login_button_business_centre)

    def open_business_centre_page(self):
        self.open(ReadBusinessCentreConfig.get_bc_staging())

    def login_as_user(self):
        with open("..//data//email.txt", "r") as file:
            random_email = file.read().strip()
        self.login(random_email, "Test@12345")

    def signup_as_user(self):
        random_email = self._generate_and_save_email()
        self.signup(random_email, "Test@12345")
