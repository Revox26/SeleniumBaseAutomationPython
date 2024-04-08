from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.pages_csl_mobile.android_capabilities import AndroidCapabilities
from selenium.webdriver.support import expected_conditions as EC


class CslMobileWelcomeVideoPage(AndroidCapabilities):
    skip_video_xpath = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]'
    continue_button_xpath = '(//android.widget.TextView[@text="Continue"])[2]'
    i_have_read_and_accept_consent_form = '//android.widget.TextView[@text="I have read and accept the data privacy notice and consent form."]'
    accept_button_for_consent_form = '(//android.widget.TextView[@text="Accept"])[2]'

    def skip_csl_app_video(self):
        mobile_action = MobileCustomActionClass()

        mobile_action.tap(self.continue_button_xpath, 500)
        mobile_action.tap(self.i_have_read_and_accept_consent_form)
        mobile_action.tap(self.accept_button_for_consent_form)
