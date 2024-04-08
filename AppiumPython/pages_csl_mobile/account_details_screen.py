import random

from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities
from configuration_files.config_reader import Readconfig


class CslMobileAccountDetailsScreen(AndroidCapabilities):
    csl_mobile_personal_details_label = '//android.widget.TextView[@text="Account Details"]'
    csl_mobile_email_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Email"]'
    csl_mobile_password_xpath = '(//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Password"])[1]'
    csl_mobile_confirm_password_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Password"]'

    csl_mobile_authentication_question_1_xpath = '//android.widget.EditText[@text="Choose a question"]'
    last_characters_of_telephone_number_xpath = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Last 3 characters of telephone number"]'
    authentication_1_textbox_xpath = '//android.widget.EditText[contains(@resource-id, "RNE__Input__text-input") and @text=""]'

    csl_mobile_authentication_question_2_xpath = '//android.widget.EditText[@text="Choose a question"]'
    last_3_characters_of_passport_number_xpath = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Last 3 characters of Passport number"]'
    authentication_2_textbox_xpath = '//android.widget.EditText[contains(@resource-id, "RNE__Input__text-input") and @text=""]'

    csl_mobile_authentication_question_3_xpath = '//android.widget.EditText[@text="Choose a question"]'
    first_3_characters_of_eye_colour_xpath = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="1st 3 characters of Eye Colour"]'
    authentication_3_textbox_xpath = '//android.widget.EditText[contains(@resource-id, "RNE__Input__text-input") and @text=""]'

    create_account_button_xpath = '//android.widget.TextView[@text="Create Account"]'
    yes_continue_never_been_a_director = '//android.widget.TextView[@text="YES"]'

    def csl_mobile_account_details(self):
        mobile_action = MobileCustomActionClass()

        with open("..//data//first_name.txt", "r") as file:
            email = file.read().strip()
            random_number = random.randint(100, 999)
            result = str(random_number) + "@automation.com"
        with open("..//data//email.txt", "w") as file:
            file.write(email + result)

        mobile_action.type(self.csl_mobile_email_xpath, email + result)
        mobile_action.type(self.csl_mobile_password_xpath, Readconfig.get_director_password())
        mobile_action.type(self.csl_mobile_confirm_password_xpath, Readconfig.get_director_password())

        # AUTHENTICATION 1
        mobile_action.swipe_down_until_element_is_visible(self.authentication_1_textbox_xpath)
        mobile_action.tap(self.csl_mobile_authentication_question_1_xpath)
        mobile_action.tap(self.last_characters_of_telephone_number_xpath)
        mobile_action.type(self.authentication_1_textbox_xpath, "123")

        # AUTHENTICATION 2
        mobile_action.swipe_down_until_element_is_visible(self.authentication_2_textbox_xpath)
        mobile_action.tap(self.csl_mobile_authentication_question_2_xpath)
        mobile_action.tap(self.last_3_characters_of_passport_number_xpath)
        mobile_action.type(self.authentication_2_textbox_xpath, "123")

        # AUTHENTICATION 3
        mobile_action.swipe_down_until_element_is_visible(self.authentication_3_textbox_xpath)
        mobile_action.tap(self.csl_mobile_authentication_question_3_xpath)
        mobile_action.tap(self.first_3_characters_of_eye_colour_xpath)
        mobile_action.type(self.authentication_3_textbox_xpath, "abc")

        mobile_action.swipe_down_until_element_is_visible(self.create_account_button_xpath)
        mobile_action.tap(self.create_account_button_xpath)

        mobile_action.tap(self.yes_continue_never_been_a_director, 60)
