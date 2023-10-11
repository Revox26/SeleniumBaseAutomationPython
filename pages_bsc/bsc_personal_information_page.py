from seleniumbase import BaseCase


class CompleteWithBscPage(BaseCase):
    i_accept_bsc = "//button[contains(text(),'I accept')]"
    next_button = "//button[contains(.,'Next')]"
    bsc_first_name = "//input[contains(@data-testid,'field-First Name')]"
    bsc_email_address = "//input[contains(@data-testid,'field-Email Address')]"
    bsc_company_name = "//input[contains(@data-testid,'field-Company Name')]"
    csl_consulting = "//div[.=' CSL Consulting']"
    i_agree_csl_consulting = "//div[.='CSL Support Package']/following-sibling::div//label[@for='terms']"
    sovereign = "//div[.=' Sovereign']"
    i_agree_sovereign = "//div[.='New Business Insurance']/following-sibling::div//label[@for='terms']"
    supplier_land = "//div[.=' Supplierland']"
    i_agree_supplier_land = "//div[.='Supplier Membership']/following-sibling::div//label[@for='terms']"
    trilogy_banking = "//div[.=' Trilogy Banking']"
    i_agree_trilogy_banking = "//div[.='UK SME Bank Account  (30K Limit Account)']//following-sibling::div//label[@for='terms']"
    bsc_i_agree_5 = "//div[.='Verity BPO']//following-sibling::div//label[@for='terms']"
    my_company_is_not_vat_registered = "//label[.='My company is not VAT registered']/following-sibling::div//label[@for='No']"
    my_company_is_registered_for_flat_rate_vat = "//label[.='My company is registered for Flat Rate VAT']/following-sibling::div//label[@for='No']"
    my_company_is_registered_for_standard_vat = "//label[.='My company is registered for standard VAT (accept £10 per worker surcharge)']/following-sibling::div//label[@for='Yes']"
    bsc_checkout = "(//button[contains(@data-testid,'checkout-button')])[2]"

    def input_bsc_personal_information(self):
        with open("..//data//first_name.txt", "r") as file:
            first_name = file.read().strip()
            print("First Name: ", first_name)
        with open("..//data//email.txt", "r") as file:
            generated_email = file.read().strip()
            print("Email : ", generated_email)
        with open("..//data//director_company.txt", "r") as file:
            company_name = file.read().strip()
            print("Company Name : ", company_name)

        self.click(self.i_accept_bsc)
        self.click(self.next_button)
        self.type(self.bsc_first_name, first_name)
        self.type(self.bsc_email_address, generated_email)
        self.type(self.bsc_company_name, company_name)
        self.scroll_into_view(self.csl_consulting)
        self.js_click(self.i_agree_csl_consulting)
        self.scroll_into_view(self.sovereign)
        self.js_click(self.i_agree_sovereign)
        self.scroll_into_view(self.supplier_land)
        self.js_click(self.i_agree_supplier_land)
        self.scroll_into_view(self.trilogy_banking)
        self.js_click(self.i_agree_trilogy_banking)
        self.click(self.my_company_is_not_vat_registered)
        self.click(self.my_company_is_registered_for_flat_rate_vat)
        self.click(self.my_company_is_registered_for_standard_vat)
        self.js_click(self.bsc_i_agree_5)
        self.click(self.bsc_checkout)
