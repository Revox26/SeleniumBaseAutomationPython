from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig
from utilities_destibrom.random_amenities_name import generate_random_amenities
from utilities_destibrom.random_icons_lists import generate_random_icon_list


class DestibromAmenitiesPage(BaseCase):
    amenities_menu = "//a[contains(.,'Amenities')]"
    add_amenity_button = "//a[@class='btn btn-destibrom']"
    amenity_name = "//input[@id='name']"
    amenity_icon = "//input[@id='icon']"
    amenity_save_button = "//button[@type='submit']"
    amenity_saved_successfully_label = "//h2[.='Amenity Saved Successfully!']"
    amenity_saved_successfully_label_okay = "//h2[.='Amenity Saved Successfully!']/..//button[.='OK']"

    def navigate_to_amenities_menu(self):
        self.click(self.amenities_menu)

    def add_new_amenity(self):
        random_amenities = generate_random_amenities()
        random_icons = generate_random_icon_list()
        self.click(self.add_amenity_button)
        self.type(self.amenity_name, random_amenities)
        self.type(self.amenity_icon, random_icons)
        self.click(self.amenity_save_button)
        self.assert_element(self.amenity_saved_successfully_label)
        self.click(self.amenity_saved_successfully_label_okay)
