import pytest
from pages_compass_star.assign_director_page import CompassStarAssignDirectorsPage
from pages_compass_star.company_details_page import CompassStarCompanyDetailsTabPage
from pages_compass_star.login_page import CompassStarLoginPage
from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage


class TransferSupplier(
    CompassStarLoginPage,
    CompassStarSuppliersTabPage,
    CompassStarCompanyDetailsTabPage,
    CompassStarAssignDirectorsPage,

):

    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_compass_star_page()
        self.compass_star_login_admin()

    @pytest.mark.run(order=2)
    def test_check_if_already_have_vat_reg_and_auth_code(self):
        self.navigate_to_suppliers_tab()
        self.search_supplier_name_in_suppliers_tab()
        self.input_auth_code_and_vat_reg()

    @pytest.mark.run(order=3)
    def test_transfer_the_supplier_to_confirmed_pre_request(self):
        self.navigate_to_assign_directors()
        self.select_confirmed_pre_request_for_transfer()
