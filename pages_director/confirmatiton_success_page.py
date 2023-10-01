from seleniumbase import BaseCase


class DirectorConfirmationPage(BaseCase):
    thank_you_for_your_application = "//h3[contains(text(),'Thank you for your application.')]"

    def director_confirmation_page(self):
        self.assert_element(self.thank_you_for_your_application)
        self.get_new_driver()
