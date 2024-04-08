from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker

from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.pages_csl_mobile.android_capabilities import AndroidCapabilities


class CslMobilePersonalDetailsPage:
    select_title_xpath = '//android.widget.EditText[@resource-id="text_input" and @text="Select a title"]'
    select_mr_title = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Mr."]'
    select_birth_date_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Birth Date"]'
    select_specific_birth_day_xpath = '//android.view.View[@text="10"]'
    date_ok = '//android.widget.Button[@text="OK"]'
    mobile_number_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Mobile Number"]'
    occupation_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Occupation"]'
    professional_interest_xpath = '//android.widget.TextView[@resource-id="iconIcon" and @text=""]'
    select_transport_xpath = '//android.widget.TextView[@resource-id="listItemTitle" and @text="Transport"]'
    close_professional_interest_xpath = '(//android.widget.TextView[@resource-id="iconIcon"])[1]'
    address_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Address"]'
    town_or_city_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Town/City"]'
    province_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Province"]'
    postal_code_xpath = '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="Postal Code"]'
    same_as_present_address = '//android.widget.TextView[@text="Same as permanent address"]'
    continue_button_for_personal_details_xpath = '(//android.widget.TextView[@text="Continue"])[2]'

    def csl_mobile_personal_details(self):
        fake = Faker()
        mobile_action = MobileCustomActionClass()

        mobile_action.tap(self.select_title_xpath, 60)
        mobile_action.tap(self.select_mr_title)

        mobile_action.swipe_down_until_element_is_visible(self.select_birth_date_xpath)
        mobile_action.tap(self.select_birth_date_xpath)
        mobile_action.tap(self.select_specific_birth_day_xpath)
        mobile_action.tap(self.date_ok)

        mobile_action.swipe_down_until_element_is_visible(self.mobile_number_xpath)
        mobile_action.type(self.mobile_number_xpath, '9' + fake.random_int(min=100000000, max=999999999).__str__())

        mobile_action.swipe_down_until_element_is_visible(self.occupation_xpath)
        mobile_action.type(self.occupation_xpath, fake.job())

        mobile_action.swipe_down_until_element_is_visible(self.professional_interest_xpath)
        mobile_action.tap(self.professional_interest_xpath)
        mobile_action.tap(self.select_transport_xpath)
        mobile_action.tap(self.close_professional_interest_xpath)

        mobile_action.swipe_down_until_element_is_visible(self.address_xpath)
        mobile_action.type(self.address_xpath, fake.address())

        mobile_action.swipe_down_until_element_is_visible(self.town_or_city_xpath)
        mobile_action.type(self.town_or_city_xpath, fake.city())

        mobile_action.swipe_down_until_element_is_visible(self.province_xpath)
        mobile_action.type(self.province_xpath, fake.state())

        mobile_action.swipe_down_until_element_is_visible(self.postal_code_xpath)
        mobile_action.type(self.postal_code_xpath, "4120")

        mobile_action.swipe_down_until_element_is_visible(self.same_as_present_address)
        mobile_action.tap(self.same_as_present_address)

        mobile_action.swipe_down_until_element_is_visible(self.continue_button_for_personal_details_xpath)
        mobile_action.tap(self.continue_button_for_personal_details_xpath)
