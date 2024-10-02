import pytest

from AppiumPython.pages_destination_x.create_an_account_screen import DestinationxCreateAnAccountPage
from AppiumPython.pages_destination_x.login_screen import DestinationxLoginPage
from pages_destibrom.login_page import DestiBromLoginPage


class DestinationxCreateAnAccountMobile(
    DestinationxLoginPage,
    DestinationxCreateAnAccountPage,
    DestiBromLoginPage

):

    @pytest.mark.run(order=1)
    def test_create_account_mobile(self):
        self.navigate_to_login()
        self.register_new_account()
