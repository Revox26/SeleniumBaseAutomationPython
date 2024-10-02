import subprocess
import threading
import tkinter
import customtkinter
from art import *


class QAApp:
    def __init__(self):
        def colored_text(text, color_code):
            return f"\033[{color_code}m{text}\033[0m"

        ascii_art = text2art(" Welcome to \n Automation", "slant")
        colored_ascii_art = colored_text(ascii_art, "35;1")
        self.app = customtkinter.CTk()
        self.app.geometry("600x900")
        self.app.title("QA Team Automation")
        print(colored_ascii_art)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.frame = self.create_frame()
        self.create_module_selection()
        self.create_dropdowns()
        self.create_test_options()
        self.create_buttons()
        self.registration_to_ready_additional_data_options()
        self.accepted_to_ready_additional_data_options()
        self.transfer_a_supplier_additional_data()
        self.pre_request_and_confirmed_additional_data()
        self.pass_to_due_diligence_additional_data()
        self.withdraw_idd_additional_data()
        self.upload_communications_template_additional_data()
        self.app.bind("<Configure>", self.handle_drag_to_other_monitor)

    def handle_drag_to_other_monitor(self, event):
        try:
            process_selection = self.process_dropdown.get()
            self.show_additional_data_for_process(process_selection)
        except Exception as e:
            pass

    def create_frame(self):
        frame = customtkinter.CTkFrame(master=self.app)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        return frame

    def registration_to_ready_additional_data_options(self):
        self.yearly_contract_frame = customtkinter.CTkFrame(master=self.frame)
        self.yearly_contract_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        # Add a text entry for 'Director Preferred Value'
        self.director_value_label = customtkinter.CTkLabel(master=self.yearly_contract_frame, justify=customtkinter.LEFT, text="Director Preferred Value", font=("Arial", 15))
        self.director_value_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.director_preferred_value_entry = customtkinter.CTkEntry(master=self.yearly_contract_frame, width=300)
        self.director_preferred_value_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.route_type_label = customtkinter.CTkLabel(master=self.yearly_contract_frame, justify=customtkinter.LEFT, text="Route Type", font=("Arial", 15))
        self.route_type_label.grid(row=2, column=0, pady=(5, 0), padx=10, sticky="w")

        self.route_type_radio_frame = customtkinter.CTkFrame(master=self.yearly_contract_frame)
        self.route_type_radio_frame.grid(row=3, column=0, columnspan=2, pady=(5, 5), padx=10, sticky="w")

        # Use tkinter IntVar as the variable
        self.route_type_var = tkinter.IntVar(value=2)  # Default selection

        radio_buttons_info = [("1.6", 1), ("1.7", 2), ("1.8", 3)]
        for i, (text, value) in enumerate(radio_buttons_info):
            button = customtkinter.CTkRadioButton(master=self.route_type_radio_frame, text=text, variable=self.route_type_var, value=value)
            button.grid(row=0, column=i)

        # self.yearly_contract_frame.grid_remove()  # hide by default

    def accepted_to_ready_additional_data_options(self):
        self.director_email_label = customtkinter.CTkLabel(master=self.yearly_contract_frame, justify=customtkinter.LEFT, text="Director Email", font=("Arial", 15))
        self.director_email_label.grid(row=5, column=0, pady=(5, 0), padx=10, sticky="w")

        self.director_email_entry = customtkinter.CTkEntry(master=self.yearly_contract_frame, width=300)
        self.director_email_entry.grid(row=6, column=0, pady=(5, 5), padx=10, sticky="nsew")

    def withdraw_idd_additional_data(self):
        self.withdraw_idd_frame = customtkinter.CTkFrame(master=self.frame)
        self.withdraw_idd_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        # Add a text entry for 'Director Preferred Value'
        self.company_number_label = customtkinter.CTkLabel(master=self.withdraw_idd_frame, justify=customtkinter.LEFT, text="Company Number", font=("Arial", 15))
        self.company_number_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.withdraw_idd_company_name_entry = customtkinter.CTkEntry(master=self.withdraw_idd_frame, width=300)
        self.withdraw_idd_company_name_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.withdraw_idd_frame.grid_remove()

    def pass_to_due_diligence_additional_data(self):
        self.pass_to_due_diligence_frame = customtkinter.CTkFrame(master=self.frame)
        self.pass_to_due_diligence_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        # Add a text entry for 'Director Preferred Value'
        self.company_name_label = customtkinter.CTkLabel(master=self.pass_to_due_diligence_frame, justify=customtkinter.LEFT, text="Company Name", font=("Arial", 15))
        self.company_name_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.pass_to_due_diligence_company_name_entry = customtkinter.CTkEntry(master=self.pass_to_due_diligence_frame, width=300)
        self.pass_to_due_diligence_company_name_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.pass_to_due_diligence_frame.grid_remove()

    def transfer_a_supplier_additional_data(self):
        self.transfer_a_supplier_frame = customtkinter.CTkFrame(master=self.frame)
        self.transfer_a_supplier_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        # Add a text entry for 'Director Preferred Value'
        self.transfer_company_name_label = customtkinter.CTkLabel(master=self.transfer_a_supplier_frame, justify=customtkinter.LEFT, text="Company Name", font=("Arial", 15))
        self.transfer_company_name_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.transfer_company_name_entry = customtkinter.CTkEntry(master=self.transfer_a_supplier_frame, width=300)
        self.transfer_company_name_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.transfer_a_supplier_frame.grid_remove()

    def show_additional_data_for_process(self, process_selection):
        if process_selection in ["Registration to ready", "Mobile registration to Ready", "Accepted to ready"]:
            self.yearly_contract_frame.grid()
        else:
            self.yearly_contract_frame.grid_remove()
            self.route_type_var.set(0)
            self.director_preferred_value_entry.delete(0, 'end')

        if process_selection == "Accepted to ready":
            self.director_email_label.grid()
            self.director_email_entry.grid()
        else:
            self.director_email_label.grid_remove()
            self.director_email_entry.delete(0, 'end')
            self.director_email_entry.grid_remove()

        if process_selection == "Transfer a supplier":
            self.transfer_a_supplier_frame.grid()
        else:
            self.transfer_a_supplier_frame.grid_remove()
            self.transfer_company_name_entry.delete(0, 'end')

        if process_selection in ["Add provisional pre-request", "Add confirmed pre-request"]:
            self.pre_request_and_confirmed_frame.grid()
        else:
            self.pre_request_and_confirmed_frame.grid_remove()
            self.select_industry_dropdown.set("Select Industry")
            self.select_client_dropdown.set("Select Client")
            self.priority_entry.delete(0, 'end')

        if process_selection == "Pass to due diligence":
            self.pass_to_due_diligence_frame.grid()
        else:
            self.pass_to_due_diligence_frame.grid_remove()
            self.pass_to_due_diligence_company_name_entry.delete(0, 'end')

        if process_selection == "Withdraw IDD":
            self.withdraw_idd_frame.grid()
        else:
            self.withdraw_idd_frame.grid_remove()
            self.withdraw_idd_company_name_entry.delete(0, 'end')

        if process_selection == "Upload communications template":
            self.upload_communications_template_frame.grid()
        else:
            self.upload_communications_template_frame.grid_remove()
            self.communication_company_number_entry.delete(0, 'end')
            self.select_communication_template_dropdown.set("Select template")

    def show_additional_data_pre_request_and_confirmed(self, process_selection):
        if process_selection in ["Registration to ready", "Mobile registration to Ready"]:
            self.yearly_contract_frame.grid()
        else:
            self.yearly_contract_frame.grid_remove()
            self.route_type_var.set(0)
            self.director_preferred_value_entry.delete(0, 'end')

        if process_selection == "Transfer a supplier":
            self.transfer_a_supplier_frame.grid()
        else:
            self.transfer_a_supplier_frame.grid_remove()

    def create_module_selection(self):
        module_options = ["CSL PROCESS", "SL PROCESS", "BSC PROCESS", "DESTINATION X PROCESS"]
        self.segmented_button = customtkinter.CTkSegmentedButton(master=self.frame, values=module_options, command=self.update_label)
        self.segmented_button.grid(row=1, column=0, columnspan=2, pady=30, padx=30)

        self.module_label = customtkinter.CTkLabel(master=self.frame, justify=customtkinter.LEFT, text="Select a module", font=("Arial", 30))
        self.module_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10)

    def upload_communications_template_additional_data(self):
        self.upload_communications_template_frame = customtkinter.CTkFrame(master=self.frame)
        self.upload_communications_template_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        self.upload_communications_template_frame.grid_remove()

        self.communication_company_number_label = customtkinter.CTkLabel(master=self.upload_communications_template_frame, justify=customtkinter.LEFT, text="Company Number", font=("Arial", 15))
        self.communication_company_number_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.communication_company_number_entry = customtkinter.CTkEntry(master=self.upload_communications_template_frame, width=332)
        self.communication_company_number_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.communication_template_label = customtkinter.CTkLabel(master=self.upload_communications_template_frame, justify=customtkinter.LEFT, text="Communcation Template", font=("Arial", 15))
        self.communication_template_label.grid(row=2, column=0, pady=(5, 0), padx=10, sticky="w")

        communication_template_values = [
            "Select All",
            "Vat Return",
            "Invoice Approval",
            "Funding Request",
            "Change Of Flat Rate VAT",
            "Confirmation of Duties"

        ]

        self.select_communication_template_dropdown = customtkinter.CTkOptionMenu(self.upload_communications_template_frame, values=communication_template_values, width=332, height=40, font=("Arial", 12))
        self.select_communication_template_dropdown.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        self.select_communication_template_dropdown.set("Select template")

    def pre_request_and_confirmed_additional_data(self):
        self.pre_request_and_confirmed_frame = customtkinter.CTkFrame(master=self.frame)
        self.pre_request_and_confirmed_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        self.pre_request_and_confirmed_frame.grid_remove()

        self.select_client_label = customtkinter.CTkLabel(master=self.pre_request_and_confirmed_frame, justify=customtkinter.LEFT, text="Client", font=("Arial", 15))
        self.select_client_label.grid(row=1, column=0, pady=(5, 0), padx=10, sticky="w")

        client_values = [
            "Random",
            "321 Corporate Payroll Ltd",
            "321 Pay Ltd",
            "4th Option Ltd",
            "Adelta Staffing Ltd",
            "ADO Pay Ltd",
            "Akin Resources Ltd",
            "Apollo Staffing Ltd",
            "Appp Solutions Ltd",
            "BROOKLANDS PROJECT MANAGEMENT LIMITED",
            "Business2 Ltd",
            "Cerberus Staffing Ltd",
            "Charon Solutions Ltd",
            "WageHub Outsourcing Limited",
            "Deliverex Ltd"

        ]
        self.select_client_dropdown = customtkinter.CTkOptionMenu(self.pre_request_and_confirmed_frame, values=client_values, width=332, height=40, font=("Arial", 12))
        self.select_client_dropdown.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        self.select_client_dropdown.set("Select client")

        self.select_industry_label = customtkinter.CTkLabel(master=self.pre_request_and_confirmed_frame, justify=customtkinter.LEFT, text="Industry", font=("Arial", 15))
        self.select_industry_label.grid(row=3, column=0, pady=(5, 0), padx=10, sticky="w")

        industry_values = [
            "Random",
            "Accounts",
            "Transport",
            "Administration",
            "Advertising",
            "Agricultural services",
            "Boarding or care of animals",
            "Call Centre",
            "Cleaning",
            "Computer repair services",
            "Construction",
            "Engineering",
            "Healthcare",
            "Financial services",
            "Gardening",
            "Hospitality"

        ]

        self.select_industry_dropdown = customtkinter.CTkOptionMenu(self.pre_request_and_confirmed_frame, values=industry_values, width=332, height=40, font=("Arial", 12))
        self.select_industry_dropdown.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.select_industry_dropdown.set("Select industry")

        self.priority_label = customtkinter.CTkLabel(master=self.pre_request_and_confirmed_frame, justify=customtkinter.LEFT, text="Priority", font=("Arial", 15))
        self.priority_label = customtkinter.CTkLabel(master=self.pre_request_and_confirmed_frame, justify=customtkinter.LEFT, text="Priority", font=("Arial", 15))
        self.priority_label.grid(row=5, column=0, pady=(5, 0), padx=10, sticky="w")

        self.priority_entry = customtkinter.CTkEntry(master=self.pre_request_and_confirmed_frame, width=332)
        self.priority_entry.grid(row=6, column=0, pady=(5, 5), padx=10, sticky="nsew")

    def create_dropdowns(self):
        self.instance_dropdown = customtkinter.CTkOptionMenu(self.frame, values=["QA Instance", "V1 Instance", "V2 Instance", "V3 Instance", "V4 Instance", "Replica Instance", "Delta Instance", "Echo Instance"], width=442, height=40, font=("Arial", 25))
        self.instance_dropdown.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        self.instance_dropdown.set("Select instance")

        self.browser_dropdown = customtkinter.CTkOptionMenu(self.frame, values=["Chrome", "Edge", "Firefox"], width=442, height=40, font=("Arial", 25))
        self.browser_dropdown.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.browser_dropdown.set("Chrome")

        self.process_dropdown_options = {
            "CSL Process": ["Registration to ready", "Accepted to ready", "Mobile registration to Ready", "Transfer a supplier", "T3 allocation to ready", "Upload communications template"],
            "SL Process": ["Add provisional pre-request", "Add confirmed pre-request", "Pass to due diligence", "Withdraw IDD"],
            "BSC Process": ["BSC order package"],
            "DestinationX Process": ["Add Categories", "Add Amenity", "Add Sponsored Ads", "Add News and Events", "Send External Link Notification", "Send Location Notification", "Send Category Notification",
                                     "Create New Account (Mobile)", "Forgot Password Non-Existing(Mobile)"]
        }

        self.process_dropdown = customtkinter.CTkOptionMenu(self.frame, values=[], width=442, height=40, font=("Arial", 25), command=self.show_additional_data_for_process)
        self.process_dropdown.set("select a process")

    def create_test_options(self):
        self.test_options_label = customtkinter.CTkLabel(master=self.frame, justify=customtkinter.LEFT, text="Test Options", font=("Arial", 15))
        self.test_options_label.grid(row=6, column=0, columnspan=2, pady=(20, 0), padx=10)

        test_options_value = ["Demo Mode", "Slow Mode", "Generate Report", "Save Screenshot", "Incognito Mode", "Start Maximized", "Dark Mode", "Headless Mode", "Trace/Debug Mode"]
        self.checkbox_frame = customtkinter.CTkFrame(master=self.frame)
        self.checkbox_frame.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        self.checkbox_texts = test_options_value
        self.checkboxes = []
        for i, text in enumerate(self.checkbox_texts):
            checkbox = customtkinter.CTkCheckBox(master=self.checkbox_frame, text=text)
            checkbox.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")
            self.checkboxes.append(checkbox)

    def create_buttons(self):
        self.button_frame = customtkinter.CTkFrame(master=self.frame)
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=10, padx=10)

        self.button_texts = ["Run", "Clear", "Exit"]
        self.buttons = []  # Store buttons in a list for reference
        for i, text in enumerate(self.button_texts):
            button = customtkinter.CTkButton(master=self.button_frame, text=text, width=120, height=50, font=("Arial", 18))
            button.grid(row=0, column=i, padx=10, pady=10)
            self.buttons.append(button)  # Append button to list

        # Bind the 'Run' button to the run_the_test() method
        self.buttons[0].configure(command=lambda: self.run_button_function(self.process_dropdown.get()))
        self.buttons[1].configure(command=self.clear_fields)
        self.buttons[2].configure(command=self.exit_application)

    def update_label(self, option):
        self.module_label.configure(text=option)
        self.show_process_dropdowns(option)
        self.yearly_contract_frame.grid_remove()
        self.transfer_a_supplier_frame.grid_remove()
        self.route_type_var.set(0)
        self.director_preferred_value_entry.delete(0, 'end')

    def show_process_dropdowns(self, option):
        self.process_dropdown.grid_forget()

        # Update and show the relevant process dropdown based on selected option
        if option == "CSL PROCESS":
            self.process_dropdown.set("Select CSL process")
            self.process_dropdown.configure(values=self.process_dropdown_options["CSL Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)
            self.instance_dropdown.grid()

        elif option == "SL PROCESS":
            self.process_dropdown.set("Select SL process")
            self.process_dropdown.configure(values=self.process_dropdown_options["SL Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)
            self.instance_dropdown.grid()

        elif option == "BSC PROCESS":
            self.process_dropdown.set("Select BSC process")
            self.process_dropdown.configure(values=self.process_dropdown_options["BSC Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)
            self.instance_dropdown.grid_remove()

        elif option == "DESTINATION X PROCESS":
            self.process_dropdown.set("Select DestinationX Process")
            self.process_dropdown.configure(values=self.process_dropdown_options["DestinationX Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)
            self.instance_dropdown.set("V1 Instance")

    def run_button_function(self, process_selection):

        # Get selected instance from dropdown
        staging_options = {"--data=qa": "QA Instance", "--data=v1": "V1 Instance", "--data=v2": "V2 Instance", "--data=v3": "V3 Instance", "--data=v4": "V4 Instance", "--data=echo": "Echo Instance", "--data=testing": "Testing Instance", "--data=replica": "Replica Instance"}
        staging_option = next(key for key, value in staging_options.items() if value == self.instance_dropdown.get())

        # Get selected browser from dropdown
        browser_options = {"--chrome": "Chrome", "--edge": "Edge", "--firefox": "Firefox"}
        browser_option = next(key for key, value in browser_options.items() if value == self.browser_dropdown.get())

        # Get selected test options from checkboxes
        check_box_test_options = {"--demo": "Demo Mode", "--slow": "Slow Mode", "--html=report.html --dashboard": "Generate Report", "--screenshot": "Save Screenshot", "--incognito": "Incognito Mode", "--maximize": "Start Maximized", "--dark": "Dark Mode", "--headless": "Headless Mode", "--trace": "Trace/Debug Mode"}
        selected_test_options = []
        for checkbox, (option_key, option_value) in zip(self.checkboxes, check_box_test_options.items()):
            if checkbox.get() and option_value in self.checkbox_texts:
                selected_test_options.append(option_key)
        selected_test_option = " ".join(selected_test_options)

        # Get the route type
        route_type_list = {1: "--var3=1_6", 2: "--var3=1_7", 3: "--var3=1_8"}
        route = route_type_list.get(self.route_type_var.get(), self.route_type_var.get())

        # Get the client in pre request
        client_values_parameter = {
            "--var3=random": "Random",
            "--var3=321_corporate_payroll_ltd": "321 Corporate Payroll Ltd",
            "--var3=321_pay_ltd": "321 Pay Ltd",
            "--var3=4th_option_ltd": "4th Option Ltd",
            "--var3=adelta_staffing_ltd": "Adelta Staffing Ltd",
            "--var3=ado_pay_ltd": "ADO Pay Ltd",
            "--var3=akin_resources_ltd": "Akin Resources Ltd",
            "--var3=apollo_staffing_ltd": "Apollo Staffing Ltd",
            "--var3=appp_solutions_ltd": "Appp Solutions Ltd",
            "--var3=brooklands_project_management_limited": "BROOKLANDS PROJECT MANAGEMENT LIMITED",
            "--var3=business2_ltd": "Business2 Ltd",
            "--var3=cerberus_staffing_ltd": "Cerberus Staffing Ltd",
            "--var3=charon_solutions_ltd": "Charon Solutions Ltd",
            "--var3=wageHub_outsourcing_limited": "WageHub Outsourcing Limited",
            "--var3=deliverex_ltd": "Deliverex Ltd"

        }

        # Get the industry in pre requestope
        industry_values_parameter = {
            "--var1=random": "Random",
            "--var1=accounts": "Accounts",
            "--var1=transport": "Transport",
            "--var1=administration": "Administration",
            "--var1=advertising": "Advertising",
            "--var1=agricultural_services": "Agricultural services",
            "--var1=boarding_or_care_of_animals": "Boarding or care of animals",
            "--var1=call_centre": "Call Centre",
            "--var1=cleaning": "Cleaning",
            "--var1=computer_repair_services": "Computer repair services",
            "--var1=construction": "Construction",
            "--var1=engineering": "Engineering",
            "--var1=healthcare": "Healthcare",
            "--var1=financial_services": "Financial services",
            "--var1=gardening": "Gardening",
            "--var1=hospitality": "Hospitality"
        }

        communication_template_values_parameters = {
            "--var2=all": "Select All",
            "--var2=vat": "Vat Return",
            "--var2=invoice": "Invoice Approval",
            "--var2=funding": "Funding Request",
            "--var2=change_of_flat_rate": "Change Of Flat Rate VAT",
            "--var2=confirmation_of_duties": "Confirmation of Duties"
        }

        def run_test(test_command):
            # print("Running subprocess with command:", test_command)
            print("")
            print("Selected Test: ", self.process_dropdown.get())
            print("Selected Instance: ", self.instance_dropdown.get())
            print("Selected Browser: ", self.browser_dropdown.get(), "\n")
            subprocess.run(test_command, shell=True)

        # Execute the selected test based on the selection
        if process_selection == "Registration to ready":
            director_pref_value = "--var1=" + self.director_preferred_value_entry.get()
            registration_to_ready_command = f"pytest ..//tests_compass_star/test_invitation_to_registration_new.py {route} {director_pref_value} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(registration_to_ready_command,)).start()

        if process_selection == "Accepted to ready":
            director_email = self.director_email_entry.get()
            with open("..//data//email.txt", "w") as file:
                file.write(director_email)
            director_pref_value = "--var1=" + self.director_preferred_value_entry.get()
            registration_to_ready_command = f"pytest ..//tests_compass_star/test_accepted_to_ready.py {route} {director_pref_value} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(registration_to_ready_command,)).start()

        elif process_selection == "Transfer a supplier":
            transfer_company_name = "--var1=" + self.transfer_company_name_entry.get()
            transfer_a_supplier_command = f'pytest ..//tests_compass_star/test_transfer_a_supplier.py "{transfer_company_name}" {selected_test_option} {staging_option} {browser_option} --rs -x -q -s'
            threading.Thread(target=run_test, args=(transfer_a_supplier_command,)).start()

        elif process_selection == "Mobile registration to Ready":
            device_selected = self.mobile_device_selection_dropdown.get()

            if device_selected == "Emulator":
                with open("..//data//mobile_device_type.txt", "w") as file:
                    file.write("--emulator")
            elif device_selected == "Vivo":
                with open("..//data//mobile_device_type.txt", "w") as file:
                    file.write("--vivo")
            elif device_selected == "Oppo":
                with open("..//data//mobile_device_type.txt", "w") as file:
                    file.write("--oppo")

            director_pref_value = "--var1=" + self.director_preferred_value_entry.get()
            device_list = self.mobile_device_selection_dropdown.get()
            mobile_registration_to_ready_command = f'pytest ..//tests_compass_star/test_invitation_to_registration_with_mobile.py  {route} {director_pref_value} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s'
            threading.Thread(target=run_test, args=(mobile_registration_to_ready_command,)).start()

        elif process_selection == "Add provisional pre-request":
            client_option = next(key for key, value in client_values_parameter.items() if value == self.select_client_dropdown.get())
            industry_option = next(key for key, value in industry_values_parameter.items() if value == self.select_industry_dropdown.get())
            priority_number = "--var2=" + self.priority_entry.get()
            add_provisional_command = f"pytest ..//tests_supplier_land/test_add_provisional_pre_request.py {client_option} {industry_option} {priority_number} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(add_provisional_command,)).start()

        elif process_selection == "Add confirmed pre-request":
            client_option = next(key for key, value in client_values_parameter.items() if value == self.select_client_dropdown.get())
            industry_option = next(key for key, value in industry_values_parameter.items() if value == self.select_industry_dropdown.get())
            priority_number = "--var2=" + self.priority_entry.get()
            add_provisional_command = f"pytest ..//tests_supplier_land/test_add_confirmed_pre_request.py {client_option} {industry_option} {priority_number} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(add_provisional_command,)).start()

        elif process_selection == "Pass to due diligence":
            due_diligence_company_name = "--var1=" + self.pass_to_due_diligence_company_name_entry.get()
            add_provisional_command = f'pytest ..//tests_supplier_land/test_pass_to_due_diligence.py "{due_diligence_company_name}" {selected_test_option} {staging_option} {browser_option} --rs -x -q -s'
            threading.Thread(target=run_test, args=(add_provisional_command,)).start()

        elif process_selection == "Withdraw IDD":
            withdraw_idd_company_name = "--var1=" + self.withdraw_idd_company_name_entry.get()
            withdraw_idd_command = f'pytest ..//tests_supplier_land/test_withdraw_idd.py "{withdraw_idd_company_name}" {selected_test_option} {staging_option} {browser_option} --rs -x -q -s'
            threading.Thread(target=run_test, args=(withdraw_idd_command,)).start()

        elif process_selection == "Upload communications template":
            communication_company_number = "--var1=" + self.communication_company_number_entry.get()
            template_option = next(key for key, value in communication_template_values_parameters.items() if value == self.select_communication_template_dropdown.get())
            upload_communications_command = f"pytest ..//tests_compass_star/test_upload_comms_template.py {communication_company_number} {template_option} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(upload_communications_command,)).start()


        # DESTINATION X
        #  "DestinationX Process": ["", "", "", "", "", "Send Location Notification", "Send Category Notification"]
        elif process_selection == "Add Categories":
            add_categories_command = '"test_login or test_add_categories"'
            destination_x_add_categories_command = f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k  {add_categories_command} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(destination_x_add_categories_command,)).start()

        elif process_selection == "Add Amenity":
            add_amenity_command = '"test_login or test_add_amenity"'
            destination_x_add_amenity_command = f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k  {add_amenity_command} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(destination_x_add_amenity_command,)).start()

        elif process_selection == "Add Sponsored Ads":
            add_sponsored_ads_command = '"test_login or test_add_sponsored_and_ads"'
            destination_x_add_sponsored_ads_command = f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k  {add_sponsored_ads_command} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(destination_x_add_sponsored_ads_command,)).start()

        elif process_selection == "Add News and Events":
            add_news_and_events_command = '"test_login or test_add_news_and_events"'
            destination_x_add_news_and_events_command = f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k  {add_news_and_events_command} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(destination_x_add_news_and_events_command,)).start()

        elif process_selection == "Send External Link Notification":
            pn_external_link_command = '"test_login or test_add_external_links_notification"'
            destination_x_pn_external_link_command_command = f"pytest ..//tests_destibrom/test_push_notification.py -k  {pn_external_link_command} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(destination_x_pn_external_link_command_command,)).start()

        elif process_selection == "Forgot Password Non-Existing(Mobile)":
            destination_x_forgot_password_mobile_command = f"pytest ..//tests_destibrom/test_forgot_password_mobile.py {selected_test_option} {staging_option} {browser_option} --rs -x -q -s --headless"
            threading.Thread(target=run_test, args=(destination_x_forgot_password_mobile_command,)).start()

        elif process_selection == "Create New Account (Mobile)":
            destination_x_create_new_account_mobile_command = f"pytest ..//tests_destibrom/test_create_an_account_mobile.py {selected_test_option} {staging_option} {browser_option} --rs -x -q -s --headless"
            threading.Thread(target=run_test, args=(destination_x_create_new_account_mobile_command,)).start()

        # Disable the 'Run' button during test execution
        self.buttons[0].configure(state="disabled")

        # Enable the 'Run' button after test execution
        self.buttons[0].configure(state="normal")

    def clear_fields(self):
        print("Clearing fields...")
        self.route_type_var.set(0)
        self.mobile_device_selection_dropdown.set("Select Device")
        self.director_preferred_value_entry.delete(0, 'end')
        self.transfer_company_name_entry.delete(0, 'end')
        self.pass_to_due_diligence_company_name_entry.delete(0, 'end')
        self.select_industry_dropdown.set("Select Industry")
        self.select_client_dropdown.set("Select Client")
        self.priority_entry.delete(0, 'end')
        self.withdraw_idd_company_name_entry.delete(0, 'end')
        self.director_email_entry.delete(0, 'end')
        self.communication_company_number_entry.delete(0, 'end')
        self.select_communication_template_dropdown.set("Select template")
        # Uncheck the test options checkboxes
        for checkbox in self.checkboxes:
            checkbox.deselect()
        print("Clear fields successfully\n ")

    def exit_application(self):
        self.app.destroy()


if __name__ == "__main__":
    app = QAApp()
    app.app.mainloop()
