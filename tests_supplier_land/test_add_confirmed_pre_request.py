from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.offerings_page import SupplierLandOfferingsPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest

from utilities.custom_logging import get_custom_logger

logger = get_custom_logger(__name__)


class AddConfirmedPreRequest(
    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage,
    SupplierLandOfferingsPage,

):

    @pytest.mark.run(order=1)
    def test_login(self):
        logger.info("Starting the login test as intermediary...")
        self.open_supplier_land_page()
        self.supplier_land_login_as_intermediary()
        logger.info("Login as intermediary completed successfully.")

    @pytest.mark.run(order=2)
    def test_navigate_to_pre_request(self):
        logger.info("Navigating to the pre-request page...")
        self.navigate_to_pre_request()
        logger.info("Successfully navigated to the pre-request page.")

    @pytest.mark.run(order=3)
    def test_pre_request_fields(self):
        logger.info("Adding new pre-request fields...")
        self.add_pre_request_fields()
        self.submit_pre_request()
        logger.info("Pre-request submitted successfully.")

    @pytest.mark.run(order=4)
    def test_search_company_in_offerings(self):
        logger.info("Logging in as George...")
        self.get_new_driver()
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()
        logger.info("Login as George completed successfully.")
        logger.info("Navigating to the offerings page...")
        self.navigate_to_offerings()
        logger.info("Searching for a company in offerings...")
        self.search_company_in_offerings()
        logger.info("Company search in offerings completed.")
