from seleniumbase import BaseCase


class CompassStarDirectorPage(BaseCase):
    directors_tab = "//a[.='Directors']"
    search_textbox = "//input[@placeholder='Search...']"
    search_button = "//button[@id='btn-trading-scheme-form']"
    view_director_documents = "//i[@title='View Documents']"

    def navigate_to_directors_page(self):
        self.click(self.directors_tab)

    def view_documents(self):
        with open("..//data//email.txt", "r") as file:
            email = file.read().strip()

        if self.data == "v2":
            self.type(self.search_textbox, self.var1)

        else:
            self.type(self.search_textbox, email)

        self.click(self.search_button)
        self.click(self.view_director_documents)
