import random
from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestinationXGeneralNotificationPage(BaseCase):
    general_button = "//button[.='General']"
    recipient = "//select[@id='recipient']"
    external_link = "//label[contains(.,'External Link (optional)')]/..//input[@id='link']"
    notification_title = "(//input[@placeholder='Title for this notification'])[1]"
    notification_text = "(//input[@id='text'])[1]"
    send_push_notification_button = "(//button[contains(.,'Send Push Notification')])[1]"

    def send_general_notification(self):
        pass
