from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities


class DestinationxHomePage(AndroidCapabilities):
    enjoy_our_special_offers_on_selected_destination = '//android.widget.TextView[@text="Enjoy our special offers on selected destination."]'
    stay_updated_with_notifications_from_our_app = '//android.widget.TextView[@text="Stay updated with notifications from our app"]'
    going_on_in_your_area = '//android.widget.TextView[@text="Find out what"s going on in your area"]'
    sign_in_with_google = '//android.widget.TextView[@text="Sign in with Google"]'
    sign_in_with_apple = '//android.widget.TextView[@text="Sign in with Apple"]'
    create_an_account = '//android.widget.Button[@content-desc="Create an Account"]'
    login = '//android.widget.Button[@content-desc="Login"]'

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
        mobile_action.tap(self.login)

