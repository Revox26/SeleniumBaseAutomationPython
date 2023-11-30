from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig
from utilities.random_website_generator import RandomWebsiteGenerator


class DestibromNewsAndEventsPage(BaseCase):
    news_and_events_menu = "//a[contains(.,'News and Events')]"
    add_news_and_events_button = "//a[contains(.,'Add News and Event')]"
    news_and_events_content_link = "//input[@id='content_link']"
    news_and_events_save_button = "//button[.='Save']"

    def navigate_to_news_and_events_menu(self):
        self.click(self.news_and_events_menu)

    def add_new_for_news_and_events(self):
        website_generator = RandomWebsiteGenerator()
        website_url = website_generator.generate_random_website()

        self.click(self.add_news_and_events_button)
        self.type(self.news_and_events_content_link, website_url)
        # self.click(self.news_and_events_save_button)


