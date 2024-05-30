import subprocess
import tkinter as tk
from tkinter import ttk

from art import *


class PytestRunnerApp:
    def __init__(self, master):
        def colored_text(text, color_code):
            return f"\033[{color_code}m{text}\033[0m"

        ascii_art = text2art(" Welcome to \n Automation", "slant")
        colored_ascii_art = colored_text(ascii_art, "35;1")
        print(colored_ascii_art)

        self.master = master
        master.title("QA-Team Automation Test Runner")

        def on_resize(event):
            # Update the size of the window based on the user's resizing
            new_width = event.width
            new_height = event.height
            master.geometry(f"{new_width}x{new_height}")
            master.bind("<Configure>", on_resize)

        master.configure(bg="light gray")  # Set background color

        self.create_label("Process:")
        self.select_a_test_dropdown_var = self.create_dropdown(
            ["New Registration To Ready",
             "T3 Allocation To Ready",
             "Registration to ready with mobile",
             "Transfer a Supplier",
             "Pass to Due Diligence",
             "Add Provisional Pre Request",
             "Add Confirmed Pre Request",
             "BSC Order Package",
             "Upload Communications Template",
             "Withdraw IDD",
             "Destination Bromsgrove",
             "Practice Page"],

        )

        self.create_label("Staging environment:")
        self.staging_dropdown_var = self.create_dropdown(
            ["QA Instance",
             "V1 Instance",
             "V2 Instance",
             "V3 Instance",
             "V4 Instance",
             "Echo Instance",
             "Testing Instance",
             "Replica Instance"])

        self.create_label("Browser:")
        self.select_browser_dropdown_var = self.create_dropdown(["Chrome", "Edge", "Firefox"])
        self.select_browser_dropdown_var.set("Chrome")

        style = ttk.Style()
        style.configure('Custom.TLabelframe', background='Light gray')

        # Create a new frame for the additional text box
        self.additional_text_frame = ttk.Frame(self.master)
        self.additional_text_frame.pack(pady=20, padx=10, fill="both")

        # Create a LabelFrame for the checkboxes
        checkbox_frame = ttk.LabelFrame(self.master, text="Select Test Options:")
        checkbox_frame.pack(pady=20, padx=10, fill="both")

        # Create a Label for additional options
        self.additional_text_label = ttk.Label(self.additional_text_frame, text="Additional Options", font=("Roboto", 12, "bold"))
        self.additional_text_label.pack(anchor="w", padx=8)

        # Create the additional text box and assign it to a variable
        self.additional_text_var = self.create_text_box(self.additional_text_frame, "")
        self.text_box_widget.pack_forget()
        self.select_a_test_dropdown_var.trace_add("write", self.update_additional_text_label)

        # Create a dropdown for types of template
        self.comms_template_dropdown_var, self.template_dropdown_value = self.create_comms_template_dropdown()
        self.template_dropdown_value.pack_forget()  # Initially hide the second dropdown

        # Create a dropdown for types of test in destibrom
        self.desibrom_select_test_dropdown_var, self.destibrom_dropdown_value = self.create_destibrom_type_of_test_dropdown()
        self.destibrom_dropdown_value.pack_forget()  # Initially hide the second dropdown

        # Create a dropdown for email credentials
        self.email_credentials_dropdown_var, self.email_credentials_value = self.create_email_credentials_dropdown()
        self.email_credentials_value.pack_forget()  # Initially hide the second dropdown

        # Create a dropdown for client dropdown
        self.pre_request_client_dropdown_var, self.pre_request_client_value = self.create_client_dropdown()
        self.pre_request_client_value.pack_forget()  # Initially hide the second dropdown
        # Create a Label for Select a Client (second text box)
        self.label_for_select_client = ttk.Label(self.additional_text_frame, text="Select a Client", font=("Roboto", 12, "bold"))
        self.label_for_select_client.pack_forget()

        # Create a Label for priority (second text box)
        self.label_for_priority_var = ttk.Label(self.additional_text_frame, text="Priority", font=("Roboto", 12, "bold"))
        self.label_for_priority_var.pack_forget()

        # Create a dropdown for Industry dropdown
        self.pre_request_industry_dropdown_var, self.pre_request_industry_value = self.create_industry_dropdown()
        self.pre_request_industry_value.pack_forget()  # Initially hide the second dropdown
        # Create a Label for Select Industry (second text box)
        self.label_for_select_industry = ttk.Label(self.additional_text_frame, text="Select Industry", font=("Roboto", 12, "bold"))
        self.label_for_select_industry.pack_forget()

        # Create a Label for upload communications template
        self.label_for_communications_var = ttk.Label(self.additional_text_frame, text="Type of template", font=("Roboto", 12, "bold"))
        self.label_for_communications_var.pack_forget()

        # Create a Label for upload communications template
        self.label_for_email_credentials_var = ttk.Label(self.additional_text_frame, text="Email Credentials", font=("Roboto", 12, "bold"))
        self.label_for_email_credentials_var.pack_forget()

        # Create the additional text box (second text box) and assign it to a variable
        self.additional_text_var2_entry = ttk.Entry(self.additional_text_frame, font=("Roboto", 18))

        # Inside the LabelFrame, add checkboxes with tooltips
        self.tooltip = None
        self.demo_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Demo Mode", "Slow down and visually see test actions as they occur.", 0, 0)
        self.slow_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Slow Mode", "Slow down the automation.", 0, 1)
        self.report_checkbox_var = self.create_checkbox(checkbox_frame, "Generate Report", "Creates a detailed pytest-html report after tests finish.", 0, 2)
        self.screenshot_checkbox_var = self.create_checkbox(checkbox_frame, "Save Screenshot", "Save a screenshot at the end of each test.", 1, 0)
        self.incognito_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Incognito Mode", "Enable Chrome's Incognito mode.", 1, 1)
        self.start_window_maximize_var = self.create_checkbox(checkbox_frame, "Start Maximized", "Start tests with the browser window maximized.", 1, 2)
        self.dark_mode_var = self.create_checkbox(checkbox_frame, "Dark Mode", "Enable Chrome's Dark mode.", 2, 0)
        self.headless_var = self.create_checkbox(checkbox_frame, "Headless", "Run tests in headless mode.", 2, 1)
        self.final_trace_var = self.create_checkbox(checkbox_frame, "Trace/Debug", "Debug Mode after each test.", 2, 2)

        self.run_button = self.create_button("Run", lambda: self.run_pytest(), bg="green", fg="white", padx=20)
        self.clear_button = self.create_button("Clear", self.clear_fields, bg="blue", fg="white", padx=20)
        self.quit_button = self.create_button("Exit", master.quit, bg="red", fg="white", padx=20)

    def create_comms_template_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        template_values = {
            "Select All": "--var2=all",
            "Vat Return": "--var2=vat",
            "Invoice Approval": "--var2=invoice",
            "Funding Request": "--var2=funding",
            "Change Of Flat Rate VAT": "--var2=change_of_flat_rate"

        }

        values = list(template_values.keys())

        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values, font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)
        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def create_client_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        client_values = {
            "Random": "--var3=random",
            "321 Corporate Payroll Ltd": "--var3=321_corporate_payroll_ltd",
            "321 Pay Ltd": "--var3=321_pay_ltd",
            "4th Option Ltd": "--var3=4th_option_ltd",
            "Adelta Staffing Ltd": "--var3=adelta_staffing_ltd",
            "ADO Pay Ltd": "--var3=ado_pay_ltd",
            "Akin Resources Ltd": "--var3=akin_resources_ltd",
            "Apollo Staffing Ltd": "--var3=apollo_staffing_ltd",
            "Appp Solutions Ltd": "--var3=appp_solutions_ltd",
            "BROOKLANDS PROJECT MANAGEMENT LIMITED": "--var3=brooklands_project_management_limited",
            "Business2 Ltd": "--var3=business2_ltd",
            "Cerberus Staffing Ltd": "--var3=cerberus_staffing_ltd",
            "Charon Solutions Ltd": "--var3=charon_solutions_ltd",
            "Hand Technology ltd": "--var3=hand_technology_ltd",
            "Deliverex Ltd": "--var3=deliverex_ltd"

        }

        values = list(client_values.keys())
        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values, font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)
        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def create_industry_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        industry_values = {
            "Random": "--var1=random",
            "Accounts": "--var1=accounts",
            "Transport": "--var1=transport",
            "Administration": "--var1=administration",
            "Advertising ": "--var1=advertising",
            "Agricultural services": "--var1=agricultural_services",
            "Boarding or care of animals": "--var1=boarding_or_care_of_animals",
            "Call Centre": "--var1=call_centre",
            "Cleaning": "--var1=cleaning",
            "Computer repair services": "--var1=computer_repair_services",
            "Construction": "--var1=construction",
            "Engineering": "--var1=engineering",
            "Healthcare": "--var1=healthcare",
            "Financial services": "--var1=financial_services",
            "Gardening": "--var1=gardening",
            "Hospitality": "--var1=hospitality"

        }

        values = list(industry_values.keys())
        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values, font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)
        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def create_email_credentials_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        list_of_email_credentials = {
            "Gmail": "--var2=gmail",
            "Outlook": "--var2=outlook",

        }

        values = list(list_of_email_credentials.keys())

        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values, font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)
        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def create_destibrom_type_of_test_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        list_of_destibrom_test = {
            "Add Categories": "",
            "Add Amenity": "",
            "Add Sponsored Ads": "",
            "Add News and Updates": "",
            "Send External Link Notification": "",
            "Send Location Notification": "",
            "Send Category Notification": ""
        }

        values = list(list_of_destibrom_test.keys())

        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values, font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)
        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def clear_fields(self):
        # Clear all the fields
        self.desibrom_select_test_dropdown_var.set("")
        self.select_a_test_dropdown_var.set("")
        self.staging_dropdown_var.set("")
        self.additional_text_var.set("")
        self.demo_mode_checkbox_var.set(0)
        self.slow_mode_checkbox_var.set(0)
        self.report_checkbox_var.set(0)
        self.screenshot_checkbox_var.set(0)
        self.incognito_mode_checkbox_var.set(0)
        self.start_window_maximize_var.set(0)
        self.dark_mode_var.set(0)
        self.headless_var.set(0)
        self.final_trace_var.set(0)
        self.comms_template_dropdown_var.set("")
        self.email_credentials_dropdown_var.set("")
        self.pre_request_client_dropdown_var.set("")
        self.pre_request_industry_dropdown_var.set("")
        self.additional_text_var2_entry.delete(0, 'end')

    def update_additional_text_label(self, *args):
        selected_test = self.select_a_test_dropdown_var.get()
        # Define a dictionary that maps test names to label text
        label_texts = {
            "Registration to ready with mobile": "Director Preferred Yearly Contract Value",
            "New Registration To Ready": "Director Preferred Yearly Contract Value",
            "Upload Communications Template": "Company number",
            "Transfer a Supplier": "Company Name",
            "Pass to Due Diligence": "Company Name",
            "BSC Order Package": "Company Number from CH",
            "Practice Page": "This is practice page",
            "T3 Allocation To Ready": "Director's Email Address",
            "Add Provisional Pre Request": "BSC ID",
            "Withdraw IDD": "Company Number",
            "Add Confirmed Pre Request": ""

        }
        # Use the dictionary to set the label text or use a default value
        self.additional_text_label.config(text=label_texts.get(selected_test, "Additional Options"))

        if selected_test in ["New Registration To Ready", "Transfer a Supplier", "Pass to Due Diligence", "BSC Order Package",
                             "Upload Communications Template", "T3 Allocation To Ready", "Add Provisional Pre Request", "Withdraw IDD", "Registration to ready with mobile"]:
            self.additional_text_label.pack(fill="both", padx=6, pady=6)
            self.text_box_widget.pack(fill="both", padx=6, pady=6)

        if selected_test == "Upload Communications Template":
            self.label_for_communications_var.pack(anchor="w", padx=8, pady=6)
            self.template_dropdown_value.pack()  # Show the second dropdown
        else:
            self.template_dropdown_value.pack_forget()  # Hide the second dropdown
            self.label_for_communications_var.pack_forget()

        if selected_test == "Destination Bromsgrove":
            self.destibrom_dropdown_value.pack()  # Show the second dropdown
            self.text_box_widget.pack_forget()
        else:
            self.destibrom_dropdown_value.pack_forget()  # Hide the second dropdown

        if selected_test == "BSC Order Package":
            self.label_for_email_credentials_var.pack(anchor="w", padx=8, pady=6)
            self.email_credentials_value.pack()  # Show the second dropdown
        else:
            self.label_for_email_credentials_var.pack_forget()  # Hide the second dropdown
            self.email_credentials_value.pack_forget()

        if selected_test == "Add Provisional Pre Request":
            self.label_for_select_client.pack(anchor="w", padx=8, pady=2)
            self.pre_request_client_value.pack()
            self.label_for_select_industry.pack(anchor="w", padx=8, pady=2)
            self.pre_request_industry_value.pack()
            self.label_for_priority_var.pack(anchor="w", padx=8, pady=2)
            self.additional_text_var2_entry.pack(fill="both", padx=6, pady=6)

        elif selected_test == "Add Confirmed Pre Request":
            self.label_for_select_client.pack(anchor="w", padx=8, pady=2)
            self.pre_request_client_value.pack()
            self.label_for_select_industry.pack(anchor="w", padx=8, pady=2)
            self.pre_request_industry_value.pack()
            self.label_for_priority_var.pack(anchor="w", padx=8, pady=2)
            self.additional_text_var2_entry.pack(fill="both", padx=6, pady=6)
            self.additional_text_label.pack_forget()
            self.text_box_widget.pack_forget()

        else:
            self.pre_request_client_value.pack_forget()
            self.label_for_select_client.pack_forget()
            self.label_for_select_industry.pack_forget()
            self.pre_request_industry_value.pack_forget()
            self.label_for_priority_var.pack_forget()
            self.additional_text_var2_entry.pack_forget()

    def create_text_box(self, frame, label_text):
        label = ttk.Label(frame, text=label_text, font=("Roboto", 12, "bold"))
        label.pack()
        label.place(anchor="center")
        text_var = tk.StringVar()
        text_box = ttk.Entry(frame, textvariable=text_var, font=("Roboto", 18))
        text_box.pack(fill="both", padx=6, pady=5)
        self.text_box_widget = text_box
        return text_var

    def create_label(self, text):
        label = tk.Label(self.master, text=text, font=("Roboto", 14, "bold"), bg="lightgray")
        label.pack(anchor="w", pady=(25, 0), padx=8)
        return label

    def create_label1(self, text):
        label = tk.Label(self.master, text=text, font=("Roboto", 12, "bold"), bg="lightgray")
        label.pack(pady=(20, 10))
        return label

    def create_dropdown(self, values):
        def remove_highlight(event):
            event.widget.master.focus_set()

        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.master, textvariable=dropdown_var, values=values, font=("Roboto", 17), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)

        # Calculate the width based on the longest item
        max_item_width = max(len(item) for item in values)
        dropdown.config(width=max_item_width)
        dropdown.config(width=27)

        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var

    def create_checkbox(self, parent, text, tooltip_text, row, column):
        checkbox_var = tk.IntVar()
        checkbox = ttk.Checkbutton(parent, text=text, variable=checkbox_var)
        checkbox.grid(row=row, column=column, padx=5, pady=5, sticky="w")
        checkbox.bind("<Enter>", lambda event, text=tooltip_text: self.show_tooltip(event, text))
        checkbox.bind("<Leave>", self.hide_tooltip)
        return checkbox_var

    def show_tooltip(self, event, text):
        x, y, _, _ = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(event.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=text, background="light yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, _):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()

    def create_button(self, text, command, **kwargs):
        button = tk.Button(self.master, text=text, command=command, **kwargs, font=("Roboto", 12, "bold"))
        button.pack(side="left", padx=(10, 10), pady=(0, 10), expand=True, fill="both")
        return button

    def run_pytest(self):
        selected_test = self.select_a_test_dropdown_var.get()
        selected_staging = self.staging_dropdown_var.get()
        selected_browser = self.select_browser_dropdown_var.get()
        if selected_test:
            print("\n Selected Test: ", selected_test)
        if selected_staging:
            print("\n Selected Staging: ", selected_staging)
        if selected_browser:
            print("\n Selected Browser:", selected_browser)

        additional_text_var2 = "--var2=" + self.additional_text_var2_entry.get()
        additional_text_var1 = "--var1=" + self.additional_text_var.get()
        selected_test = self.select_a_test_dropdown_var.get()

        test_commands = {
            "New Registration To Ready": [f"pytest ..//tests_compass_star/test_invitation_to_registration_new.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Registration to ready with mobile": [f"pytest ..//tests_compass_star/test_invitation_to_registration_with_mobile.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "T3 Allocation To Ready": [f"pytest ..//tests_compass_star/test_t3_allocation_to_ready.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Transfer a Supplier": [f'pytest ..//tests_compass_star/test_transfer_a_supplier.py {additional_text_var2} "{additional_text_var1}" --rs -x -q -s'],
            "Pass to Due Diligence": [f'pytest ..//tests_supplier_land/test_pass_to_due_diligence.py {additional_text_var2} "{additional_text_var1}" --rs -x -q -s'],
            "Add Provisional Pre Request": [f"pytest ..//tests_supplier_land/test_add_provisional_pre_request.py {additional_text_var1} {additional_text_var1} --rs -x -q -s"],
            "Add Confirmed Pre Request": [f"pytest ..//tests_supplier_land/test_add_confirmed_pre_request.py {additional_text_var1} {additional_text_var1} --rs -x -q -s"],
            "BSC Order Package": [f"pytest ..//tests_bsc/test_bsc_redeem_package.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Upload Communications Template": [f"pytest ..//tests_compass_star/test_upload_comms_template.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Withdraw IDD": [f"pytest ..//tests_supplier_land/test_withdraw_idd.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Practice Page": [f"pytest ..//test_runner/practice.py {additional_text_var2} {additional_text_var1} --rs -x -q -s"]
        }
        add_categories_command = '"test_login or test_add_categories"'
        add_amenity_command = '"test_login or test_add_amenity"'
        add_sponsored_ads_command = '"test_login or test_add_sponsored_and_ads"'
        add_news_and_update_command = '"test_login or test_add_news_and_events"'
        pn_external_link_command = '"test_login or test_add_external_links_notification"'
        pn_location_command = '"test_login or test_add_location_notification"'
        pn_category_command = '"test_login or test_add_category_notification"'

        list_of_destibrom_test_commands = {
            "Add Categories": [f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k {add_categories_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Add Amenity": [f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k {add_amenity_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Add Sponsored Ads": [f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k {add_sponsored_ads_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Add News and Updates": [f"pytest ..//tests_destibrom/test_end_to_end_destibrom.py -k {add_news_and_update_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Send External Link Notification": [f"pytest ..//tests_destibrom/test_push_notification.py -k {pn_external_link_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Send Location Notification": [f"pytest ..//tests_destibrom/test_push_notification.py -k {pn_location_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"],
            "Send Category Notification": [f"pytest ..//tests_destibrom/test_push_notification.py -k {pn_category_command} {additional_text_var2} {additional_text_var1} --rs -x -q -s"]
        }

        # Get the value of the list of test in desti dropdown
        additional_dropdown_value_for_destibrom_test = self.desibrom_select_test_dropdown_var.get()

        if additional_dropdown_value_for_destibrom_test in list_of_destibrom_test_commands:
            pytest_command = list_of_destibrom_test_commands[additional_dropdown_value_for_destibrom_test]

        # Get the value of the comms template dropdown
        additional_dropdown_value_for_comms = self.comms_template_dropdown_var.get()
        option_values_for_comms_dropdown = {
            "Select All": "--var2=all",
            "Vat Return": "--var2=vat",
            "Invoice Approval": "--var2=invoice",
            "Funding Request": "--var2=funding",
            "Change Of Flat Rate VAT": "--var2=change_of_flat_rate"
        }
        # Get the value of the comms template dropdown
        option_values_for_email_credentials_dropdown = {
            "Gmail": "--var2=gmail",
            "Outlook": "--var2=outlook",
        }
        additional_dropdown_value_for_email_credentials = self.email_credentials_dropdown_var.get()

        client_values = {
            "Random": "--var3=random",
            "321 Corporate Payroll Ltd": "--var3=321_corporate_payroll_ltd",
            "321 Pay Ltd": "--var3=321_pay_ltd",
            "4th Option Ltd": "--var3=4th_option_ltd",
            "Adelta Staffing Ltd": "--var3=adelta_staffing_ltd",
            "ADO Pay Ltd": "--var3=ado_pay_ltd",
            "Akin Resources Ltd": "--var3=akin_resources_ltd",
            "Apollo Staffing Ltd": "--var3=apollo_staffing_ltd",
            "Appp Solutions Ltd": "--var3=appp_solutions_ltd",
            "BROOKLANDS PROJECT MANAGEMENT LIMITED": "--var3=brooklands_project_management_limited",
            "Business2 Ltd": "--var3=business2_ltd",
            "Cerberus Staffing Ltd": "--var3=cerberus_staffing_ltd",
            "Charon Solutions Ltd": "--var3=charon_solutions_ltd",
            "Deliverex Ltd": "--var3=deliverex_ltd"

        }
        industry_values = {
            "Random": "--var1=random",
            "Accounts": "--var1=accounts",
            "Transport": "--var1=transport",
            "Administration": "--var1=administration",
            "Advertising ": "--var1=advertising",
            "Agricultural services": "--var1=agricultural_services",
            "Boarding or care of animals": "--var1=boarding_or_care_of_animals",
            "Call Centre": "--var1=call_centre",
            "Cleaning": "--var1=cleaning",
            "Computer repair services": "--var1=computer_repair_services",
            "Construction": "--var1=construction",
            "Engineering": "--var1=engineering",
            "Healthcare": "--var1=healthcare",
            "Financial services": "--var1=financial_services",
            "Gardening": "--var1=gardening",
            "Hospitality": "--var1=hospitality"

        }
        additional_dropdown_value_for_client = self.pre_request_client_dropdown_var.get()
        additional_dropdown_value_for_industry = self.pre_request_industry_dropdown_var.get()

        if selected_test in test_commands:
            pytest_command = test_commands[selected_test]
            pytest_command.append(client_values.get(additional_dropdown_value_for_client, ""))  # Get the corresponding option
            pytest_command.append(industry_values.get(additional_dropdown_value_for_industry, ""))  # Get the corresponding option
            pytest_command.append(option_values_for_comms_dropdown.get(additional_dropdown_value_for_comms, ""))  # Get the corresponding option
            pytest_command.append(option_values_for_email_credentials_dropdown.get(additional_dropdown_value_for_email_credentials, ""))  # Get the corresponding option
        else:
            print("")

        options = {
            "--demo": self.demo_mode_checkbox_var.get(),
            "--html=report.html --dashboard": self.report_checkbox_var.get(),
            "--screenshot": self.screenshot_checkbox_var.get(),
            "--slow": self.slow_mode_checkbox_var.get(),
            "--incognito": self.incognito_mode_checkbox_var.get(),
            "--maximize": self.start_window_maximize_var.get(),
            "--dark": self.dark_mode_var.get(),
            "--headless": self.headless_var.get(),
            "--trace": self.final_trace_var.get()

        }

        additional_args = self.staging_dropdown_var.get()

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
        pytest_command.extend([key for key, value in staging_options.items() if value == additional_args])
        browser_arguments = self.select_browser_dropdown_var.get()
        browser_options = {
            "--chrome": "Chrome",
            "--edge": "Edge",
            "--firefox": "Firefox"
        }
        pytest_command.extend([key for key, value in browser_options.items() if value == browser_arguments])
        pytest_command.extend([option for option, value in options.items() if value])
        subprocess.Popen(" ".join(pytest_command), shell=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = PytestRunnerApp(root)
    root.mainloop()
