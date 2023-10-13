from seleniumbase import BaseCase


class SupplierLandOfferingsPage(BaseCase):
    _offerings = "//a[contains(.,'Offerings')]"
    _offerings_client = "//input[@placeholder='Please select client']"
    _offerings_industry = "//input[@placeholder='Please select industry']"
    _offerings_search_button = "//button[contains(.,'Search')]"

    def navigate_to_offerings(self):
        self.click(self._offerings)

    def search_company_in_offerings(self):
        arrow_down = self.press_down_arrow(self._offerings_industry)

        with open("..//data//intermediary.txt", "r") as file:
            _get_intermediary = file.read().strip()

        with open("..//data//industry.txt", "r") as file:
            _get_industry = file.read().strip()

        self.type(self._offerings_client, _get_intermediary + "\n")
        self.type(self._offerings_industry, _get_industry)
        self.press_keys(self._offerings_industry, "\ue015\ue007")
        self.click(self._offerings_search_button)

        self.sleep(60)
