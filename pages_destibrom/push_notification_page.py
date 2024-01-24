from seleniumbase import BaseCase
import random
from utilities_destibrom.random_website_generator import RandomWebsiteGenerator
from configuration_files.config_reader import Readconfig


class DestibromPushNotificationPage(BaseCase):
    external_link_tab = "//button[.='External Links']"
    external_link_notification_title = "(//input[@name='title'])[1]"
    external_link_notification_text = "(//input[@name='text'])[1]"
    external_link = "(//input[@name='link'])[1]"
    external_link_send_push_notification_button = "(//button[.='Send Push Notification'])[1]"

    location_link_tab = "//button[.='Location']"
    location_resource = "//select[contains(@name,'resource')]"
    location_notification_title = "(//input[@name='title'])[2]"
    location_notification_text = "(//input[@name='text'])[2]"
    location_send_push_notification_button = "(//button[.='Send Push Notification'])[2]"

    category_tab = "//button[.='Category']"
    category_resource = "//select[@class='form-select']"
    category_notification_title = "(//input[@name='title'])[3]"
    category_notification_text = "(//input[@name='text'])[3]"
    category_send_push_notification_button = "(//button[.='Send Push Notification'])[3]"

    push_notification_sent_alert = "//h2[.='Push Notification Sent!']"
    push_notification_sent_ok = "//button[.='OK']"

    def navigate_to_push_notification_url(self):
        self.open(Readconfig.get_destibrom_v1_push_notif_url())

    def add_external_links_notification(self):
        website_generator = RandomWebsiteGenerator()
        website_url = website_generator.generate_random_website()
        random_category_title = ["New Update Available", "Special Offer", "Event Reminder", "Breaking News"]
        random_category_text = ["Check out the latest features!", "Limited time offer just for you.", "Don't forget our upcoming event.", "Stay tuned for important updates."]
        random_title = random.choice(random_category_title)
        random_text = random.choice(random_category_text)

        self.click(self.external_link_tab)
        self.type(self.external_link_notification_title, random_title)
        self.type(self.external_link_notification_text, random_text)
        self.type(self.external_link, website_url)
        self.click(self.external_link_send_push_notification_button)
        self.assert_element(self.push_notification_sent_alert)
        self.click(self.push_notification_sent_ok)

    def add_location_notification(self):
        random_category_title = ["New Update Available", "Special Offer", "Event Reminder", "Breaking News"]
        random_category_text = ["Check out the latest features!", "Limited time offer just for you.", "Don't forget our upcoming event.", "Stay tuned for important updates."]
        random_title = random.choice(random_category_title)
        random_text = random.choice(random_category_text)

        self.click(self.location_link_tab)
        options = self.get_select_options(self.location_resource)
        random_option = random.choice(options)
        self.select_option_by_text(self.location_resource, random_option)
        self.type(self.location_notification_title, random_title)
        self.type(self.location_notification_text, random_text)
        self.click(self.location_send_push_notification_button)
        self.assert_element(self.push_notification_sent_alert)
        self.click(self.push_notification_sent_ok)

    def add_category_notification(self):
        random_category_title = ["New Update Available", "Special Offer", "Event Reminder", "Breaking News"]
        random_category_text = ["Check out the latest features!", "Limited time offer just for you.", "Don't forget our upcoming event.", "Stay tuned for important updates."]
        random_title = random.choice(random_category_title)
        random_text = random.choice(random_category_text)

        self.click(self.category_tab)
        self.click(self.category_resource)
        arrow_down_count = random.randint(1, 6)
        for _ in range(arrow_down_count):
            self.press_down_arrow(self.category_resource + "\n")
        self.type(self.category_notification_title, random_title)
        self.type(self.category_notification_text, random_text)
        self.click(self.category_send_push_notification_button)
        self.assert_element(self.push_notification_sent_alert)
        self.click(self.push_notification_sent_ok)
