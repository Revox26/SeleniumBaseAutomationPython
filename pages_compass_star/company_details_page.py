from seleniumbase import BaseCase
import random


class CompassStarCompanyDetailsTabPage(BaseCase):
    _vat_reg_no = "//input[@id='vat_reg_no']"
    _auth_code = "//input[@name='auth_code']"
    _update_company_details_button = "//button[contains(.,'Update Company Details')]"

    def input_auth_code_and_vat_reg(self):
        random_vat_reg = random.randint(100000, 999999)
        random_auth_code = random.randint(100000, 999999)

        already_have_vat_reg = self.get_attribute(self._vat_reg_no, "value")
        already_have_auth_code = self.get_attribute(self._auth_code, "value")

        if not already_have_vat_reg:
            self.type(self._vat_reg_no, random_vat_reg)
            print("Vat Reg is empty", "\n New Vat Reg Number: ", random_vat_reg)

        if not already_have_auth_code:
            self.type(self._auth_code, random_auth_code)
            print("Auth Code is empty", "\n New Auth Code: ", random_auth_code)

        if not already_have_vat_reg or not already_have_auth_code:
            self.click(self._update_company_details_button)

        else:
            print("Already have vat reg and auth code")

        print("\n Vat Reg Number: ", already_have_vat_reg)
        print("Auth Code: ", already_have_auth_code)
