from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromLocationPage(BaseCase):
    location_menu = "//a[text()='Locations']"
    add_location_button = "//a[contains(.,'Add Locations')]"
    name_of_location = "//input[@id='name']"
    location_address = "//input[@id='address']"
    search_address_button = "//button[@id='address-search']"
    about_this_location = "//input[@id='about']"
    contact_number = "//input[@id='contact_number']"
    location_email = "//input[@id='email']"
    location_website = "//input[@id='website']"
    location_category = "//input[@aria-labelledby='category_id-ts-label']"

    upload_custom_icon = "//input[@id='filepond--browser-nhv7chwgf']"

    def navigate_to_locations_menu(self):
        self.click(self.location_menu)
