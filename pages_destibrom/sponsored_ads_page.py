from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromSponsoredAdsPage(BaseCase):
    sponsored_ads_menu = "//a[contains(.,'Sponsored Ads')]"

    def navigate_to_sponsored_ads_menu(self):
        self.click(self.sponsored_ads_menu)
