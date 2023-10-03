from seleniumbase import BaseCase


class SupplierLandOfferingsPage(BaseCase):
    _offerings = "//a[contains(.,'Offerings')]"
    _offerings_client = "//input[@placeholder='Please select client']"
    _offerings_industry = "//input[@placeholder='Please select industry']"
    _offerings_search_button = "//button[contains(.,'Search')]"

    def navigate_to_offerings(self):
        self.click(self._offerings)

    def search_company_in_offerings(self):
        with open("..//configuration_files//intermediary.txt", "r") as file:
            _get_intermediary = file.read().strip()

        with open("..//configuration_files//industry.txt", "r") as file:
            _get_industry = file.read().strip()

        self.type(self._offerings_client, _get_intermediary + "\n")
        self.type(self._offerings_industry, _get_industry + "\n")
        self.click(self._offerings_search_button)

        self.sleep(60)
