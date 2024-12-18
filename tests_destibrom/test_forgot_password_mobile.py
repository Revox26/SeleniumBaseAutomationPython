import pytest

from AppiumPython.pages_destination_x.home_screen import DestinationxHomePage
from AppiumPython.pages_destination_x.login_screen import DestinationxLoginPage
from pages_destibrom.login_page import DestiBromLoginPage


class DestinationxForgotPasswordMobile(
    DestiBromLoginPage,
    DestinationxLoginPage,
    DestinationxHomePage

):

    @pytest.mark.run(order=1)
    def test_forgot_password_non_existing_mobile(self):
        self.navigate_to_login()
        self.navigate_to_forgot_password_non_existing_account()

    @pytest.mark.run(order=2)
    def test_forgot_password_existing_mobile(self):
        self.navigate_to_login()
        self.navigate_to_forgot_password_existing_account()
