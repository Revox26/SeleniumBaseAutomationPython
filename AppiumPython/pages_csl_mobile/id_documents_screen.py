from AppiumPython.actions.mobile_actions import MobileCustomActionClass
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities


class CslMobileIdDocumentsScreen(AndroidCapabilities):
    select_an_id = '//android.widget.EditText[@resource-id="text_input" and @text="Select an item..."]'
    select_pag_ibig_id_mobile = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Pag Ibig ID"]'
    select_philhealth_id_mobile = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="PhilHealth ID"]'
    upload_id_button_mobile = '//android.widget.TextView[@text="Upload ID"]'
    browse_id = '//android.widget.Button[@resource-id="android:id/button2" and @text="BROWSE"]'
    upload_id_1 = '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'
    upload_id_2 = '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[2]'
    upload_and_finish_button = '(//android.widget.TextView[@text="Upload & Finish"])[2]'
    view_account = '//android.widget.TextView[@text="View Account"]'

    def csl_mobile_upload_id(self):
        mobile_action = MobileCustomActionClass()
        mobile_action.push_id_to_upload_in_android()

        mobile_action.tap(self.select_an_id)
        mobile_action.tap(self.select_pag_ibig_id_mobile)
        mobile_action.tap(self.upload_id_button_mobile)
        mobile_action.tap(self.browse_id)
        mobile_action.tap(self.upload_id_1)

        mobile_action.swipe_down_until_element_is_visible(self.select_an_id)

        mobile_action.tap(self.select_an_id)
        mobile_action.tap(self.select_philhealth_id_mobile)
        mobile_action.swipe_down_until_element_is_visible(self.upload_id_button_mobile)
        mobile_action.tap(self.upload_id_button_mobile)
        mobile_action.tap(self.browse_id)
        mobile_action.tap(self.upload_id_2)

        mobile_action.swipe_down_until_element_is_visible(self.upload_and_finish_button)
        mobile_action.tap(self.upload_and_finish_button)

        mobile_action.tap(self.view_account)
