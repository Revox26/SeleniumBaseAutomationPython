import random

from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig
from utilities_destibrom.random_website_generator import RandomWebsiteGenerator


class DestinationXExternalLinkNotificationPage(BaseCase):
    external_link_button = "//button[.='External Links']"
    external_link = "//label[.='External Link']/..//input[@id='link']"
    notification_title = "(//input[@placeholder='Title for this notification'])[2]"
    notification_text = "(//input[contains(@value,'Tap here for details')])[2]"
    send_push_notification_button = "(//button[contains(.,'Send Push Notification')])[2]"
    push_notification_sent_alert = "//h2[.='Push Notification Sent!']"

    def send_external_link_notification(self):
        website_generator = RandomWebsiteGenerator()
        notification_generator = RandomWebsiteGenerator.generate_random_notification_title()
        text_generator = RandomWebsiteGenerator.generate_random_notification_text()
        website_url = website_generator.generate_random_website()

        self.click(self.external_link_button)
        self.type(self.external_link, website_url)
        self.type(self.notification_title, notification_generator)
        self.type(self.notification_text, text_generator)
        self.click(self.send_push_notification_button)
        self.assert_element(self.push_notification_sent_alert)
