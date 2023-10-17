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


class InvitationToReadyNew(
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
        self.open_compass_star_page()
        self.compass_star_login_admin()

    @pytest.mark.run(order=2)
    def test_navigate_to_invite_director(self):
        self.navigate_to_invite_director_page()
        self.invite_director_page()
        self.get_invitation_link()

    @pytest.mark.run(order=3)
    def test_open_invitation_link(self):
        self.open_invitation_link(self.get_invitation_link())
        sb_config.shared_driver = self.driver
        self.skip_the_video()

    @pytest.mark.run(order=4)
    def test_registering_as_director(self):
        self.director_personal_details()
        self.director_account_details()

        try:
            self.director_documentation_page()
            self.director_confirmation_page()

        except Exception as e:  # catch if auto log out occur.
            self.compass_star_login_director()
            self.director_documentation_page()
            print(e)

        self.open_compass_star_page()
        self.compass_star_login_admin()
        self.view_documents()
        self.accept_id_and_set_to_accepted()

        process = self.var1
        if process == "old":
            self.navigate_to_assign_directors_tab()  # assign director using admin account

    @pytest.mark.run(order=5)
    def test_complete_with_bsc(self):
        process = self.var1
        if process != "old":
            self.assign_a_company_in_director_account()  # assign director using director account

        self.navigate_to_complete_with_bsc()
        self.input_bsc_personal_information()
        self.create_your_bsc_account()
        self.bsc_payment_details()

    @pytest.mark.run(order=6)
    def test_proceed_to_complete_with_supplier_land(self):
        self.complete_with_supplier_land()
        self.i_want_to_be_a_supplier_and_interested()

    @pytest.mark.run(order=7)
    def test_set_director_to_ready(self):
        self.csl_log_out()
        self.compass_star_login_admin()
        self.view_documents()
        self.set_status_to_offered()
        self.set_supplier_status_to_ready()
