from seleniumbase import BaseCase


class CompassStarCommunicationsTabPage(BaseCase):
    communications_tab = "//a[contains(.,'Communications')]"
    select_template = "//select[@id='template']"
    input_comms_note = "//textarea[@id='comment']"
    _upload_csv_file = "//input[@id='csv-upload']"
    send_to_communications_queue = "//button[@id='send-comms-queue']"

    def navigate_to_communications_tab(self):
        self.click(self.communications_tab)

    def __upload_template__(self, template_name, note, template_path):
        self.select_option_by_text(self.select_template, template_name)
        self.type(self.input_comms_note, note)
        self.choose_file(self._upload_csv_file, template_path)
        self.click(self.send_to_communications_queue)

    def upload_vat_return_template(self):
        self.__upload_template__("Vat Return ( Requires CSV )", "Upload Vat Return",
                                 "..//comms_templates/Vat_Return.csv")

    def upload_invoice_approval_template(self):
        self.__upload_template__("Invoice Approval ( Requires CSV )", "Upload Invoice Approval",
                                 "..//comms_templates/Invoice_Approval.csv")

    def upload_funding_request_template(self):
        self.__upload_template__("Funding Request ( Requires CSV )", "Upload Funding Request",
                                 "..//comms_templates/Funding_Request.csv")
