from appium.webdriver.common.appiumby import AppiumBy

from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.pages_csl_mobile.android_capabilities import AndroidCapabilities


class CslMobileLoginPage(AndroidCapabilities):
    csl_mobile_app = '//android.widget.TextView[@content-desc="CSL"]'
    new_user_verify_referral_code = '//android.widget.TextView[@text="New user? Verify Referral Code"]'
    referral_code_textbox = '//android.widget.EditText[@resource-id="RNE__Input__text-input"]'
    csl_verify_button = '//android.widget.Button'

    def input_referral_code(self):
        mobile_action = MobileCustomActionClass()

        mobile_action.tap(self.csl_mobile_app, 60)
        mobile_action.tap(self.new_user_verify_referral_code, 60)

        with open("..//data//referral_code.txt", "r") as file:
            mobile_referral_code = file.read().strip()

        mobile_action.type(self.referral_code_textbox, mobile_referral_code)
        mobile_action.tap(self.csl_verify_button)
