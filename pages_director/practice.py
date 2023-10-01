from seleniumbase import BaseCase
from seleniumbase import config as sb_config


class MyClass(BaseCase):

    def test_1(self):
        self.open("https://www.facebook.com")
        self.sleep(2)
        sb_config.shared_driver = self.driver  # Store the driver instance

    def test_2(self):
        self.get_new_driver()  # Create a new driver instance
        sb_config.shared_driver = self.driver  # Store the driver instance
        self.open("https://www.youtube.com")  # Open Facebook again
        # Add your test logic for test_2 here

    def test_3(self):
        self.get_new_driver()  # Create a new driver instance
        self.open("https://www.google.com")  # Open Facebook again
        sb_config.shared_driver = self.driver  # Store the driver instance
        # Add your test logic for test_2 here


if __name__ == "__main__":
    MyClass.main()
