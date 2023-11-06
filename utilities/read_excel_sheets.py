import pandas as pd


class ReadCommsTemplate:
    def input_company_number_in_template(self, template_path, csv_company_number):
        df = pd.read_csv(template_path, dtype={'CompanyNumber': str})

        row_index = 0  # Replace with the desired row index
        column_name = 'CompanyNumber'  # Replace with the column name
        new_value = csv_company_number  # This should remain a string
        df.at[row_index, column_name] = new_value

        # Save the modified DataFrame back to the same CSV file
        df.to_csv(template_path, index=False)  # Use the same file path

    def input_company_number_in_vat_return_csv(self, csv_company_number):
        template_path = "..//comms_templates//Vat_Return.csv"
        self.input_company_number_in_template(template_path, csv_company_number)

    def input_company_number_in_invoice_approval_csv(self, csv_company_number):
        template_path = "..//comms_templates//Invoice_Approval.csv"
        self.input_company_number_in_template(template_path, csv_company_number)

    def input_company_number_in_funding_request_csv(self, csv_company_number):
        template_path = "..//comms_templates//Funding_Request.csv"
        self.input_company_number_in_template(template_path, csv_company_number)

    def input_company_number_in_change_of_flat_rate_csv(self, csv_company_number):
        template_path = "..//comms_templates//Change_Of_Flat_Rate_VAT_Business_Type.csv"
        self.input_company_number_in_template(template_path, csv_company_number)
