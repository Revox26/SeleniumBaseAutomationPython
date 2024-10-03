from datetime import datetime

from faker import Faker

from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities


class DestinationxLoginPage(AndroidCapabilities):
    email = '//android.widget.EditText[@resource-id="email"]'
    password = '//android.widget.EditText[@resource-id="password"]'
    destix_login = '//android.widget.Button[@content-desc="Login"]'
    sign_in_with_google = '//android.widget.TextView[@text="Sign in with Google"]'
    sign_in_with_apple = '//android.widget.TextView[@text="Sign in with Apple"]'
    create_an_account = '//android.widget.Button[@content-desc="Create an Account"]'
    forgot_password = '//android.widget.TextView[@text="Forgot Password?"]'
    forgot_password_email = '(//android.widget.EditText[@resource-id="email"])[1]'
    reset_password = '//android.widget.Button[@content-desc="Reset Password"]'

    def navigate_to_sign_in_with_google(self):
        mobile_action = MobileCustomActionClass()
        mobile_action.tap(self.sign_in_with_google)

    def navigate_to_sign_in_with_apple(self):
        mobile_action = MobileCustomActionClass()
        mobile_action.tap(self.sign_in_with_apple)

    def navigate_to_create_an_account(self):
        mobile_action = MobileCustomActionClass()
        mobile_action.tap(self.create_an_account)

    def navigate_to_login(self):
        mobile_action = MobileCustomActionClass()
        if mobile_action.assert_element(self.email, timeOut=2):
            pass
        else:
            mobile_action.tap(self.destix_login)

    def navigate_to_forgot_password(self):
        mobile_action = MobileCustomActionClass()

        fake = Faker()
        random_first_name = fake.first_name()
        random_surname = fake.last_name()
        timestamp = datetime.now().strftime("%H%M%S")
        random_email = random_first_name + "" + random_surname + timestamp + "@testing.com"

        mobile_action.tap(self.forgot_password)
        mobile_action.assert_element(self.reset_password)
        mobile_action.type_text(self.forgot_password_email, random_email)
        mobile_action.tap(self.reset_password)
