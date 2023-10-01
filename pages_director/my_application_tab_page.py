from seleniumbase import BaseCase


class DirectorMyApplicationTabPage(BaseCase):
    my_application_tab = "//a[contains(.,'My Application')]"
    complete_application_with_bsc_button = "//a[contains(.,'Complete Application with BSC')]"

    def navigate_to_complete_with_bsc(self):
        self.click(self.my_application_tab)
        self.click(self.complete_application_with_bsc_button)
        self.switch_to_window(1)
