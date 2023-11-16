from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class CompassStarLoginPage(BaseCase):
    logo_icon = "//img[@src='/supplierland/images/login_logo.png']"
    profile_button = "//a[contains(@role,'button')]"
    log_out = "//a[.='Logout']"
    username = "//input[@placeholder='Email address']"
    password = "//input[@placeholder='Password']"
    login_button = "//button[@type='submit']"

    def open_compass_star_page(self):  # select environmental staging
        instance = self.data

        csl_urls = {
            "qa": Readconfig.get_qa_csl_url(),
            "v1": Readconfig.get_v1_csl_url(),
            "v2": Readconfig.get_v2_csl_url(),
            "v3": Readconfig.get_v3_csl_url(),
            "v4": Readconfig.get_v4_csl_url(),
            "replica": Readconfig.get_replica_csl_url(),
            "testing": Readconfig.get_testing_csl_url(),
            "echo": Readconfig.get_echo_csl_url()
        }

        self.open(csl_urls.get(instance, Readconfig.get_qa_csl_url()))
        self.save_cookies(name="cookies.txt")

    def compass_star_login_admin(self):
        if self.data == "testing":
            self.type(self.username, Readconfig.get_it_dev_jech_username())
        else:
            self.type(self.username, Readconfig.get_it_dev_username())
        self.type(self.password, Readconfig.get_password())
        self.click(self.login_button)

    def compass_star_login_as_jech(self):
        self.type(self.username, Readconfig.get_it_dev_jech_username())
        self.type(self.password, Readconfig.get_password())
        self.click(self.login_button)

    def open_compass_star_new_window(self):
        self.get_new_driver()
        self.open(Readconfig.get_qa_sl_url())
        self.maximize_window()

    def csl_log_out(self):
        self.click(self.profile_button, timeout=15)
        self.click(self.log_out)
        self.sleep(5)

    def compass_star_login_director(self):
        with open("..//data//email.txt", "r") as file:
            email = file.read().strip()
        self.type(self.username, email)
        self.type(self.password, Readconfig.get_director_password())
        self.click(self.login_button)
