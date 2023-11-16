import pytest
from pages_compass_star.communications_page import CompassStarCommunicationsTabPage
from pages_compass_star.login_page import CompassStarLoginPage
from utilities.custom_logging import get_custom_logger
from utilities.read_excel_sheets import ReadCommsTemplate

logger = get_custom_logger(__name__)


class UploadCommunicationsTemplate(
    CompassStarLoginPage,
    ReadCommsTemplate,
    CompassStarCommunicationsTabPage

):

    @pytest.mark.run(order=0)
    def test_login(self):
        logger.info("Starting the Compass Star login test as admin...")
        self.open_compass_star_page()
        self.compass_star_login_admin()
        logger.info("Compass Star login as admin completed successfully.")

    @pytest.mark.run(order=1)
    def test_upload_communications(self):
        logger.info("Starting to upload the communications template...")
        list_of_templates = {
            'vat': (self.input_company_number_in_vat_return_csv, self.upload_vat_return_template),
            'invoice': (self.input_company_number_in_invoice_approval_csv, self.upload_invoice_approval_template),
            'funding': (self.input_company_number_in_funding_request_csv, self.upload_funding_request_template),
            'change_of_flat_rate': (self.input_company_number_in_change_of_flat_rate_csv, self.upload_change_of_flat_rate_template),

        }
        # Handle the selected template
        if self.var2 in list_of_templates:
            input_method, upload_method = list_of_templates[self.var2]
            input_method(self.var1)
            self.navigate_to_communications_tab()
            upload_method()

        elif self.var2 == 'all':
            # Handle the combination of all templates
            for template_type, (input_method, upload_method) in list_of_templates.items():
                input_method(self.var1)
                self.navigate_to_communications_tab()
                upload_method()

        logger.info("Communication template uploaded successfully.")
