from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class SupplierLandLoginPage(BaseCase):
    __logo_icon = "//img[@src='/supplierland/images/login_logo.png']"
    __username = "//input[@placeholder='User Email']"
    __password = "//input[@placeholder='Password']"
    __login_button = "//button[@type='submit']"

    def open_supplier_land_page(self):  # select environmental staging
        instance = self.data

        environmental_staging = {
            "qa": Readconfig.get_qa_sl_url(),
            "v1": Readconfig.get_v1_sl_url(),
            "v2": Readconfig.get_v2_sl_url(),
            "v3": Readconfig.get_v3_sl_url(),
            "v4": Readconfig.get_v4_sl_url(),
            "replica": Readconfig.get_replica_sl_url(),
            "echo": Readconfig.get_echo_sl_url(),
        }
        self.open(environmental_staging.get(instance, Readconfig.get_qa_sl_url()))


    def login(self, username, password):
        self.type(self.__username, username)
        self.type(self.__password, password)
        self.click(self.__login_button)

    def supplier_land_login_as_it_dev(self):
        self.login(Readconfig.get_it_dev_username(), Readconfig.get_password())

    def supplier_land_login_as_george(self):
        self.login(Readconfig.get_george_user_name(), Readconfig.get_password())

    def supplier_land_login_as_intermediary(self):
        self.login(Readconfig.get_intermediary_username(), Readconfig.get_password())

    def open_supplier_land_new_window(self):
        self.get_new_driver()
        self.open(Readconfig.get_qa_sl_url())
        self.maximize_window()

    def complete_with_supplier_land(self):
        self.refresh_page()
        self.click("a[type='button']")
        self.type(self.__password, Readconfig.get_director_password())
        self.click(self.__login_button)


