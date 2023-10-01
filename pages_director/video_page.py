from seleniumbase import BaseCase


class DirectorVideoPage(BaseCase):
    click_to_continue = "//button[@id='continue-button']"
    i_accept = "//span[contains(@class,'checkmark')]"
    proceed = "//button[@id='btn-proceed']"

    def skip_the_video(self):
        self.wait_for_element_clickable(self.click_to_continue, timeout=500)
        self.click(self.click_to_continue)
        self.sleep(1)
        self.click(self.i_accept)
        self.click(self.proceed)

