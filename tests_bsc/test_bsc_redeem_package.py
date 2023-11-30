import pytest
from pages_bsc.bsc_create_your_account_page import BscCreateYOurAccountPage
from pages_bsc.bsc_open_orders_page import BscOpenOrdersPage
from pages_bsc.bsc_payment_details_page import BscPaymentDetailsPage
from pages_bsc.bsc_redeem_package import BscRedeemPackagePage
from pages_bsc.login_uat_bsc import BscLoginUatPage

from utilities.custom_logging import get_custom_logger
from utilities.loading_bar import updt

logger = get_custom_logger(__name__)


class TestBscRedeemPackage(
    BscRedeemPackagePage,
    BscCreateYOurAccountPage,
    BscPaymentDetailsPage,
    BscLoginUatPage,
    BscOpenOrdersPage
):

    @pytest.mark.run(order=1)
    def test_open_uat_redeem_url(self):
        updt(2, 1)
        logger.info("Opening the UAT redeem URL...")
        self.open_bsc_redeem_package()
        logger.info("Providing the following information...")
        self.provide_following_information()
        logger.info("Creating BSC account...")
        self.create_account_after_redeem()
        self.please_enter_your_card_details_or_pay_with_payPal()
        logger.info("BSC payment has been processed successfully.")

    @pytest.mark.run(order=2)
    def test_login_bsc_uat_url(self):
        updt(2, 2)
        logger.info("Logging in to BSC UAT URL as Jdctest...")
        self.login_bsc_uat_url()
        self.manage_orders()
        self.transfer_company_tab()
        if self.var2 == "gmail":
            self.transmit_gmail_credentials()
        elif self.var2 == "outlook":
            self.transmit_outlook_credentials()
        logger.info("BSC company and email transmitted successfully")
