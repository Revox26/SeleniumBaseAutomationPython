from seleniumbase import BaseCase


class CompassStarSuppliersTabPage(BaseCase):
    suppliers_tab = "//a[.='Suppliers']"
    search_suppliers_textbox = "input[placeholder='Search']"
    search_suppliers_button = "//button[contains(.,'Search')]"
    director_appointed = "//input[@name='director_appointed']"
    _amend = "//input[@name='amend']"
    _verify = "//input[@name='verify']"
    _initial_due_diligence = "//input[@name='initial_due_diligence']"
    supplier_status = "//select[@name='status']"
    growl_successfully_set_to_ready = "//div[@class='col-sm-12  text-center']//div//strong"
    _company_details = "//a[contains(.,'Ltd')]"
    _intermediary_name_text = "//th[.='Intermediary']//following::td[position()=2]"
    _company_name_text = "//a[contains(text(),'Ltd') or contains(text(),'limited')]"

    def navigate_to_suppliers_tab(self):
        self.click(self.suppliers_tab)

    def set_supplier_status_to_ready(self):
        with open("..//data//director_company.txt", "r") as file:
            director_company = file.read().strip()

        self.click(self.suppliers_tab)
        self.click(self.director_appointed)
        self.type(self.search_suppliers_textbox, director_company)
        self.click(self.search_suppliers_button)
        self.select_option_by_text(self.supplier_status, "Ready")
        self.assert_element(self.growl_successfully_set_to_ready)

    def search_supplier_name_in_suppliers_tab(self):
        company_name_var = self.var1
        self.type(self.search_suppliers_textbox, company_name_var)
        self.click(self._amend)
        self.click(self._verify)
        self.click(self.search_suppliers_button)
        self.click(self._company_details)

    def get_intermediary_name(self):
        company_name_var = self.var1
        self.type(self.search_suppliers_textbox, company_name_var)
        self.click(self._amend)
        self.click(self._verify)
        self.click(self.search_suppliers_button)
        self.scroll_into_view(self._intermediary_name_text)
        intermediary_name = self.get_text(self._intermediary_name_text)
        company_name = self.get_text(self._company_name_text)
        with open("..//data//intermediary.txt", "w") as file:
            file.write(intermediary_name)

        with open("..//data//director_company.txt", "w") as file:
            file.write(company_name)

    def tick_the_initial_due_diligence_status(self):
        self.click(self._initial_due_diligence)
