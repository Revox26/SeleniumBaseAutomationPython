import pytest

from AppiumPython.pages_csl_mobile.account_details_screen import CslMobileAccountDetailsPage
from AppiumPython.pages_csl_mobile.login_screen import CslMobileLoginPage
from AppiumPython.pages_csl_mobile.personal_details_screen import CslMobilePersonalDetailsPage
from AppiumPython.pages_csl_mobile.welcome_video_screen import CslMobileWelcomeVideoPage
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


class InvitationToReadyWithMobile(
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
    SupplierLandLoginPage,
    CslMobileLoginPage,
    CslMobileWelcomeVideoPage,
    CslMobileAccountDetailsPage,
    CslMobilePersonalDetailsPage

):

    @pytest.mark.run(order=1)
    def test_login(self):
        updt(7, 1)
        logger.info("Starting the Compass Star login test as admin...")
        self.open_compass_star_page()
        self.compass_star_login_admin()
        logger.info("Compass Star login as admin completed successfully.")

    @pytest.mark.run(order=2)
    def test_navigate_to_invite_director(self):
        updt(7, 2)
        logger.info("Navigating to the invite director page...")
        self.navigate_to_invite_director_page()
        self.invite_director_page()
        self.get_referral_code()
        logger.info("Referral Code has been generated successfully")

    @pytest.mark.run(order=3)
    def test_csl_mobile_registration(self):
        self.input_referral_code()
        self.skip_csl_app_video()
        self.csl_mobile_account_details()
        self.csl_mobile_personal_details()
