from seleniumbase import BaseCase
from faker import Faker


class DirectorPersonalDetailsPage(BaseCase):
    personal_details_label = "// span[contains(text(), 'Personal details')]"
    title = "//input[contains(@value,'mr')]"
    first_name = "//input[@id='first_name']"
    nationality = "//input[@id='nationality']"
    nationality_dropdown = "//select[@id='nationality']"
    occupation = "//input[@id='occupation']"
    professional_interest = "//span[contains(text(),'None selected')]"
    select_transport = "//label[starts-with(text(),' Transport')]"
    date_of_birth = "//input[contains(@class,'form-control hasDatepicker')]"
    mobile_number = "//input[@id='phone']"
    address = "//input[@id='address']"
    town_city = "//input[@id='town']"
    province = "//input[@id='county']"
    country = "//select[@id='country']"
    zip_code = "//input[@name='post_code']"
    same_address = "//input[@id='same-as-permanent-address']"
    smart_phone = "//input[@id='has_mobile_id']"
    android_phone = "//input[@name='android_phone']"
    mobile_close_button = "//button[@id='close-has-mobile-modal']"
    continue_button = "//button[contains(.,'Continue')]"

    def director_personal_details(self):
        fake = Faker()

        self.assert_element(self.personal_details_label)

        self.click(self.title)

        if self.is_element_present(self.nationality_dropdown):
            self.select_option_by_text(self.nationality_dropdown, "Filipino")
        else:
            self.type(self.nationality, "Filipino")

        self.type(self.occupation, fake.job())

        self.click(self.professional_interest)

        self.click(self.select_transport)

        self.click(self.title)

        self.type(self.date_of_birth, "1999-04-08 \n")

        self.type(self.mobile_number, '9' + fake.random_int(min=100000000, max=999999999).__str__())

        self.type(self.address, fake.address())

        self.type(self.town_city, fake.city())

        self.type(self.province, fake.state())

        self.select_option_by_text(self.country, "Philippines")

        self.type(self.zip_code, "4120")

        self.click(self.same_address)

        self.click(self.smart_phone)

        self.click(self.android_phone)

        self.click(self.mobile_close_button)

        self.click(self.continue_button)
