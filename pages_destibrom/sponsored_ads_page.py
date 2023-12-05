from seleniumbase import BaseCase
from utilities_destibrom.random_image_generator import ImageHandler
from utilities_destibrom.random_website_generator import RandomWebsiteGenerator


class DestibromSponsoredAdsPage(BaseCase):
    sponsored_ads_menu = "//a[contains(.,'Sponsored Ads')]"
    add_sponsored_ads_button = "//a[contains(.,'Add Sponsored Ad')]"
    sponsored_ads_content_link = "//input[@id='content_link']"
    sponsored_ads_upload_content_image = "//input[@class='filepond--browser']"
    sponsored_ads_button = "//button[.='Save']"
    sponsored_ads_save_successfully_label = "//h2[.='Sponsored Ad Saved Successfully!']"
    sponsored_ads_successfully_ok = "//h2[.='Sponsored Ad Saved Successfully!']/..//button[.='OK']"
    remove_hidden_class = "document.getElementById('filepond--browser-zdukl0c2q').classList.remove('filepond--browser')"

    def navigate_to_sponsored_ads_menu(self):
        self.click(self.sponsored_ads_menu)

    def add_new_for_sponsored_ads(self):
        api_call = "https://picsum.photos/200"
        save_path = "..//random_images"
        image_handler = ImageHandler(api_call, save_path)
        image_handler.download_and_resize_image()

        website_generator = RandomWebsiteGenerator()
        website_url = website_generator.generate_random_website()

        self.click(self.add_sponsored_ads_button)
        self.add_js_code(self.remove_hidden_class)
        self.choose_file(self.sponsored_ads_upload_content_image, "..//random_images/resized_image.png")
        self.type(self.sponsored_ads_content_link, website_url)
        self.sleep(1)
        self.click(self.sponsored_ads_button)
        self.assert_element(self.sponsored_ads_save_successfully_label)
        self.click(self.sponsored_ads_successfully_ok)
