from seleniumbase import BaseCase


class DirectorDocumentationPage(BaseCase):
    select_id_1 = "//select[@id='document-id-0']"
    select_id_2 = "//select[@id='document-id-1']"
    select_id_3 = "//select[@id='document-id-2']"

    input_id_1 = "(// input[@ type='file'])[1]"
    input_id_2 = "(// input[@ type='file'])[2]"
    input_id_3 = "(// input[@ type='file'])[3]"

    upload_and_finish = "//button[@id='save']"
    upload_and_finish2 = "#submit-myapplication"

    proceed_anyway = "//button[@id='proceed-anyway']"

    def director_documentation_page(self):
        self.select_option_by_text(self.select_id_1, "Pag Ibig ID")
        self.choose_file(self.input_id_1, "..//director_id's/Pag-ibig.png")

        self.select_option_by_text(self.select_id_2, "(NBI) Clearance")
        self.choose_file(self.input_id_2, "..//director_id's/NBI-ID.jpg")

        # self.select_option_by_text(self.select_id_3, "PhilHealth ID")
        # self.choose_file(self.input_id_3, "..//director_id's/Philhealth-ID.jpg")

        if self.is_element_present(self.upload_and_finish):
            self.click(self.upload_and_finish)
            if self.is_element_present(self.proceed_anyway):
                self.click(self.proceed_anyway)

        else:
            self.click(self.upload_and_finish2)
            self.get_new_driver()
