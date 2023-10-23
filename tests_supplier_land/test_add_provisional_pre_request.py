from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.offerings_page import SupplierLandOfferingsPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest


class AddProvisionalPreRequest(
    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage,
    SupplierLandOfferingsPage,
):
    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()

    @pytest.mark.run(order=2)
    def test_navigate_to_pre_request(self):
        self.navigate_to_pre_request()

    @pytest.mark.run(order=3)
    def test_pre_request_fields(self):
        if self.data == "v2":
            self.t3_add_pre_request_fields()
        else:
            self.add_pre_request_fields()
        self.submit_pre_request()

    @pytest.mark.run(order=4)
    def test_search_company_in_offerings(self):
        self.navigate_to_offerings()
        self.search_company_in_offerings()
