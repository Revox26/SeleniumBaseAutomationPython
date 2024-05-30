import base64
import subprocess
import sys
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities
from selenium.webdriver.support import expected_conditions as EC


class MobileCustomActionClass(AndroidCapabilities):
    _driver = None

    def __init__(self):
        super().__init__()
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        if not MobileCustomActionClass._driver:
            MobileCustomActionClass._driver = self.get_android_emulator_driver()
        return MobileCustomActionClass._driver

    def tap(self, value, timeOut=7):
        button = WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located((By.XPATH, value)))
        button.click()
        return button

    def double_tap(self, value, timeOut=7):
        for _ in range(2):
            button = self.tap(value, timeOut)
            return button

    def type(self, value, text, timeOut=7):
        text_box = WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located((By.XPATH, value)))
        text_box.send_keys(text)
        return text_box

    def swipe_down_until_element_is_visible(self, element_locator, max_swipe=5):
        for _ in range(max_swipe):
            try:
                # Check if the element is visible
                element = self.driver.find_element(by=AppiumBy.XPATH, value=element_locator).is_displayed()
                if element is True:
                    break  # Element found, no need to scroll
            except:
                # Get the device size
                size = self.driver.get_window_size()

                # Calculate swipe coordinates
                start_x = size['width'] // 2
                start_y = size['height'] // 2
                end_x = start_x
                end_y = size['height'] // 4
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=250)
                continue

    def swipe_element_right(self, element_locator):
        # Find the slider element by its ID or XPath
        slider = self.driver.find_element(by=AppiumBy.XPATH, value=element_locator)

        # Get the location and size of the slider
        slider_location = slider.location
        slider_size = slider.size

        # Calculate start and end points for swipe
        start_x = slider_location["x"] + slider_size["width"] * 0.2  # starting point
        end_x = slider_location["x"] + slider_size["width"] * 0.8  # ending point

        # Calculate the duration of the swipe
        duration_ms = 1000  # 1000 milliseconds = 1 second

        # Perform the swipe action by setting the value of the slider
        self.driver.swipe(start_x, slider_location["y"], end_x, slider_location["y"], duration_ms)

    def push_id_to_upload_in_android(self):
        file_paths = [
            ("..//director_id's/Philhealth-ID.jpg", "/storage/emulated/0/Download/Philhealth-ID.jpg"),
            ("..//director_id's/Pag-ibig.png", "/storage/emulated/0/Download/Pag-ibig.png")
        ]

        for local_path, android_path in file_paths:
            with open(local_path, 'rb') as file:
                data = file.read()
                encoded_data = base64.b64encode(data).decode('utf-8')
                self.driver.push_file(android_path, encoded_data)
