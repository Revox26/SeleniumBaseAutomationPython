from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_supplier_land.due_diligence_page import SupplierLandDueDiligencePage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest


class PassToDueDiligence(
    SupplierLandLoginPage,
    SupplierLandDueDiligencePage,
    CompassStarSuppliersTabPage

):
    @pytest.mark.run(order=1)
    def test_login(self):
        print("Starting the Login test...")
        self.open_supplier_land_page()
        self.supplier_land_login_as_simon()
        print("Login test as Simon completed successfully")

    @pytest.mark.run(order=2)
    def test_pass_to_idd(self):
        print("\n Starting the pass to IDD test...")
        self.navigate_to_initial_check()
        self.pass_the_supplier_to_idd()
        print("Pass to IDD test completed successfully")

    @pytest.mark.run(order=3)
    def test_pass_to_rdd(self):
        print("\nStarting to get the intermediary name")
        self.navigate_to_suppliers_tab()
        self.get_intermediary_name()
        print("Starting the pass to RDD test...")
        self.navigate_to_regular_check()
        self.pass_the_supplier_to_rdd()
        print("Pass to RDD test completed successfully")
