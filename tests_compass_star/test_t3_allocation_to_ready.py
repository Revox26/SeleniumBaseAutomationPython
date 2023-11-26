import pytest
from pages_compass_star.assign_director_page import CompassStarAssignDirectorsPage
from pages_compass_star.directors_page import CompassStarDirectorPage
from pages_compass_star.login_page import CompassStarLoginPage
from pages_compass_star.suppliers_page import CompassStarSuppliersTabPage
from pages_compass_star.view_director_documents_page import CompassStarViewDocumentsPage

from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt

logger = get_custom_logger(__name__)


class T3AllocationToReady(
    CompassStarLoginPage,
    CompassStarDirectorPage,
    CompassStarViewDocumentsPage,
    CompassStarAssignDirectorsPage,
    CompassStarSuppliersTabPage

):

    @pytest.mark.run(order=1)
    def test_login(self):
        updt(9, 3)
        logger.info("Starting the Compass Star login test as admin...")
        self.open_compass_star_page()
        self.compass_star_login_admin()
        logger.info("Compass Star login as admin completed successfully.")

    @pytest.mark.run(order=2)
    def test_TC_001(self):
        updt(9, 6)
        logger.info("Starting to accept the ID and set the status to accepted...")
        self.view_documents()
        self.accept_director_id()
        logger.info("Director status successfully set to accepted")
        logger.info("Allocating company using admin account...")
        self.navigate_to_assign_directors_tab()
        logger.info("Allocation of the company using the admin account was successful.")

    @pytest.mark.run(order=3)
    def test_TC_002(self):
        updt(9, 9)
        logger.info("Setting company status to ready...")
        self.set_status_to_offered()
        self.set_supplier_status_to_ready()
        logger.info("Company status set to ready.")
