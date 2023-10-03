from seleniumbase import BaseCase


class SupplierLandFindCustomerPage(BaseCase):
    _find_customer_proceed = "//button[.='PROCEED']"
    _i_am_interested = "button[class='btn btn-success btn-interested']"
    _customer_close_button = "button[class='btn btn-success']"
    _fcp_supplier_name = "//h4[contains(@class,'bold_light')]//b"
    _director_preferred_value = "(//input[contains(@class,'form-control')])[6]"
    _include_other_industries = "//label[@for='sectorChange']"
    _i_am_interested_disabled = "button[class='btn btn-success btn-interested disabledBtn']"

    def i_want_to_be_a_supplier_and_interested(self):
        process = self.var1
        if process != "old":
            self.clear(self._director_preferred_value)
            self.type(self._director_preferred_value, process)
            self.click(self._find_customer_proceed)
        else:
            self.click(self._find_customer_proceed)

        self.assert_element(self._i_am_interested_disabled)

        if not self.is_element_visible(self._i_am_interested):
            self.click(self._include_other_industries)

        self.click(self._i_am_interested)

        try:
            if self.assert_element(self._customer_close_button):
                self.sleep(1)
                self.click(self._customer_close_button)
        except Exception as e:
            print(e)
