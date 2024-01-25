from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig
from utilities_destibrom.random_categories_name import generate_random_categories_name
from utilities_destibrom.random_icons_lists import generate_random_icon_list
from utilities_destibrom.random_image_generator import ImageHandler


class DestibromCategoriesPage(BaseCase):
    categories_menu = "//a[.='Categories']"
    add_category_button = "//a[.='Add Category']"
    edit_category = "//a[contains(.,'Edit')]"
    category_name = "//input[contains(@name,'name')]"
    upload_icon_monochrome = "(//input[@class='filepond--browser'])[1]"
    upload_icon_coloured = "(//input[@class='filepond--browser'])[2]"
    icon_side_bar = "//input[@id='icon_sidebar']"
    save_category_button = "//button[@type='submit']"
    _remove_icon_monochrome_hidden_class = "document.getElementById('filepond--browser-kp74m52bf').classList.remove('filepond--browser')"
    _remove_icon_coloured_hidden_class = "document.getElementById('filepond--browser-7m61mxfta').classList.remove('filepond--browser')"
    category_saved_successfully_alert = "//h2[.='Category Saved Successfully!']"
    category_saved_successfully_ok_button = "//h2[.='Category Saved Successfully!']/..//button[.='OK']"

    def navigate_to_categories_menu(self):
        self.click(self.categories_menu)

    def add_new_category(self):
        api_call = "https://picsum.photos/200"
        save_path = "..//random_images"
        image_handler = ImageHandler(api_call, save_path)
        image_handler.download_and_resize_icon()

        random_icons = generate_random_icon_list()
        random_categories = generate_random_categories_name()
        self.click(self.add_category_button)
        self.add_js_code(self._remove_icon_monochrome_hidden_class)
        self.add_js_code(self._remove_icon_coloured_hidden_class)
        self.type(self.category_name, random_categories)


        self.choose_file(self.upload_icon_monochrome, "..//random_images/resized_icons.jpg")
        self.choose_file(self.upload_icon_coloured, "..//random_images/resized_icons2.jpg")

        self.type(self.icon_side_bar, random_icons)
        self.click(self.save_category_button)
        self.assert_element(self.category_saved_successfully_alert)
        self.click(self.category_saved_successfully_ok_button)
