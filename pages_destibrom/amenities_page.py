from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromAmenitiesPage(BaseCase):
    amenities_menu = "//a[contains(.,'Amenities')]"

    def navigate_to_amenities_menu(self):
        self.click(self.amenities_menu)
