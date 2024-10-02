from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities
from faker import Faker
from datetime import datetime
from configuration_files.config_reader import Readconfig


class DestinationxCreateAnAccountPage(AndroidCapabilities):
    create_an_account_button = '//android.widget.TextView[@text="Create an account"]'
    first_name = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="First Name"]'
    surname = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Surname"]'
    email_address = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Email Address"]'
    password_ = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Password"]'
    confirm_password_ = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Confirm Password"]'
    sign_up_button = '//android.widget.Button[@content-desc="Signup"]'
    cancel_button = '//android.widget.TextView[@text="Cancel"]'

    def register_new_account(self):
        mobile_action = MobileCustomActionClass()

        fake = Faker()
        random_first_name = fake.first_name()
        random_surname = fake.last_name()
        timestamp = datetime.now().strftime("%H%M%S")
        random_email = random_first_name + "" + random_surname + timestamp + "@testing.com"

        mobile_action.swipe_down_until_element_is_visible(self.create_an_account_button)
        mobile_action.tap(self.create_an_account_button)
        mobile_action.type_text(self.first_name, random_first_name)
        mobile_action.type_text(self.surname, random_surname)
        mobile_action.type_text(self.email_address, random_email)
        mobile_action.type_text(self.password_, Readconfig.get_director_password())
        mobile_action.type_text(self.confirm_password_, Readconfig.get_director_password())
        mobile_action.tap(self.sign_up_button)
