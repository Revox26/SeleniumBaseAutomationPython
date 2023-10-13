from seleniumbase import BaseCase
import pyautogui
import time


class DirectorVideoPage(BaseCase):
    click_to_continue = "//button[@id='continue-button']"
    i_accept = "//span[contains(@class,'checkmark')]"
    proceed = "//button[@id='btn-proceed']"

    def skip_the_video(self):
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        pyautogui.click(center_x, center_y)
        time.sleep(1)
        self.scroll_into_view(self.click_to_continue)
        pyautogui.press('num9')
        num_presses = 7
        [pyautogui.press('right') for _ in range(num_presses)]

        self.wait_for_element_clickable(self.click_to_continue, timeout=500)
        self.click(self.click_to_continue)
        self.sleep(1)
        self.click(self.i_accept)
        self.click(self.proceed)
