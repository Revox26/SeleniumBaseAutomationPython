from seleniumbase import BaseCase
from seleniumbase import config as sb_config
import pytest
from faker import Faker

class CompassStarInviteDirectorPage(BaseCase):
    invite_director_button = "//a[.='Invite Director']"
    first_name = "//input[@name='first_name']"
    last_name = "//input[@name='last_name']"
    generate_invitation_link = "//button[@id='generate-invitation-link']"
    invitation_link = "//span[@id='inviteUrlLink']"

    def navigate_to_invite_director_page(self):
        self.click(self.invite_director_button)

    def generate_random_name(self):
        fake = Faker()
        random_name = fake.first_name()
        random_last_name = fake.last_name()
        return random_name, random_last_name

    def invite_director_page(self):

        random_name, random_last_name = self.generate_random_name()
        self.type(self.first_name, random_name)
        self.type(self.last_name, random_last_name)
        self.click(self.generate_invitation_link)

        # save the text of first name and last name
        with open("first_name.txt", "w") as file:
            file.write(random_name)
        with open("last_name.txt", "w") as file:
            file.write(random_last_name)
        print("\n First Name: ", random_name, "\n Last Name: ", random_last_name)

    def get_invitation_link(self):
        director_invitation_link = self.get_text_content(self.invitation_link)
        return director_invitation_link

    def open_invitation_link(self, invitation_link):
        self.get_new_driver()
        self.open(invitation_link)
