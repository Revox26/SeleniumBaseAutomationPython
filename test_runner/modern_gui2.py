import subprocess
import threading
import tkinter
import customtkinter


class QAApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("600x800")
        self.app.title("QA Team Automation")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.frame = self.create_frame()
        self.create_module_selection()
        self.create_dropdowns()
        self.create_test_options()
        self.create_buttons()
        self.registration_to_ready_additional_data_options()
        self.transfer_a_supplier_additional_data()
        self.app.bind("<Configure>", self.handle_drag_to_other_monitor)

    def handle_drag_to_other_monitor(self, event):
        # Show or hide frames based on dropdown selection
        process_selection = self.process_dropdown.get()
        self.show_additional_data_for_process(process_selection)

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

        self.yearly_contract_frame.grid_remove()  # hide by default

    def transfer_a_supplier_additional_data(self):
        self.transfer_a_supplier_frame = customtkinter.CTkFrame(master=self.frame)
        self.transfer_a_supplier_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        # Add a text entry for 'Director Preferred Value'
        self.company_name_label = customtkinter.CTkLabel(master=self.transfer_a_supplier_frame, justify=customtkinter.LEFT, text="Company Name", font=("Arial", 15))
        self.company_name_label.grid(row=0, column=0, pady=(5, 0), padx=10, sticky="w")

        self.transfer_company_name_entry = customtkinter.CTkEntry(master=self.transfer_a_supplier_frame, width=300)
        self.transfer_company_name_entry.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nsew")

        self.transfer_a_supplier_frame.grid_remove()

    def show_additional_data_for_process(self, process_selection):
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
        module_options = ["CSL PROCESS", "SL PROCESS", "BSC PROCESS", "BROMSGROVE PROCESS"]
        self.segmented_button = customtkinter.CTkSegmentedButton(master=self.frame, values=module_options, command=self.update_label)
        self.segmented_button.grid(row=1, column=0, columnspan=2, pady=30, padx=30)

        self.module_label = customtkinter.CTkLabel(master=self.frame, justify=customtkinter.LEFT, text="Select a module", font=("Arial", 30))
        self.module_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10)

    def create_dropdowns(self):
        self.instance_dropdown = customtkinter.CTkOptionMenu(self.frame, values=["QA Instance", "V1 Instance", "V2 Instance", "V3 Instance", "V4 Instance", "Replica Instance", "Delta Instance", "Echo Instance"], width=442, height=40, font=("Arial", 25))
        self.instance_dropdown.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        self.instance_dropdown.set("Select instance")

        self.browser_dropdown = customtkinter.CTkOptionMenu(self.frame, values=["Chrome", "Edge", "Firefox"], width=442, height=40, font=("Arial", 25))
        self.browser_dropdown.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.browser_dropdown.set("Chrome")

        self.process_dropdown_options = {
            "CSL Process": ["Registration to ready", "Mobile registration to Ready", "Transfer a supplier", "T3 allocation to ready", "Upload communications template"],
            "SL Process": ["Add provisional pre-request", "Add confirmed pre-request", "Pass to due diligence", "Withdraw IDD"],
            "BSC Process": ["BSC order package"]
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

        elif option == "SL PROCESS":
            self.process_dropdown.set("Select SL process")
            self.process_dropdown.configure(values=self.process_dropdown_options["SL Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)
        elif option == "BSC PROCESS":
            self.process_dropdown.set("Select BSC process")
            self.process_dropdown.configure(values=self.process_dropdown_options["BSC Process"])
            self.process_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)

    def run_button_function(self, process_selection):

        staging_options = {
            "--data=qa": "QA Instance",
            "--data=v1": "V1 Instance",
            "--data=v2": "V2 Instance",
            "--data=v3": "V3 Instance",
            "--data=v4": "V4 Instance",
            "--data=echo": "Echo Instance",
            "--data=testing": "Testing Instance",
            "--data=replica": "Replica Instance"
        }

        browser_options = {
            "--chrome": "Chrome",
            "--edge": "Edge",
            "--firefox": "Firefox"
        }

        check_box_test_options = {
            "--demo": "Demo Mode",
            "--slow": "Slow Mode",
            "--html=report.html --dashboard": "Generate Report",
            "--screenshot": "Save Screenshot",
            "--incognito": "Incognito Mode",
            "--maximize": "Start Maximized",
            "--dark": "Dark Mode",
            "--headless": "Headless Mode",
            "--trace": "Trace/Debug Mode"

        }

        # Get selected test options from checkboxes
        selected_test_options = []
        for checkbox, (option_key, option_value) in zip(self.checkboxes, check_box_test_options.items()):
            if checkbox.get() and option_value in self.checkbox_texts:
                selected_test_options.append(option_key)
        selected_test_option = " ".join(selected_test_options)

        # Get selected browser from dropdown
        browser_option = next(key for key, value in browser_options.items() if value == self.browser_dropdown.get())
        # Get selected instance from dropdown
        staging_option = next(key for key, value in staging_options.items() if value == self.instance_dropdown.get())

        def run_test(test_command):
            print("Running subprocess with command:", test_command)
            subprocess.run(test_command, shell=True)

        # Execute the selected test based on the selection
        if process_selection == "Registration to ready":
            route_type_list = {
                1: "--var3=1_6",
                2: "--var3=1_7",
                3: "--var3=1_8"
            }
            route = route_type_list.get(self.route_type_var.get(), self.route_type_var.get())
            director_pref_value = "--var1=" + self.director_preferred_value_entry.get()
            registration_to_ready_command = f"pytest ..//tests_compass_star/test_invitation_to_registration_new.py {route} {director_pref_value} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(registration_to_ready_command,)).start()

        elif process_selection == "Transfer a supplier":
            transfer_company_name = "--var1=" + self.transfer_company_name_entry.get()
            transfer_a_supplier_command = f'pytest ..//tests_compass_star/test_transfer_a_supplier.py "{transfer_company_name}" {selected_test_option} {staging_option} {browser_option} --rs -x -q -s'
            threading.Thread(target=run_test, args=(transfer_a_supplier_command,)).start()

        elif process_selection == "Mobile registration to Ready":
            route_type_list = {
                1: "--var3=1_6",
                2: "--var3=1_7",
                3: "--var3=1_8"
            }
            route = route_type_list.get(self.route_type_var.get(), self.route_type_var.get())
            director_pref_value = "--var1=" + self.director_preferred_value_entry.get()
            mobile_registration_to_ready_command = f"pytest ..//tests_compass_star/test_invitation_to_registration_with_mobile.py {route} {director_pref_value} {selected_test_option} {staging_option} {browser_option} --rs -x -q -s"
            threading.Thread(target=run_test, args=(mobile_registration_to_ready_command,)).start()

        # Disable the 'Run' button during test execution
        self.buttons[0].configure(state="disabled")

        # Enable the 'Run' button after test execution
        self.buttons[0].configure(state="normal")


if __name__ == "__main__":
    app = QAApp()
    app.app.mainloop()
