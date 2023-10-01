from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class CompassStarLoginPage(BaseCase):
    logo_icon = "//img[@src='/supplierland/images/login_logo.png']"
    profile_button = "//a[contains(@role,'button')]"
    log_out = "//a[.='Logout']"
    username = "//input[@placeholder='Email address']"
    password = "//input[@placeholder='Password']"
    login_button = "//button[@type='submit']"

    def open_compass_star_page(self):
        instance = self.data

        if instance == "qa":
            self.open(Readconfig.get_qa_csl_url())
        elif instance == "v1":
            self.open(Readconfig.get_v1_csl_url())
        elif instance == "v2":
            self.open(Readconfig.get_v2_csl_url())
        elif instance == "v3":
            self.open(Readconfig.get_v3_csl_url())
        elif instance == "v4":
            self.open(Readconfig.get_v4_csl_url())
        elif instance == "replica":
            self.open(Readconfig.get_replica_csl_url())
        elif instance == "echo":
            self.open(Readconfig.get_echo_csl_url())
        else:
            self.open(Readconfig.get_qa_csl_url())

        self.save_cookies(name="cookies.txt")

    def compass_star_login_admin(self):
        self.type(self.username, Readconfig.get_it_dev_username())
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
        with open("email.txt", "r") as file:
            email = file.read().strip()
        self.type(self.username, email)
        self.type(self.password, Readconfig.get_director_password())
        self.click(self.login_button)
