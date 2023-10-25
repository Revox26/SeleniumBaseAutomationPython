import time

from seleniumbase import BaseCase


class SupplierLandOfferingsPage(BaseCase):
    _offerings = "//a[contains(.,'Offerings')]"
    _offerings_client = "//input[@placeholder='Please select client']"
    _offerings_industry = "//input[@placeholder='Please select industry']"
    _offerings_search_button = "//button[contains(.,'Search')]"
    _offerings_check_all = "//label[@for='offer_check_all']"
    disabled_cancel_all = "//button[@disabled='disabled']"
    enabled_cancel_all = "//button[starts-with(text(),'Cancel All')]"

    def navigate_to_offerings(self):
        self.click(self._offerings)

    def search_company_in_offerings(self):
        with open("..//data//intermediary.txt", "r") as file:
            _get_intermediary = file.read().strip()

        with open("..//data//industry.txt", "r") as file:
            _get_industry = file.read().strip()

        self.type(self._offerings_client, _get_intermediary + "\n", timeout=60)
        self.type(self._offerings_industry, _get_industry)
        self.press_keys(self._offerings_industry, "\ue015\ue007")
        self.click(self._offerings_search_button)
        self.click(self._offerings_check_all)

        # handle the auto close once assigned priority
        time.sleep(35)



