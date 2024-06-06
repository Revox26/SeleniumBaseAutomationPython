import subprocess
import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions


class AndroidCapabilities:
    url = 'http://localhost:4724'

    def get_android_emulator_capabilities(self) -> Dict[str, Any]:
        return {
            'platformName': 'Android',
            'platformVersion': '14.0',
            'deviceName': 'Pixel_3a_API_34_extension_level_7_x86_64',
            'language': 'en',
            'noReset': True,
            'skipDeviceInitialization': True,
            'skipServerInstallation': True,
            'waitForIdleTimeout': 0,
            'networkSpeed': 'full',
            'automationName': 'UiAutomator2'
        }

    def get_vivo_test_phone_capabilities(self) -> Dict[str, Any]:
        return {
            'platformName': 'Android',
            'platformVersion': '12.0',
            'deviceName': 'vivo V2204',
            'language': 'en',
            'noReset': True,
            'skipDeviceInitialization': True,
            'skipServerInstallation': True,
            'waitForIdleTimeout': 0,
            'networkSpeed': 'full',
            'automationName': 'UiAutomator2',
            'autoGrantPermissions': True
        }

    def get_oppo_test_phone_capabilities(self) -> Dict[str, Any]:
        return {
            'platformName': 'Android',
            'platformVersion': '13.0',
            'deviceName': 'OPPO CPH2473',
            'noReset': True,
            'skipDeviceInitialization': True,
            'skipServerInstallation': True,
            'udid': 'b07db607',
            'waitForIdleTimeout': 0,
            'networkSpeed': 'full',
            'automationName': 'UiAutomator2',
            'autoGrantPermissions': True,
            'newCommandTimeout': 300
        }

    def get_android_emulator_driver(self):
        return webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.get_android_emulator_capabilities()))

    def get_oppo_test_phone_driver(self):
        return webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.get_oppo_test_phone_capabilities()))

    def get_vivo_test_phone_driver(self):
        return webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.get_vivo_test_phone_capabilities()))
