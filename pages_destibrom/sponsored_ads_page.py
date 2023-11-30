from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig
from utilities.random_website_generator import RandomWebsiteGenerator


class DestibromSponsoredAdsPage(BaseCase):
    sponsored_ads_menu = "//a[contains(.,'Sponsored Ads')]"
    add_sponsored_ads_button = "//a[contains(.,'Add Sponsored Ad')]"
    sponsored_ads_content_link = "//input[@id='content_link']"
    sponsored_ads_button = "//button[.='Save']"

    def navigate_to_sponsored_ads_menu(self):
        self.click(self.sponsored_ads_menu)

    def add_new_for_sponsored_ads(self):
        website_generator = RandomWebsiteGenerator()
        website_url = website_generator.generate_random_website()

        self.click(self.add_sponsored_ads_button)
        self.type(self.sponsored_ads_content_link, website_url)
        # self.click(self.sponsored_ads_button)
