from seleniumbase import BaseCase


class BscPaymentDetailsPage(BaseCase):
    bsc_payment_check_box1 = "div[class='p-3 w-100 border rounded mt-4'] label[for='terms']"
    bsc_payment_check_box2 = "div[class='p-3 mt-4 border rounded w-100'] label[for='terms']"
    bsc_complete_order = "//button[.='Complete Order']"
    bsc_card_number = "//input[@placeholder='1234 1234 1234 1234']"
    card_expiry_date = "input[placeholder='MM / YY']"
    cvc = "//input[@placeholder='CVC']"
    post_code = "//input[contains(@placeholder,'Post Code')]"
    pay_now_with_stripe = "//button[.='Pay now with Stripe']"
    payment_label = "//h4[.='Please enter your card details or pay with PayPal']"
    your_order_is_confirmed = "//div[.='Your order is confirmed!']"

    def bsc_payment_details(self):
        self.js_click(self.bsc_payment_check_box1)
        self.js_click(self.bsc_payment_check_box2)
        self.sleep(1)
        self.click(self.bsc_complete_order)
        self.assert_element(self.your_order_is_confirmed, timeout=60)
        self.switch_to_window(0)

    def please_enter_your_card_details_or_pay_with_payPal(self):
        self.assert_element(self.payment_label)
        self.slow_scroll_to_element(self.payment_label)
        self.switch_to_frame("iframe")
        self.type(self.bsc_card_number, "4242424242424242")

        self.switch_to_parent_frame()
        self.switch_to_frame("//iframe[@title='Secure expiration date input frame']")
        self.type(self.card_expiry_date, "12 24")

        self.switch_to_parent_frame()
        self.switch_to_frame("//iframe[@title='Secure CVC input frame']")
        self.type(self.cvc, "123")

        self.switch_to_parent_frame()
        self.type(self.post_code, "W1U 3EU")

        self.js_click(self.bsc_payment_check_box1)
        self.js_click(self.bsc_payment_check_box2)

        self.wait_for_element_clickable(self.pay_now_with_stripe)
        self.sleep(2)
        self.click(self.pay_now_with_stripe)
        self.assert_element(self.your_order_is_confirmed, timeout=30)
