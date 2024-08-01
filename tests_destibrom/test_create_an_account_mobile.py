import pytest

from AppiumPython.pages_destination_x.create_an_account_screen import DestinationxCreateAnAccountPage
from pages_destibrom.login_page import DestiBromLoginPage


class DestinationxCreateAnAccountMobile(

    DestinationxCreateAnAccountPage,
    DestiBromLoginPage

):

    @pytest.mark.run(order=1)
    def test_create_account_mobile(self):
        self.register_new_account()
