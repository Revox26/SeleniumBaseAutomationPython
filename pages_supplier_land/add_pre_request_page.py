import random
import time

from seleniumbase import BaseCase
from configuration_files.config_reader import Readconfig


class SupplierLandAddNewPreRequestPage(BaseCase):
    _new_suppliers = "//a[contains(.,'New Suppliers')]"
    _pre_request = "//span[contains(.,'Pre-Request')]"
    _add_pre_request = "(//a[.='Add Pre-Request'])[1]"
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
    _t3_tick_box = "//label[@for='t3']"
    _add_pre_request_modal = "//div[@class='modal-header no-border']"
    _data_not_found = "//td[contains(.,'Data not found')]"

    def navigate_to_pre_request(self):
        self.click(self._new_suppliers)
        self.sleep(1)
        self.hover(self._pre_request)
        self.click(self._add_pre_request)
        self.assert_element(self._add_pre_request_heading, timeout=60)

    def add_pre_request_fields(self):
        client_selected_dropdown = self.var3
        industry_selected_dropdown = self.var1

        list_of_client_in_dropdown = {
            "random": "Random",
            "321_corporate_payroll_ltd": "321 Corporate Payroll Ltd",
            "321_pay_ltd": "321 Pay Ltd",
            "4th_option_ltd": "4th Option Ltd",
            "adelta_staffing_ltd": "Adelta Staffing Ltd",
            "ado_pay_ltd": "ADO Pay Ltd",
            "akin_resources_ltd": "Akin Resources Ltd",
            "apollo_staffing_ltd": "Apollo Staffing Ltd",
            "appp_solutions_ltd": "Appp Solutions Ltd",
            "brooklands_project_management_limited": "BROOKLANDS PROJECT MANAGEMENT LIMITED",
            "business2_ltd": "Business2 Ltd",
            "cerberus_staffing_ltd": "Cerberus Staffing Ltd",
            "charon_solutions_ltd": "Charon Solutions Ltd",
            "hand_technology_ltd": "Hand Technology ltd",
            "wageHub_outsourcing_limited": "WageHub Outsourcing Limited",
            "deliverex_ltd": "Deliverex Ltd",
        }
        selected_client = list_of_client_in_dropdown.get(client_selected_dropdown)
        if selected_client:
            self.type(self._client, selected_client + "\n")

        list_of_industry_in_dropdown = {
            "random": "Random",
            "accounts": "Accounts",
            "transport": "Transport",
            "administration": "Administration",
            "advertising": "Advertising",
            "agricultural_services": "Agricultural services",
            "boarding_or_care_of_animals": "Boarding or care of animals",
            "call_centre": "Call Centre",
            "cleaning": "Cleaning",
            "computer_repair_services": "Computer repair services",
            "construction": "Construction",
            "engineering": "Engineering",
            "healthcare": "Healthcare",
            "financial_services": "Financial services",
            "gardening": "Gardening",
            "hospitality": "Hospitality"
        }
        selected_industry = list_of_industry_in_dropdown.get(industry_selected_dropdown)
        if selected_industry:
            self.type(self._industry, selected_industry)
            self.press_keys(self._industry, "\ue015\ue007")

        _client_text = self.get_text_content(self._client_value)
        _industry_text = self.get_text_content(self._industry_value)

        # save the text of first name and last name
        with open("..//data//intermediary.txt", "w") as file:
            file.write(_client_text)
        with open("..//data//industry.txt", "w") as file:
            file.write(_industry_text)
        print("Client Name: ", _client_text)
        print("Industry Name: ", _industry_text)

        if self.is_element_present(self._number_of_suppliers):
            self.type(self._number_of_suppliers, "3")

        self.type(self._pay_type, "Umbrella\n")
        self.click(self._contract_start_date)
        self.click(self._select_contract_start_date)

        if self.is_element_present(self._contract_value):
            self.type(self._contract_value, "200000")
        else:
            self.type(self._yearly_contract_value, "2000000")

        if self.is_element_present(self._number_of_contractors_per_supplier):
            self.type(self._number_of_contractors_per_supplier, "3")

        if self.is_element_present(self._priority):
            self.type(self._priority, "1")

        self.type(self._desired_margin, "3.5")
        self.click(self._add_button)

        if self.is_element_present(self._add_pre_request_modal):
            self.wait_for_element_visible(self._continue_button, timeout=15)
            self.sleep(2)
            if self.is_element_visible(self._link_placeholder):
                self.type(self._link_placeholder, Readconfig.get_bsc_uat_redeem_link(), timeout=60)
                self.click(self._continue_button)
            else:
                self.click(self._continue_button)

    def t3_add_pre_request_fields(self):
        self.click(self._t3_tick_box)
        self.press_keys(self._client, "\ue015\ue007")
        self.press_keys(self._industry, "\ue015\ue007")

        _client_text = self.get_text_content(self._client_value)
        with open("..//data//intermediary.txt", "w") as file:
            file.write(_client_text)

        _industry_text = self.get_text_content(self._industry_value)
        with open("..//data//industry.txt", "w") as file:
            file.write(_industry_text)

        print("Client Name: ", _client_text)
        print("Industry Name: ", _industry_text)

        self.type(self._pay_type, "Umbrella\n")
        self.click(self._contract_start_date)
        self.click(self._select_contract_start_date)
        self.type(self._contract_value, "50000")
        self.type(self._number_of_contractors_per_supplier, "3")
        self.type(self._desired_margin, "3.5")
        self.click(self._add_button)
        self.type(self._link_placeholder, Readconfig.get_bsc_uat_url_t3() + self.var1)
        self.click(self._continue_button)

    def submit_pre_request(self):
        self.wait_for_element_visible(self._pre_request_checkbox, timeout=60)
        time.sleep(1)
        # while True:
        #     self.click(self._pre_request_checkbox)
        #     self.click(self._submit_button)
        #     if self.is_element_present(self._data_not_found):
        #         break
        while True:
            try:
                self.click(self._pre_request_checkbox)
                self.click(self._submit_button)
                if self.is_element_visible(self._data_not_found):
                    break
            except Exception as e:
                break
