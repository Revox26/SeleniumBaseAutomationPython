from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromContentBurger(BaseCase):
    contents_menu = "//a[contains(.,'Contents')]"

    def click_the_content_burger_menu(self):
        self.click(self.contents_menu)
