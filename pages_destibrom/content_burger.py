from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromContentBurger(BaseCase):
    content_burger_menu = "//a[@aria-controls='contentDropdown']"

    def click_the_content_burger_menu(self):
        self.click(self.content_burger_menu)
