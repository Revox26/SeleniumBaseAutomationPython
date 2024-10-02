import base64
import subprocess
import sys
import time

from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import BaseCase

from AppiumPython.device_capabilities.adb_devices import save_devices_to_file, start_appium_server
from test_runner.app import QAApp

BaseCase.main(__name__, __file__)
from AppiumPython.device_capabilities.android_capabilities import AndroidCapabilities
from selenium.webdriver.support import expected_conditions as EC


class MobileCustomActionClass(AndroidCapabilities, QAApp):
    _driver = None

    def __init__(self):
        super().__init__()
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        start_appium_server()
        time.sleep(5)
        save_devices_to_file("adb_devices.txt")
        with open("..//data//adb_devices.txt", "r") as file:
            selected_device = file.read().strip()
            print(selected_device)

        if not MobileCustomActionClass._driver:
            if selected_device.startswith("emulator-5554"):
                MobileCustomActionClass._driver = self.get_android_emulator_driver()
            elif selected_device == "--oppo":
                MobileCustomActionClass._driver = self.get_oppo_test_phone_driver()
            elif selected_device == "--vivo":
                MobileCustomActionClass._driver = self.get_vivo_test_phone_driver()
            else:
                print("Device argument not provided or not recognized.")

        return MobileCustomActionClass._driver

        # with open("..//data//mobile_device_type.txt", "r") as file:
        #     selected_device = file.read().strip()
        #
        # if not MobileCustomActionClass._driver:
        #     if selected_device == "--emulator":
        #         MobileCustomActionClass._driver = self.get_android_emulator_driver()
        #     elif selected_device == "--oppo":
        #         MobileCustomActionClass._driver = self.get_oppo_test_phone_driver()
        #     elif selected_device == "--vivo":
        #         MobileCustomActionClass._driver = self.get_vivo_test_phone_driver()
        #     else:
        #         print("Device argument not provided or not recognized.")
        #
        # return MobileCustomActionClass._driver

    def tap(self, value, timeOut=7):
        button = WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located((By.XPATH, value)))
        button.click()
        return button

    def assert_element(self, value, timeOut=7):
        try:
            element = WebDriverWait(self.driver, timeOut).until(
                EC.visibility_of_element_located((By.XPATH, value))
            )
            return element
        except TimeoutException:
            print(f"Element located by {value} not found within {timeOut} seconds.")
            return None  # or raise an exception, depending on your needs

    def double_tap(self, value, timeOut=7):
        for _ in range(2):
            button = self.tap(value, timeOut)
            return button

    def type_text(self, value, text, timeOut=7):
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
