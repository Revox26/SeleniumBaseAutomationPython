from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_supplier_land.due_diligence_page import SupplierLandInitialCheckPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest


class AddProvisionalPreRequest(
    SupplierLandLoginPage,
    SupplierLandInitialCheckPage,
    CompassStarSuppliersTabPage

):
    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_supplier_land_page()
        self.supplier_land_login_as_simon()

    @pytest.mark.run(order=2)
    def test_pass_to_idd(self):
        self.navigate_to_initial_check()
        self.pass_the_supplier_to_idd()

    @pytest.mark.run(order=3)
    def test_pass_to_rdd(self):
        self.navigate_to_suppliers_tab()
        self.get_intermediary_name()
        self.navigate_to_regular_check()
        self.pass_the_supplier_to_rdd()
