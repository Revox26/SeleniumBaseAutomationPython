import pytest

from pages_destibrom.amenities_page import DestibromAmenitiesPage
from pages_destibrom.categories_page import DestibromCategoriesPage
from pages_destibrom.content_burger import DestibromContentBurger
from pages_destibrom.dashboard_page import DestibromDashboardPage
from pages_destibrom.locations_page import DestibromLocationPage
from pages_destibrom.login_page import DestiBromLoginPage
from pages_destibrom.new_and_events_page import DestibromNewsAndEventsPage
from pages_destibrom.sponsored_ads_page import DestibromSponsoredAdsPage


class DestiBromTesting(
    DestibromAmenitiesPage,
    DestibromCategoriesPage,
    DestibromContentBurger,
    DestibromDashboardPage,
    DestibromLocationPage,
    DestiBromLoginPage,
    DestibromNewsAndEventsPage,
    DestibromSponsoredAdsPage

):

    @pytest.mark.run(order=1)
    def test_login(self):
        self.open_destibrom_page()
        self.navigate_to_login_menu()
        self.destibrom_login_as_super_admin()
        self.assert_element(DestibromDashboardPage.dashboard_label)
        self.navigate_to_locations_menu()
        self.navigate_to_categories_menu()
        self.navigate_to_amenities_menu()
        self.navigate_to_sponsored_ads_menu()
        self.navigate_to_news_and_events_menu()
