import pytest
from pages_bsc.bsc_create_your_account_page import BscCreateYOurAccountPage
from pages_bsc.bsc_open_orders_page import BscOpenOrdersPage
from pages_bsc.bsc_payment_details_page import BscPaymentDetailsPage
from pages_bsc.bsc_redeem_package import BscRedeemPackagePage
from pages_bsc.login_uat_bsc import BscLoginUatPage


class TestBscRedeemPackage(
    BscRedeemPackagePage,
    BscCreateYOurAccountPage,
    BscPaymentDetailsPage,
    BscLoginUatPage,
    BscOpenOrdersPage
):

    @pytest.mark.run(order=1)
    def test_open_uat_redeem_url(self):
        self.open_bsc_redeem_package()
        self.provide_following_information()
        self.create_account_after_redeem()
        self.please_enter_your_card_details_or_pay_with_payPal()

    @pytest.mark.run(order=2)
    def test_login_bsc_uat_url(self):
        self.login_bsc_uat_url()
        self.manage_orders()
        self.transfer_company_tab()
        self.email_credentials_tab()
