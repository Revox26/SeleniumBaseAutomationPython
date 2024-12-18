from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromDashboardPage(BaseCase):
    dashboard_menu = "//a[contains(.,'Dashboard')]"
    dashboard_label = "//h2[contains(.,'Dashboard')]"
    add_new_destination_button = "//a[@id='addDestination']"
    dashboard_location = "//h5[.='  Locations']"
    dashboard_sponsored_ads = "//h5[.='  Sponsored Ads']"
    dashboard_news_and_events = "//h5[.='  News & Events']"
    dashboard_administrator = "//h5[.='  Administrators']"
    dashboard_notification_sent = "//h5[.=' Notifications Sent']"
    select_a_destination = "//select[.='Select a Destination']"

    firebase_label = "//h5[.='Firebase  ']"
    sendgrid_label = "// h5[. = 'SendGrid  ']"

    def navigate_to_dashboard_menu(self):
        self.click(self.dashboard_menu)

    def choose_a_destination(self):
        # self.select_option_by_text(self.select_a_destination, self.var2)
        self.assert_element(self.firebase_label, timeout=60)
        self.assert_element(self.firebase_label, timeout=60)
        # self.assert_element(self.add_new_destination_button)
        # self.assert_element(self.dashboard_location, timeout=60)
        # self.assert_element(self.dashboard_sponsored_ads, timeout=60)
        # self.assert_element(self.dashboard_news_and_events, timeout=60)
        # self.assert_element(self.dashboard_administrator, timeout=60)
        # self.assert_element(self.dashboard_notification_sent, timeout=60)
