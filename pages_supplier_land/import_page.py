from seleniumbase import BaseCase


class SupplierLandImportPage(BaseCase):
    _import = "(//div[contains(.,'Import')])[6]"
    _mass_idd_update = "//span[contains(text(),'Mass')]"
    _enroll_idd = "//a[.='Enroll IDD']"
    _withdraw_idd = "//a[.='Withdraw IDD']"
    _select_excel_file = "//input[@class='custom-input custom-file-upload-mass-hidden']"
    import_button_for_withdraw_enroll = "//button[contains(.,'Import')]"
    i_agree_that_these_are_all_correct = "//input[@id='agree']"
    proceed_and_update = "//button[contains(text(),'Proceed &')]"
    successfully_withdraw_alert = "//div[@class='alert alert-success alert-white rounded fade in']"

    def navigate_to_enroll_idd(self):
        self.click(self._import)
        self.hover_and_click(self._mass_idd_update, self._enroll_idd)

    def proceed_to_enroll_idd(self, template_path):
        self.choose_file(self._select_excel_file, template_path)

    def navigate_to_withdraw_idd(self):
        self.click(self._import)
        self.hover_and_click(self._mass_idd_update, self._withdraw_idd)

    def proceed_to_withdraw_idd(self):
        self.choose_file(self._select_excel_file, "..//withdraw_enroll_template/withdraw-dd.csv")
        self.click(self.import_button_for_withdraw_enroll)
        self.click(self.i_agree_that_these_are_all_correct)
        self.click(self.proceed_and_update)
        # self.assert_element(self.successfully_withdraw_alert)
