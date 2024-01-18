from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_supplier_land.due_diligence_page import SupplierLandDueDiligencePage
from pages_supplier_land.import_page import SupplierLandImportPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest
from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt
from utilities.withdraw_and_enroll_excel_sheets import WithdrawAndEnrollIddExcelSheet

logger = get_custom_logger(__name__)


class WithdrawInitialDueDiligence(
    SupplierLandLoginPage,
    SupplierLandDueDiligencePage,
    SupplierLandImportPage,
    WithdrawAndEnrollIddExcelSheet,
    CompassStarSuppliersTabPage

):
    @pytest.mark.run(order=1)
    def test_login(self):
        updt(4, 1)
        logger.info("Starting the login test...")
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()
        logger.info("Login test completed successfully.")

    @pytest.mark.run(order=2)
    def test_get_the_intermediary_name(self):
        updt(4, 2)
        logger.info("Navigating to the suppliers tab...")
        self.navigate_to_suppliers_tab()
        self.tick_the_initial_due_diligence_status()
        logger.info("Navigated to suppliers tab successfully.")

        logger.info("Getting the intermediary name...")
        self.get_intermediary_name()
        logger.info("Got the intermediary name successfully.")

    @pytest.mark.run(order=3)
    def test_navigate_to_withdraw_idd_page(self):
        updt(4, 3)
        logger.info("Navigating to the withdraw idd page...")
        self.navigate_to_withdraw_idd()
        logger.info("Navigated to withdraw idd page successfully.")

    @pytest.mark.run(order=4)
    def test_proceed_to_withdraw_idd(self):
        updt(4, 4)
        self.input_company_data_in_enroll_withdraw_csv()
        logger.info("Proceeding to the withdraw idd...")
        self.proceed_to_withdraw_idd()
        logger.info("Withdraw idd successfully.")
