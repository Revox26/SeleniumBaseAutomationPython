import subprocess
import tkinter as tk
from tkinter import ttk

from art import *


class PytestRunnerApp:
    def __init__(self, master):
        ascii_art = text2art(" Welcome to \n Automation", "slant")
        print(ascii_art)
        self.master = master
        master.title("QA-Team Automation Test Runner")

        def on_resize(event):
            # Update the size of the window based on the user's resizing
            new_width = event.width
            new_height = event.height
            master.geometry(f"{new_width}x{new_height}")
            master.bind("<Configure>", on_resize)

        master.configure(bg="light gray")  # Set background color

        self.create_label("Select a test:")
        self.select_a_test_dropdown_var = self.create_dropdown(
            ["Registration To Ready",
             "New Registration To Ready",
             "Transfer a Supplier",
             "Pass to Due Diligence",
             "Add Provisional Pre Request",
             "Add Confirmed Pre Request",
             "BSC Order Package",
             "Upload Communications Template",
             "Practice Page"],

        )

        self.create_label("Select a staging environment:")
        self.staging_dropdown_var = self.create_dropdown(
            ["QA Instance",
             "V1 Instance",
             "V2 Instance",
             "V3 Instance",
             "V4 Instance",
             "Echo Instance",
             "Replica Instance"])

        self.create_label("Select a browser:")
        self.select_browser_dropdown_var = self.create_dropdown(["Chrome", "Edge", "Firefox"])

        style = ttk.Style()
        style.configure('Custom.TLabelframe', background='Light gray')

        # Create a new frame for the additional text box
        self.additional_text_frame = ttk.Frame(self.master)
        self.additional_text_frame.pack(pady=20, padx=10, fill="both")

        # Create a LabelFrame for the checkboxes
        checkbox_frame = ttk.LabelFrame(self.master, text="Select Test Options:")
        checkbox_frame.pack(pady=20, padx=10, fill="both")

        # Create a Label for additional options
        self.additional_text_label = ttk.Label(self.additional_text_frame, text="Additional Options",
                                               font=("Roboto", 12, "bold"))
        self.additional_text_label.pack()
        # Create the additional text box and assign it to a variable
        self.additional_text_var = self.create_text_box(self.additional_text_frame, "")
        self.select_a_test_dropdown_var.trace_add("write", self.update_additional_text_label)

        # Inside the LabelFrame, add checkboxes with tooltips
        self.demo_mode_checkbox_var = self.create_checkbox(checkbox_frame,
                                                           "Demo Mode",
                                                           "Slow down and visually see test actions as they occur.",
                                                           0, 0)

        self.slow_mode_checkbox_var = self.create_checkbox(checkbox_frame,
                                                           "Slow Mode",
                                                           "Slow down the automation.",
                                                           0, 1)

        self.report_checkbox_var = self.create_checkbox(checkbox_frame,
                                                        "Generate Report",
                                                        "Creates a detailed pytest-html report after tests finish.",
                                                        0, 2)

        self.screenshot_checkbox_var = self.create_checkbox(checkbox_frame,
                                                            "Save Screenshot",
                                                            "Save a screenshot at the end of each test.",
                                                            1, 0)

        self.incognito_mode_checkbox_var = self.create_checkbox(checkbox_frame,
                                                                "Incognito Mode",
                                                                "Enable Chrome's Incognito mode.",
                                                                1, 1)

        self.start_window_maximize_var = self.create_checkbox(checkbox_frame,
                                                              "Start Maximized",
                                                              "Start tests with the browser window maximized.",
                                                              1, 2)
        self.dark_mode_var = self.create_checkbox(checkbox_frame,
                                                  "Dark Mode",
                                                  "Enable Chrome's Dark mode.",
                                                  2, 0)
        self.headless_var = self.create_checkbox(checkbox_frame,
                                                 "Headless",
                                                 "Run tests in headless mode.",
                                                 2, 1)
        self.final_trace_var = self.create_checkbox(checkbox_frame,
                                                    "Trace/Debug",
                                                    "Debug Mode after each test.",
                                                    2, 2)

        self.run_button = self.create_button("Run", lambda: self.run_pytest(), bg="green", fg="white", padx=20)
        self.clear_button = self.create_button("Clear", self.clear_fields, bg="blue", fg="white", padx=20)
        self.quit_button = self.create_button("Quit", master.quit, bg="red", fg="white", padx=20)

        self.comms_template_dropdown_var, self.template_dropdown_value = self.create_comms_template_dropdown()
        # Replace with your desired options
        self.template_dropdown_value.pack_forget()  # Initially hide the second dropdown

    def create_comms_template_dropdown(self):
        def remove_highlight(event):
            event.widget.master.focus_set()

        template_values = {
            "Select All": "--var2=all",
            "Vat Return": "--var2=vat",
            "Invoice Approval": "--var2=invoice",
            "Funding Request": "--var2=funding"

        }

        values = list(template_values.keys())

        dropdown_var = tk.StringVar()
        dropdown = ttk.Combobox(self.additional_text_frame, textvariable=dropdown_var, values=values,
                                font=("Roboto", 18), state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)

        dropdown.config(width=26)
        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var, dropdown

    def clear_fields(self):
        # Clear all the fields
        self.select_a_test_dropdown_var.set("")
        self.staging_dropdown_var.set("")
        self.select_browser_dropdown_var.set("")
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

    def update_additional_text_label(self, *args):
        selected_test = self.select_a_test_dropdown_var.get()
        # Define a dictionary that maps test names to label text
        label_texts = {
            "New Registration To Ready": "Director Preferred Yearly Contract Value",
            "Upload Communications Template": "Company number and type of template",
            "Transfer a Supplier": "Company Name",
            "Pass to Due Diligence": "Company Name",
            "BSC Order Package": "Company Number from CH",
            "Practice Page": "This is practice page"

        }
        # Use the dictionary to set the label text or use a default value
        self.additional_text_label.config(text=label_texts.get(selected_test, "Additional Options"))

        if selected_test == "Upload Communications Template":
            self.template_dropdown_value.pack()  # Show the second dropdown
        else:
            self.template_dropdown_value.pack_forget()  # Hide the second dropdown

    def create_text_box(self, frame, label_text):
        label = ttk.Label(frame, text=label_text, font=("Roboto", 12, "bold"))
        label.pack(padx=0, pady=0)
        text_var = tk.StringVar()
        text_box = ttk.Entry(frame, textvariable=text_var, font=("Roboto", 18))
        text_box.pack(fill="both", padx=6, pady=5)
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
        dropdown = ttk.Combobox(self.master, textvariable=dropdown_var, values=values, font=("Roboto", 17),
                                state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)

        # Calculate the width based on the longest item
        # max_item_width = max(len(item) for item in values)
        # dropdown.config(width=max_item_width)

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
        additional_text = "--var1=" + self.additional_text_var.get()
        selected_test = self.select_a_test_dropdown_var.get()

        registration_to_ready_command = "pytest ..//tests_compass_star/test_invitation_to_registration.py --rs -x -q -s"
        new_registration_to_ready_command = "pytest ..//tests_compass_star/test_invitation_to_registration_new.py --rs -x -q -s"
        transfer_supplier_command = "pytest ..//tests_compass_star/test_transfer_a_supplier.py --rs -x -q -s"
        pass_to_due_diligence_command = "pytest ..//tests_supplier_land/test_pass_to_due_diligence.py --rs -x -q -s"
        add_provisional_pre_request_command = "pytest ..//tests_supplier_land/test_add_provisional_pre_request.py --rs -x -q -s"
        add_confirmed_pre_request_command = "pytest ..//tests_supplier_land/test_add_confirmed_pre_request.py --rs -x -q -s"
        bsc_order_package_command = "pytest ..//tests_bsc/test_bsc_redeem_package.py --rs -x -q -s"
        upload_comms_template_command = "pytest ..//tests_compass_star/test_upload_comms_template.py --rs -x -q -s"
        practice_page_command = "pytest ..//test_runner/practice.py --rs -x -q -s"

        test_commands = {
            "Registration To Ready": [registration_to_ready_command, additional_text],
            "New Registration To Ready": [new_registration_to_ready_command, additional_text],
            "Transfer a Supplier": [transfer_supplier_command, additional_text],
            "Pass to Due Diligence": [pass_to_due_diligence_command, additional_text],
            "Add Provisional Pre Request": [add_provisional_pre_request_command, additional_text],
            "Add Confirmed Pre Request": [add_confirmed_pre_request_command, additional_text],
            "BSC Order Package": [bsc_order_package_command, additional_text],
            "Upload Communications Template": [upload_comms_template_command, additional_text],
            "Practice Page": [practice_page_command, additional_text]
        }

        # Get the value of the additional dropdown
        additional_dropdown_value = self.comms_template_dropdown_var.get()

        option_values = {
            "Select All": "--var2=all",
            "Vat Return": "--var2=vat",
            "Invoice Approval": "--var2=invoice",
            "Funding Request": "--var2=funding"

        }

        if selected_test in test_commands:
            pytest_command = test_commands[selected_test]
            pytest_command.append(option_values.get(additional_dropdown_value, ""))  # Get the corresponding option
        else:
            print("Please Select a Test")

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
