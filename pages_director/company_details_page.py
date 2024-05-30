from seleniumbase import BaseCase


class DirectorCompanyDetailsPage(BaseCase):
    company_details = "//a[contains(.,'2. Company Details')]"
    let_us_find_a_company = "//button[@id='findACompany']"
    get_company_button = "//a[starts-with(text(),'Get Company')]"
    get_company_text = "//label[.='Name']/..//div[@class='col-sm-6']/..//p"
    company_acquired_growl_message = "//div[.='Congratulations, Company successfully acquired']"
    include_other_industries = "//strong[contains(.,'Include other industries')]"
    non_vat_registered = "//strong[contains(.,'Non-Vat Registered')]"
    vat_registered = "//strong[starts-with(text(),'Vat Registered')]"

    def assign_a_company_in_director_account(self):
        process = self.var3
        self.switch_to_window(0)
        self.click_link_text('My Application')
        self.click(self.company_details)
        self.click(self.let_us_find_a_company)
        if process == "1_7":
            self.click(self.non_vat_registered)
        elif process == "1_8":
            self.click(self.vat_registered)
        else:
            self.click(self.non_vat_registered)
        try:
            self.click(self.get_company_button)
        except Exception as e:
            self.click(self.include_other_industries)
            self.click(self.get_company_button)
        self.assert_element(self.company_acquired_growl_message, timeout=60)
        self.click(self.company_details)


        store_company_text = self.get_text(self.get_company_text)
        with open("..//data//director_company.txt", "w") as file:
            file.write(store_company_text)
