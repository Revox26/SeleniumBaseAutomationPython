from pages_supplier_land.add_pre_request_page import SupplierLandAddNewPreRequestPage
from pages_supplier_land.offerings_page import SupplierLandOfferingsPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage
import pytest

from utilities.custom_logging import get_custom_logger

logger = get_custom_logger(__name__)


class AddProvisionalPreRequest(

    SupplierLandLoginPage,
    SupplierLandAddNewPreRequestPage,
    SupplierLandOfferingsPage,
):
    @pytest.mark.run(order=1)
    def test_login(self):
        logger.info("Starting the login test...")
        self.open_supplier_land_page()
        self.supplier_land_login_as_george()
        logger.info("Login test as George completed successfully.")

    # @pytest.mark.run(order=2)
    # def test_navigate_to_pre_request(self):
    #     logger.info("Navigating to the pre-request page...")
    #     self.navigate_to_pre_request()
    #
    # @pytest.mark.run(order=3)
    # def test_pre_request_fields(self):
    #     logger.info("Filling in pre-request fields...")
    #     if self.data == "v2":
    #         self.t3_add_pre_request_fields()
    #     else:
    #         self.add_pre_request_fields()
    #     self.submit_pre_request()
    #     logger.info("Pre-request fields submitted successfully.")
    #
    # @pytest.mark.run(order=4)
    # def test_search_company_in_offerings(self):
    #     logger.info("Navigating to the offerings page...")
    #     self.navigate_to_offerings()
    #     self.search_company_in_offerings()
    #     logger.info("Company search in offerings completed.")
