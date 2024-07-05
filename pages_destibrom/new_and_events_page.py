from seleniumbase import BaseCase
from utilities_destibrom.random_image_generator import ImageHandler
from utilities_destibrom.random_website_generator import RandomWebsiteGenerator


class DestibromNewsAndEventsPage(BaseCase):
    news_and_events_menu = "//a[contains(.,'News & Events')]"
    add_news_and_events_button = "//a[contains(.,'Add News and Event')]"
    news_and_events_content_link = "//input[@id='content_link']"
    news_and_events_content_image = "//input[@class='filepond--browser']"
    news_and_events_save_button = "//button[.='Save']"
    news_and_events_save_successfully_label = "//h2[.='News & Event Saved Successfully!']"
    news_and_events_successfully_ok = "//h2[.='News & Event Saved Successfully!']/..//button[.='OK']"
    _remove_hidden_class = "document.getElementById('filepond--browser-zdukl0c2q').classList.remove('filepond--browser')"

    def navigate_to_news_and_events_menu(self):
        self.click(self.news_and_events_menu)

    def add_new_for_news_and_events(self):
        api_call = "https://picsum.photos/200"
        save_path = "..//random_images"
        image_handler = ImageHandler(api_call, save_path)
        image_handler.download_and_resize_image()

        website_generator = RandomWebsiteGenerator()
        website_url = website_generator.generate_random_website()

        self.click(self.add_news_and_events_button)
        self.add_js_code(self._remove_hidden_class)
        self.choose_file(self.news_and_events_content_image, "..//random_images/resized_image.png")
        self.type(self.news_and_events_content_link, website_url)
        self.sleep(1)
        self.click(self.news_and_events_save_button)
        self.assert_element(self.news_and_events_save_successfully_label)
        self.click(self.news_and_events_successfully_ok)
