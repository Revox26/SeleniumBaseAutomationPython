import time
import pyautogui
import random
import pytest
from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class PinMarkerMap(BaseCase):
    location = "path.RIFvHW-maps-pin-view-background"

    @pytest.mark.run(repeats=3)
    def test_drag_pin_marker(self):
        self.open("https://developers.google.com/maps/documentation/javascript/examples/advanced-markers-draggable")
        self.switch_to_frame("iframe")
        self.assert_element(self.location)
        time.sleep(1)
        x = 700
        y = 466
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        new_x = random.randint(500, 1000)
        new_y = random.randint(300, 800)
        pyautogui.moveTo(new_x, new_y, duration=0.5)
        pyautogui.mouseUp()
        time.sleep(2)
