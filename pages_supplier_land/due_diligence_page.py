import time

from seleniumbase import BaseCase


class SupplierLandInitialCheckPage(BaseCase):
    _due_diligence = "//a[contains(text(),'Due Diligence')]"
    _initial_check = "//a[contains(text(),'Initial Check')]"
    _regular_check = "//a[contains(text(),'Regular Check')]"
    _idd_search_box = "//input[@placeholder='Search for Client Name, Company Name, Company Registration or VAT Number']"
    _idd_search_button = "//button[starts-with(@class,'btn btn-success initial-search-button')]"
    _view_initial_due_diligence = "//a[starts-with(text(),'Initial Due Diligence')]"
    _idd_supplier_name = "//a[starts-with(@class,'link_1')]"

    _dd_next_button = "//button[.='Next']"
    _dd_pass_button = "//button[.='Pass']"
    _dd_yes_pass_button = "//button[.='Yes, pass this supplier']"
    _growl_idd_successfully_passed = "//div[.='Initial due diligence has Passed successfully.']"
    _growl_rdd_successfully_passed = "//div[.='Regular due diligence has Passed successfully and Job has been successfully mark done.']"

    _rdd_select_a_client = "//input[@aria-controls='vs2__listbox']"
    _rdd_select_a_sample_size = "//input[@placeholder='Please select a sample size']"
    _rdd_create_a_job_button = "//button[contains(.,'Create Job')]"
    _rd_search_for_company_name_to_add = "//input[@placeholder='Search for Company Name, Company Registration or VAT Number']"
    _rdd_search_button = "//button[contains(.,'Search')]"
    _rdd_select_button = "//button[contains(.,'Select')]"
    _rdd_yes_select_button = "//button[contains(@class,'btn btn-success margin-left-sssm btnYes')]"
    _rdd_search_job_textbox = "//input[@placeholder='Search using a company name/number, cycle name or Job ID']"
    _view_regular_due_diligence = "//a[contains(.,'Regular Due Diligence')]"
    _view = "//a[.='View Companies']"
    _rdd_company_details = "//a[contains(.,'Ltd')]"
    current_job_text = "//td[@nowrap='nowrap']"

    def navigate_to_initial_check(self):
        self.click(self._due_diligence)
        self.click(self._initial_check)

    def navigate_to_regular_check(self):
        self.click(self._due_diligence)
        self.click(self._regular_check)

    def pass_the_supplier_to_idd(self):
        supplier_name_text = self.var1
        self.type(self._idd_search_box, supplier_name_text)
        self.click(self._idd_search_button)
        time.sleep(1)

        while True:
            get_supplier_name_text = self.get_text_content(self._idd_supplier_name)
            if get_supplier_name_text == supplier_name_text:
                self.click(self._view_initial_due_diligence)
                break

        self.click(self._dd_next_button, timeout=60)
        self.click(self._dd_pass_button, timeout=60)
        self.click(self._dd_yes_pass_button, timeout=60)
        self.assert_element(self._growl_idd_successfully_passed, timeout=60)

    def pass_the_supplier_to_rdd(self):
        with open("..//data//intermediary.txt", "r") as file:
            intermediary_text = file.read().strip()
        self.type(self._rdd_select_a_client, intermediary_text + "\n", timeout=60)
        self.type(self._rdd_select_a_sample_size, "Select a supplier\n")
        self.wait_for_element_clickable(self._rdd_create_a_job_button, timeout=60)
        self.click(self._rdd_create_a_job_button)
        self.type(self._rd_search_for_company_name_to_add, self.var1)
        self.click(self._rdd_search_button)
        self.click(self._rdd_select_button)
        self.click(self._rdd_yes_select_button)
        time.sleep(2)
        self.refresh_page()
        while True:
            get_job_name_text = self.get_text_content(self.current_job_text)
            if intermediary_text == get_job_name_text:
                self.click(self._view)
                break
        self.click(self._view_regular_due_diligence)
        self.click(self._dd_next_button, timeout=60)
        self.click(self._dd_pass_button, timeout=60)
        self.click(self._dd_yes_pass_button, timeout=60)
        self.assert_element(self._growl_rdd_successfully_passed)
