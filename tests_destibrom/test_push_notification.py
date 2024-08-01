import pytest

from pages_destibrom.dashboard_page import DestibromDashboardPage
from pages_destibrom.login_page import DestiBromLoginPage
from pages_destibrom.push_notificaion_page.external_link_pn_page import DestinationXExternalLinkNotificationPage
from pages_destibrom.push_notification_page import DestibromPushNotificationPage


class DestiBromPushNotification(
    DestiBromLoginPage,
    DestibromDashboardPage,
    DestibromPushNotificationPage,
    DestinationXExternalLinkNotificationPage

):

    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_destibrom_page()
        self.destibrom_login_as_super_admin()
        self.choose_a_destination()
        self.navigate_to_push_notification_url()

    @pytest.mark.run(order=2)
    def test_add_external_links_notification(self):
        self.send_external_link_notification()

    @pytest.mark.run(order=3)
    def test_add_location_notification(self):
        self.add_location_notification()

    @pytest.mark.run(order=4)
    def test_add_category_notification(self):
        self.add_category_notification()
