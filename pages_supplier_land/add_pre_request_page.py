import random
from seleniumbase import BaseCase

from configuration_files.config_reader import Readconfig


class SupplierLandAddNewPreRequestPage(BaseCase):
    _new_suppliers = "//a[contains(.,'New Suppliers')]"
    _pre_request = "//span[contains(.,'Pre-Request')]"
    _add_pre_request = "//a[.='Add Pre-Request']"
    _add_pre_request_heading = "//h4[.='Add Pre-Request']"
    _logo = "//img[@alt='SupplierLand - Transforming Supply Chain Management']"
    _client = "//input[@placeholder='Please select a client']"
    _client_value = "(//span[@class='vs__selected']//div)[1]"
    _industry = "//input[@placeholder='Please select industry']"
    _industry_value = "(//span[@class='vs__selected']//div)[2]"
    _number_of_suppliers = "//input[@name='number_of_pre_request']"
    _pay_type = "//input[@placeholder='Pay Type']"
    _contract_start_date = "//input[@placeholder='DD-MM-YYYY']"
    _select_contract_start_date = "//span[normalize-space()='19']"
    _yearly_contract_value = "//input[@placeholder='Enter Yearly Contract Value']"
    _contract_value = "//input[@placeholder='Enter Contract Value']"
    _number_of_contractors_per_supplier = "//input[@placeholder='Enter Number of contractors per supplier']"
    _priority = "//input[@placeholder='Enter Priority']"
    _desired_margin = "//input[@placeholder='Enter Desired Margin']"
    _add_button = "//button[contains(.,'Add')]"
    _link_placeholder = "//input[@placeholder='Copy and Paste BSC link here']"
    _continue_button = "//button[@type='submit']"
    _pre_request_checkbox = "//label[contains(@class,'no-margin checkboxLabelNoText')]"
    _submit_button = "//button[contains(.,'Submit')]"

    def navigate_to_pre_request(self):
        self.click(self._new_suppliers)
        self.sleep(1)
        self.hover(self._pre_request)
        self.click(self._add_pre_request)
        self.assert_element(self._add_pre_request_heading, timeout=60)

    def add_pre_request_fields(self):
        client_dropdown_list = ['Apollo', '321 Pay Ltd', '4th Option Ltd', 'Adelta Staffing Ltd']
        industry_dropdown_list = ['Accounts', 'Administration', 'Advertising', 'Boarding or care of animals',
                                  "Call Centre", "Cleaning"]
        random_list = self.var1

        if random_list == "random":
            self.type(self._client, random.choice(client_dropdown_list) + "\n")
            self.type(self._industry, random.choice(industry_dropdown_list))
            self.press_keys(self._industry, "\ue015\ue007")
        else:
            self.type(self._client, "Apollo \n")
            self.type(self._industry, "transport")
            self.press_keys(self._industry, "\ue015\ue007")

        _client_text = self.get_text_content(self._client_value)
        _industry_text = self.get_text_content(self._industry_value)

        # save the text of first name and last name
        with open("..//data//intermediary.txt", "w") as file:
            file.write(_client_text)
        with open("..//data//industry.txt", "w") as file:
            file.write(_industry_text)
        print("\n Client Name: ", _client_text, "\n Industry Name: ", _industry_text)

        if self.is_element_present(self._number_of_suppliers):
            self.type(self._number_of_suppliers, "3")

        self.type(self._pay_type, "Umbrella\n")
        self.click(self._contract_start_date)
        self.click(self._select_contract_start_date)

        if self.is_element_present(self._contract_value):
            self.type(self._contract_value, "2000000")
        else:
            self.type(self._yearly_contract_value, "2000000")

        if self.is_element_present(self._number_of_contractors_per_supplier):
            self.type(self._number_of_contractors_per_supplier, "3")

        if self.is_element_present(self._priority):
            self.type(self._priority, "1")

        self.type(self._desired_margin, "3.5")
        self.click(self._add_button)
        self.sleep(3)

        if self.is_element_present(self._link_placeholder):
            self.type(self._link_placeholder, Readconfig.get_bsc_uat_redeem_link())
            self.click(self._continue_button)

    def submit_pre_request(self):
        self.wait_for_element_visible(self._pre_request_checkbox, timeout=60)
        self.click(self._pre_request_checkbox)
        self.click(self._submit_button)
        self.sleep(10)
