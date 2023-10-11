from seleniumbase import BaseCase


class DirectorCompanyDetailsPage(BaseCase):
    company_details = "//a[contains(.,'2. Company Details')]"
    let_us_find_a_company = "//button[@id='findACompany']"
    get_company_button = "//a[starts-with(text(),'Get Company')]"
    get_company_text = "//label[.='Name']/..//div[@class='col-sm-6']/..//p"
    company_acquired_growl_message = "//div[.='Congratulations, Company successfully acquired']"

    def assign_a_company_in_director_account(self):
        self.switch_to_window(0)
        self.click_link_text('My Application')
        self.click(self.company_details)
        self.click(self.let_us_find_a_company)
        self.click(self.get_company_button)
        self.assert_element(self.company_acquired_growl_message, timeout=60)
        self.click(self.company_details)

        store_company_text = self.get_text_content(self.get_company_text)
        with open("..//data//director_company.txt", "w") as file:
            file.write(store_company_text)
