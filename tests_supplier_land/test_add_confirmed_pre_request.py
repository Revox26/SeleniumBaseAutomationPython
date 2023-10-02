from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.offerings_page import SupplierLandOfferingsPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage


class AddConfirmedPreRequest(
    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage,
    SupplierLandOfferingsPage,
):

    def test_login(self):
        self.open_supplier_land_page()
        self.supplier_land_login_as_intermediary()

    def test_navigate_to_pre_request(self):
        self.navigate_to_pre_request()

    def test_pre_request_fields(self):
        self.add_pre_request_fields()
        self.submit_pre_request()

    def test_search_company_in_offerings(self):
        self.get_new_driver()
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()
        self.navigate_to_offerings()
        self.search_company_in_offerings()
