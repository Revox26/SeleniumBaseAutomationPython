from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromNewsAndEventsPage(BaseCase):
    news_and_events_menu = "//a[contains(.,'News and Events')]"

    def navigate_to_news_and_events_menu(self):
        self.click(self.news_and_events_menu)
