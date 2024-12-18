from selenium.common import NoSuchElementException
from seleniumbase import BaseCase
from configuration_files.business_centre_config_reader import ReadBusinessCentreConfig


class BusinessCentreDashboardnPage(BaseCase):
    add_shortcut_button = "//span[.='Add Shortcut']"
    add_shortcut_name = "//label[.='Name ']//input[@type='text']"
    add_shortcut_url = "//label[.='URL ']//input[@type='text']"
    save_shortcut_button = "//button[.='Add Shortcut']"
    favourites_icon = "//div[@class='relative flex h-[82px] items-center justify-center rounded-xl bg-white hover:bg-gray-200 group-hover:bg-gray-200']"
    delete_icon = "//span[@class='material-symbols-outlined text-base']"
    continue_delete_icon = "//button[.='Continue']"

    def add_shortcut_favourites(self):
        with open("..//data//business_centre_fav_website.txt", "r") as file:
            favourites_sites = file.readlines()

        for index, url in enumerate(favourites_sites):
            url = url.strip()
            shortcut_name = f"Shortcut {index + 1}"

            self.slow_scroll_to_element(self.add_shortcut_button)
            self.click(self.add_shortcut_button)

            self.type(self.add_shortcut_name, shortcut_name)
            self.type(self.add_shortcut_url, url)

            self.click(self.save_shortcut_button)

    def delete_shortcut(self):
        # self.hover(self.favourites_icon)
        # self.click(self.delete_icon)
        # self.click(self.continue_delete_icon)

        while True:
            try:
                # Check if the favourites icon (i.e., the delete button) is still visible
                self.wait_for_element_visible(self.favourites_icon, timeout=5)  # Wait for the element to be visible
                self.hover_and_click(self.favourites_icon, self.delete_icon)
                self.click(self.continue_delete_icon)
            except Exception:
                # If the element is not found, we break the loop (i.e., no more shortcuts to delete)
                print("No more favourites to delete.")
                break
