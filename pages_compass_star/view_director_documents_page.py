from seleniumbase import BaseCase


class CompassStarViewDocumentsPage(BaseCase):
    company_name_label = "//h3[contains(.,'Company name:')]"
    accept_id = "//i[@class='fa fa-check-square-o']"
    yes_accept_id = "//button[contains(text(),'Yes')]"
    set_to_accepted = "//input[contains(@value,'Accepted')]"
    set_to_offered = "//input[@value='Offered']"
    yes_accept_to_certified = "//button[@id='certified-button-yes']"
    update_application = "//button[contains(.,'Update Application')]"

    def accept_id_and_set_to_accepted(self):
        self.assert_element(self.company_name_label)
        self.click(self.accept_id)
        self.click(self.yes_accept_id)
        self.click(self.accept_id)
        self.click(self.yes_accept_id)
        self.click(self.set_to_accepted)
        self.click(self.update_application)
        self.click(self.yes_accept_to_certified)


    def set_status_to_offered(self):
        self.click(self.set_to_offered)
        self.click(self.update_application)
