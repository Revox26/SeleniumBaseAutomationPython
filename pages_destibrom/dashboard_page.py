from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class DestibromDashboardPage(BaseCase):
    dashboard_menu = "//a[contains(.,'Dashboard')]"
    dashboard_label = "//h2[contains(.,'Dashboard')]"

    def navigate_to_dashboard_menu(self):
        self.click(self.dashboard_menu)
