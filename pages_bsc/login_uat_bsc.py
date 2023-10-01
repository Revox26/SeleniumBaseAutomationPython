from seleniumbase import BaseCase


class BscLoginUatPage(BaseCase):
    lup_login = "//a[.='Login']"
    lup_email_address = "input[placeholder='Your email address']"
    lup_password = "input[placeholder='Your password']"
    lup_login_button = "button[type='submit']"
    lup_logo_container = "//div[@class='styles_logoContainer__SC-dJ my-4 mx-3']"
    lup_log_out_button = "//span[contains(.,'Log Out')]"


    def login_bsc_uat_url(self):
        self.get_new_driver()
        self.open("https://uat-web-tbsc.azurewebsites.net/")
        self.bring_active_window_to_front()
        self.click(self.lup_login)
        self.type(self.lup_email_address, "JDCTestSupplier@test.com")
        self.type(self.lup_password, "Test123456!")
        self.click(self.lup_login_button)

    def logout_bsc_uat_url(self):
        self.click(self.lup_logo_container)
        self.click(self.lup_log_out_button)
