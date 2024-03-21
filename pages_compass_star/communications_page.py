from seleniumbase import BaseCase
from datetime import datetime


class CompassStarCommunicationsTabPage(BaseCase):
    communications_tab = "//a[contains(.,'Communications')]"
    select_template = "//select[@id='template']"
    input_comms_note = "//textarea[@id='comment']"
    _upload_csv_file = "//input[@id='csv-upload']"
    send_to_communications_queue = "//button[@id='send-comms-queue']"
    scheduled = "//input[@name='scheduled']"
    send_sms = "//input[@name='send_sms']"
    comms_not_successfully_upload_alert = "//div[contains(@class,'alert alert-danger')]"
    comms_successfully_upload_alert = "//div[@class='growl growl-notice growl-medium']"

    def navigate_to_communications_tab(self):
        self.click(self.communications_tab)

    def __upload_template__(self, template_name, template_path, note, ):
        timestamp = datetime.now().strftime("%Y/%m/%d/%H%M%S")
        self.select_option_by_text(self.select_template, template_name)
        self.choose_file(self._upload_csv_file, template_path)
        self.type(self.input_comms_note, note + " " + timestamp)
        self.click(self.scheduled)
        self.click(self.send_sms)
        self.click(self.send_to_communications_queue)

    def upload_vat_return_template(self):
        self.__upload_template__("Vat Return ( Requires CSV )", "..//comms_templates/Vat_Return.csv", "Upload Vat Return")

    def upload_invoice_approval_template(self):
        self.__upload_template__("Invoice Approval ( Requires CSV )", "..//comms_templates/Invoice_Approval.csv", "Upload Invoice Approval")

    def upload_funding_request_template(self):
        self.__upload_template__("Funding Request ( Requires CSV )", "..//comms_templates/Funding_Request.csv", "Upload Funding Request")

    def upload_change_of_flat_rate_template(self):
        self.__upload_template__("Change Of Flat Rate VAT Business Type ( Requires CSV )", "..//comms_templates/Change_Of_Flat_Rate_VAT_Business_Type.csv", "Upload Change of Flat Rate")
