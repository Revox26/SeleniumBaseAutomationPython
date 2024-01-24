import pytest

from pages_destibrom.dashboard_page import DestibromDashboardPage
from pages_destibrom.login_page import DestiBromLoginPage
from pages_destibrom.push_notification_page import DestibromPushNotificationPage


class DestiBromPushNotification(
    DestiBromLoginPage,
    DestibromPushNotificationPage,

):

    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_destibrom_page()
        self.destibrom_login_as_super_admin()
        self.assert_element(DestibromDashboardPage.dashboard_label)
        self.navigate_to_push_notification_url()

    @pytest.mark.run(order=2)
    def test_add_external_links_notification(self):
        self.add_external_links_notification()

    @pytest.mark.run(order=3)
    def test_add_location_notification(self):
        self.add_location_notification()

    @pytest.mark.run(order=4)
    def test_add_category_notification(self):
        self.add_category_notification()
