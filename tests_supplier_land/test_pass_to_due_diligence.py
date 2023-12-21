from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_supplier_land.due_diligence_page import SupplierLandDueDiligencePage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest
from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt

logger = get_custom_logger(__name__)


class PassToDueDiligence(
    SupplierLandLoginPage,
    SupplierLandDueDiligencePage,
    CompassStarSuppliersTabPage

):
    @pytest.mark.run(order=1)
    def test_login(self):
        updt(8, 2)
        logger.info("Starting the login test...")
        self.open_supplier_land_page()

        self.supplier_land_login_as_simon()
        logger.info("Login test as Simon completed successfully.")

    @pytest.mark.run(order=2)
    def test_pass_to_idd(self):
        updt(8, 4)
        logger.info("Navigating to the initial check page...")
        self.navigate_to_initial_check()
        logger.info("Navigated to initial check page successfully.")

        logger.info("Starting the pass to IDD test...")
        self.pass_the_supplier_to_idd()
        logger.info("Pass to IDD test completed successfully.")

    @pytest.mark.run(order=3)
    def test_get_the_intermediary_name(self):
        updt(8, 6)
        logger.info("Navigating to the suppliers tab...")
        self.navigate_to_suppliers_tab()
        logger.info("Navigated to suppliers tab successfully.")

        logger.info("Getting the intermediary name...")
        self.get_intermediary_name()
        logger.info("Got the intermediary name successfully.")

    @pytest.mark.run(order=4)
    def test_pass_to_rdd(self):
        updt(8, 8)
        logger.info("Navigating to the regular check page...")
        self.navigate_to_regular_check()
        logger.info("Navigated to regular check page successfully.")

        logger.info("Starting the pass to RDD test...")
        self.pass_the_supplier_to_rdd()
        logger.info("Pass to RDD test completed successfully.")
