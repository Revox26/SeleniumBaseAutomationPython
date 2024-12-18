import pytest

from pages_business_centre.dashboard_page import BusinessCentreDashboardnPage
from pages_business_centre.login_page import BusinessCentreLoginPage


class BusinessCentreRegressionTesting(
    BusinessCentreLoginPage,
    BusinessCentreDashboardnPage

):

    @pytest.mark.run(order=1)
    def test_sign_up(self):
        self.open_business_centre_page()
        self.signup_as_user()

    @pytest.mark.run(order=2)
    def test_login(self):
        self.open_business_centre_page()
        self.login_as_user()

    @pytest.mark.run(order=3)
    def test_add_shortcut(self):
        self.add_shortcut_favourites()

    @pytest.mark.run(order=4)
    def test_delete_shortcut(self):
        self.delete_shortcut()

    # @pytest.mark.run(order=1)
    # def test_regression(self):
    #     self.open_business_centre_page()
    #     self.signup_as_user()
    #     self.login_as_user()
    #     self.add_shortcut_favourites()
    #     self.delete_shortcut()
