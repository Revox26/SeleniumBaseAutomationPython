from seleniumbase import BaseCase


class CompassStarAssignDirectorsPage(BaseCase):
    companies_tab = "//a[contains(.,'Companies')]"
    assign_directors_tab = "//a[contains(.,'Assign Directors')]"
    select_a_supplier = "//a[contains(@class,'label label-primary')]//span[.='Select a supplier']"
    include_other_sectors = "input[name='include_other_sectors']"
    assign_a_director = "//span[contains(.,'Assign a Director')]"
    director_name_search_box = "//input[@id='director-name']"
    click_search_button = "//button[contains(.,'Search')]"
    select_director = "//input[@name='select_director_check']"
    assign_director_to_the_company_button = "//button[contains(.,'Assign Director to the Company')]"
    yes_confirm_assign_director = "//button[contains(.,'Yes')]"
    company_name_text = "//h3[contains(.,'Company name:')]//strong"
    search_certified = "//button[.='Search ']"

    def navigate_to_assign_directors_tab(self):
        with open("first_name.txt", "r") as file:
            first_name = file.read().strip()
        with open("last_name.txt", "r") as file:
            last_name = file.read().strip()
        self.click(self.companies_tab)
        self.click(self.assign_directors_tab)
        self.click(self.select_a_supplier)

        if not self.is_element_present(self.assign_a_director):
            self.click(self.include_other_sectors)
            self.click(self.search_certified)

        self.click(self.assign_a_director)

        self.type(self.director_name_search_box, first_name + " " + last_name)
        self.click(self.click_search_button)
        self.click(self.select_director)
        self.click(self.assign_director_to_the_company_button)
        self.click(self.yes_confirm_assign_director)
        self.assert_element(self.company_name_text)

        get_company_name_text = self.get_text_content(self.company_name_text)

        with open("director_company.txt", "w") as file:
            file.write(get_company_name_text)
