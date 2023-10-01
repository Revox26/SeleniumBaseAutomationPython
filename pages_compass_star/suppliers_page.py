from seleniumbase import BaseCase


class CompassStarSuppliersTabPage(BaseCase):
    suppliers_tab = "//a[.='Suppliers']"
    search_suppliers_textbox = "input[placeholder='Search']"
    search_suppliers_button = "//button[contains(.,'Search')]"
    director_appointed = "//input[@name='director_appointed']"
    supplier_status = "//select[@name='status']"
    growl_successfully_set_to_ready = "//div[@class='col-sm-12  text-center']//div//strong"

    def set_supplier_status_to_ready(self):
        with open("director_company.txt", "r") as file:
            director_company = file.read().strip()

        self.click(self.suppliers_tab)
        self.click(self.director_appointed)
        self.type(self.search_suppliers_textbox, director_company)
        self.click(self.search_suppliers_button)
        self.select_option_by_text(self.supplier_status, "Ready")
        self.assert_element(self.growl_successfully_set_to_ready)
