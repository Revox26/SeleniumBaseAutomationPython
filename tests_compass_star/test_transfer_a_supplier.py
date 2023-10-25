import pytest

from pages_compass_star.assign_director_page import CompassStarAssignDirectorsPage
from pages_compass_star.company_details_page import CompassStarCompanyDetailsTabPage
from pages_compass_star.login_page import CompassStarLoginPage
from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from utilities.custom_logging import get_custom_logger

logger = get_custom_logger(__name__)


class TransferSupplier(
    CompassStarLoginPage,
    CompassStarSuppliersTabPage,
    CompassStarCompanyDetailsTabPage,
    CompassStarAssignDirectorsPage,

):

    @pytest.mark.run(order=1)
    def test_login(self):
        logger.info("Starting the Compass Star login test as admin...")
        self.open_compass_star_page()
        self.compass_star_login_admin()
        logger.info("Compass Star login as admin completed successfully.")

    @pytest.mark.run(order=2)
    def test_check_if_already_have_vat_reg_and_auth_code(self):
        logger.info("Checking if VAT registration and authorization code already exist...")
        self.navigate_to_suppliers_tab()
        self.search_supplier_name_in_suppliers_tab()
        self.input_auth_code_and_vat_reg()
        logger.info("VAT registration and authorization already checked.")

    @pytest.mark.run(order=3)
    def test_transfer_the_supplier_to_confirmed_pre_request(self):
        logger.info("Proceeding to transfer the supplier to confirmed pre-request...")
        self.navigate_to_assign_directors()
        self.select_confirmed_pre_request_for_transfer()
        logger.info("Supplier transfer to confirmed pre-request completed.")
