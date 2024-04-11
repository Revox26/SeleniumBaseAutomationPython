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

    def initialize_driver(self):
        if not MobileCustomActionClass._driver:
            MobileCustomActionClass._driver = self.get_android_emulator_driver()
        return MobileCustomActionClass._driver

    def tap(self, value, timeOut=7):
        driver = self.initialize_driver()
        button = WebDriverWait(driver, timeOut).until(EC.visibility_of_element_located((By.XPATH, value)))
        button.click()
        return button

    def type(self, value, text, timeOut=7):
        driver = self.initialize_driver()
        WebDriverWait(driver, timeOut).until(EC.visibility_of_element_located((By.XPATH, value)))
        text_box = driver.find_element(by=AppiumBy.XPATH, value=value)
        text_box.send_keys(text)
        return text_box

    def swipe_down_until_element_is_visible(self, element_locator, max_swipe=5):
        driver = self.initialize_driver()
        for _ in range(max_swipe):
            try:
                # Check if the element is visible
                element = driver.find_element(by=AppiumBy.XPATH, value=element_locator).is_displayed()
                if element is True:
                    break  # Element found, no need to scroll
            except:
                # Get the device size
                size = driver.get_window_size()

                # Calculate swipe coordinates
                start_x = size['width'] // 2
                start_y = size['height'] // 2
                end_x = start_x
                end_y = size['height'] // 4
                driver.swipe(start_x, start_y, end_x, end_y, duration=300)
                continue
            time.sleep(1)

    def push_id_to_upload_in_android(self):
        driver = self.initialize_driver()
        file_paths = [
            ("..//director_id's/Philhealth-ID.jpg", "/storage/emulated/0/Download/Philhealth-ID.jpg"),
            ("..//director_id's/Pag-ibig.png", "/storage/emulated/0/Download/Pag-ibig.png")
        ]

        for local_path, android_path in file_paths:
            with open(local_path, 'rb') as file:
                data = file.read()
                encoded_data = base64.b64encode(data).decode('utf-8')
                driver.push_file(android_path, encoded_data)
