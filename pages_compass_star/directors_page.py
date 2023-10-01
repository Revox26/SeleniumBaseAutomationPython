from seleniumbase import BaseCase


class CompassStarDirectorPage(BaseCase):
    search_textbox = "//input[@placeholder='Search...']"
    search_button = "//button[@id='btn-trading-scheme-form']"
    view_director_documents = "//i[@title='View Documents']"

    def view_documents(self):
        with open("email.txt", "r") as file:
            email = file.read().strip()

        self.type(self.search_textbox, email)
        self.click(self.search_button)
        self.click(self.view_director_documents)
