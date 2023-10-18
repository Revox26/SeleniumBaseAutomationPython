from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_supplier_land.due_diligence_page import SupplierLandDueDiligencePage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest
import logging

# Set up the logging configuration
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class PassToDueDiligence(
    SupplierLandLoginPage,
    SupplierLandDueDiligencePage,
    CompassStarSuppliersTabPage

):
    @pytest.mark.run(order=1)
    def test_login(self):
        print(logging.info('Starting the login test'))
        self.open_supplier_land_page()
        self.supplier_land_login_as_simon()
        print(logging.info("Login test completed successfully"))

    @pytest.mark.run(order=2)
    def test_pass_to_idd(self):
        print(logging.info("Starting the pass to IDD test"))
        self.navigate_to_initial_check()
        self.pass_the_supplier_to_idd()
        print(logging.info("Pass to IDD test completed successfully"))

    @pytest.mark.run(order=3)
    def test_pass_to_rdd(self):
        print(logging.info("Starting the pass to rdd test"))
        self.navigate_to_suppliers_tab()
        print(logging.info("Starting to get the intermediary name"))
        self.get_intermediary_name()
        self.navigate_to_regular_check()
        self.pass_the_supplier_to_rdd()
        print(logging.info("Pass to RDD test completed successfully"))
