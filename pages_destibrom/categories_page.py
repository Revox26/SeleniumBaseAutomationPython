from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromCategoriesPage(BaseCase):
    categories_menu = "//a[.='Categories']"
    add_category_button = "//a[.='Add Category']"
    edit_category = "//a[contains(.,'Edit')]"
    category_name = "//input[contains(@name,'name')]"
    upload_icon_monochrome = "//input[@id='filepond--browser-g0w5u6q0v']"
    upload_icon_coloured = "//input[@aria-controls='filepond--assistant-rkawwcsnd']"
    icon_side_bar = "//input[@id='icon_sidebar']"
    save_category_button = "//button[@type='submit']"

    def navigate_to_categories_menu(self):
        self.click(self.categories_menu)
