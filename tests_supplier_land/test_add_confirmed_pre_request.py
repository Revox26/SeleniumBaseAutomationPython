from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.offerings_page import SupplierLandOfferingsPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest
from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt

logger = get_custom_logger(__name__)


class AddConfirmedPreRequest(
    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage,
    SupplierLandOfferingsPage,

):

    @pytest.mark.run(order=1)
    def test_login(self):
        updt(4, 1)
        logger.info("Starting the login test as intermediary...")
        self.open_supplier_land_page()
        self.supplier_land_login_as_intermediary()
        logger.info("Login as intermediary completed successfully.")

    @pytest.mark.run(order=2)
    def test_navigate_to_pre_request(self):
        updt(4, 2)
        logger.info("Navigating to the pre-request page...")
        self.navigate_to_pre_request()
        logger.info("Navigated to pre-request page successfully.")

    @pytest.mark.run(order=3)
    def test_pre_request_fields(self):
        updt(4, 3)
        logger.info("Adding new pre-request fields...")
        self.add_pre_request_fields()
        self.submit_pre_request()
        logger.info("Pre-request submitted successfully.")

    @pytest.mark.run(order=4)
    def test_search_company_in_offerings(self):
        updt(4, 3.5)
        logger.info("Logging in as George...")
        self.get_new_driver()
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()
        logger.info("Login as George completed successfully.")

        logger.info("Navigating to the offerings page...")
        self.navigate_to_offerings()
        logger.info("Navigated to offerings page successfully.")

        logger.info("Searching for a company in offerings...")
        self.search_company_in_offerings()
        logger.info("Company search in offerings completed.")
        updt(4, 4)
