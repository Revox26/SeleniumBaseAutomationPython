from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage


class AddProvisionalPreRequest(
    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage
):

    def test_login(self):
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()

    def test_navigate_to_pre_request(self):
        self.navigate_to_pre_request()

    def test_pre_request_fields(self):
        self.add_pre_request_fields()
        self.submit_pre_request()


