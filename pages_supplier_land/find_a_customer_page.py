from seleniumbase import BaseCase


class SupplierLandFindCustomerPage(BaseCase):
    _find_customer_proceed = "//button[.='PROCEED']"
    _i_am_interested = "button[class='btn btn-success btn-interested']"
    _customer_close_button = "button[class='btn btn-success']"
    _fcp_supplier_name = "//h4[contains(@class,'bold_light')]//b"

    def i_want_to_be_a_supplier_and_interested(self):
        self.click(self._find_customer_proceed)
        self.click(self._i_am_interested)

        try:
            if self.assert_element(self._fcp_supplier_name):
                self.click(self._customer_close_button)
        except Exception as e:
            print(e)
