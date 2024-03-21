import pandas as pd
from seleniumbase import BaseCase

class WithdrawAndEnrollIddExcelSheet(BaseCase):
    def input_company_number_in_withraw_enroll_idd_template(self, template_path, csv_company_name, csv_company_number, csv_intermediary_name):
        df = pd.read_csv(template_path)

        company_name_row_index = 0  # Replace with the desired row index
        company_number_row_index = 0  # Replace with the desired row index
        intermediary_name_row_index = 0  # Replace with the desired row index

        # Update Company Name
        column_name = 'Company Name'
        new_value = csv_company_name
        df.at[company_name_row_index, column_name] = new_value

        # Update Company Number
        column_name = 'Company Number'
        new_value = int(csv_company_number)  # Explicitly cast to str
        # new_string_value, new_int_value = str(existing_value) + " " + str(csv_company_number), int(existing_value)
        df.at[company_number_row_index, column_name] = new_value

        # Update Intermediary Name
        column_name = 'Intermediary Name'
        new_value = csv_intermediary_name
        df.at[intermediary_name_row_index, column_name] = new_value

        # Save the modified DataFrame back to the same CSV file
        df.to_csv(template_path, index=False)  # Use the same file path

    def input_company_data_in_enroll_withdraw_csv(self):
        with open("..//data//intermediary.txt", "r") as file:
            intermediary_name = file.read().strip()

        with open("..//data//director_company.txt", "r") as file:
            company_name = file.read().strip()

        template_path = "..//withdraw_enroll_template/withdraw-dd.csv"

        self.input_company_number_in_withraw_enroll_idd_template(template_path, company_name, self.var1, intermediary_name)
