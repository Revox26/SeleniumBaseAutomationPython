import pytest
from seleniumbase import config as sb_config
from pages_bsc.bsc_create_your_account_page import BscCreateYOurAccountPage
from pages_bsc.bsc_payment_details_page import BscPaymentDetailsPage
from pages_bsc.bsc_personal_information_page import CompleteWithBscPage
from pages_compass_star.assign_director_page import CompassStarAssignDirectorsPage
from pages_compass_star.directors_page import CompassStarDirectorPage
from pages_compass_star.login_page import CompassStarLoginPage
from pages_compass_star.invite_director_page import CompassStarInviteDirectorPage
from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_compass_star.view_director_documents_page import CompassStarViewDocumentsPage
from pages_director.account_details_page import DirectorAccountDetailsPage
from pages_director.company_details_page import DirectorCompanyDetailsPage
from pages_director.confirmatiton_success_page import DirectorConfirmationPage
from pages_director.documentation_page import DirectorDocumentationPage
from pages_director.my_application_tab_page import DirectorMyApplicationTabPage
from pages_director.personal_details_page import DirectorPersonalDetailsPage
from pages_director.video_page import DirectorVideoPage
from pages_supplier_land.find_a_customer_page import SupplierLandFindCustomerPage
from pages_supplier_land.sl_login_page import SupplierLandLoginPage

from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt

logger = get_custom_logger(__name__)


class AcceptedToReady(
    BscCreateYOurAccountPage,
    BscPaymentDetailsPage,
    CompassStarLoginPage,
    CompassStarInviteDirectorPage,
    CompassStarDirectorPage,
    CompassStarViewDocumentsPage,
    CompassStarAssignDirectorsPage,
    CompassStarSuppliersTabPage,
    CompleteWithBscPage,
    DirectorCompanyDetailsPage,
    DirectorVideoPage,
    DirectorPersonalDetailsPage,
    DirectorAccountDetailsPage,
    DirectorDocumentationPage,
    DirectorConfirmationPage,
    DirectorMyApplicationTabPage,
    SupplierLandFindCustomerPage,
    SupplierLandLoginPage

):

    @pytest.mark.run(order=1)
    def test_login(self):
        updt(7, 1)
        logger.info("Starting the Compass Star login test as admin...")
        self.open_compass_star_page()
        self.compass_star_login_admin()
        logger.info("Compass Star login as admin completed successfully.")

    @pytest.mark.run(order=4)
    def test_allocation_of_director(self):
        updt(7, 4)
        logger.info("Starting to accept the ID and set the status to accepted...")
        self.view_documents()
        self.accept_id_and_set_to_accepted()
        logger.info("Director status successfully set to accepted")

    @pytest.mark.run(order=5)
    def test_complete_with_bsc(self):
        updt(7, 5)
        self.csl_log_out()
        self.compass_star_login_director()
        logger.info("Allocating company using director account...")
        self.assign_a_company_in_director_account()
        logger.info("Allocation of the company using the director's account was successful.")

        logger.info("Completing the process with BSC...")

        try:
            self.navigate_to_complete_with_bsc()
            self.input_bsc_personal_information()
            self.create_your_bsc_account()
            self.bsc_payment_details()
            logger.info("BSC process completed successfully.")

        except Exception as e:  # catch if error in BSC occur.
            logger.error("BSC Process not completed")

    @pytest.mark.run(order=6)
    def test_proceed_to_complete_with_supplier_land(self):
        updt(7, 6)
        logger.info("Completing the process with Supplier Land...")
        self.complete_with_supplier_land()
        self.i_want_to_be_a_supplier_and_interested()
        logger.info("Supplier Land process completed successfully.")

    @pytest.mark.run(order=7)
    def test_set_director_to_ready(self):
        updt(7, 7)
        logger.info("Setting company status to ready...")
        self.csl_log_out()
        self.compass_star_login_admin()
        self.view_documents()
        self.set_status_to_offered()
        self.set_supplier_status_to_ready()
        logger.info("Company status set to ready.")
