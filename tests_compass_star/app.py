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

        self.create_label("Select a Test:")
        self.select_a_test_dropdown_var = self.create_dropdown(
            ["Registration To Ready", "New Registration To Ready", "Transfer a Supplier", "Pass to Due Diligence", "Add Provisional Pre Request",
             "Add Confirmed Pre Request", "BSC Order Package",
             "Practice Page"])

        self.create_label("Select Staging Environment:")
        self.staging_dropdown_var = self.create_dropdown(
            ["QA Instance", "V1 Instance", "V2 Instance", "V3 Instance", "V4 Instance", "Echo Instance",
             "Replica Instance"])

        self.create_label("Select Browser:")
        self.select_browser_dropdown_var = self.create_dropdown(["Chrome", "Edge", "Firefox"])

        # Create a new frame for the additional text box
        self.additional_text_frame = ttk.Frame(self.master)
        self.additional_text_frame.pack(pady=20, padx=10, fill="both")

        # Create a LabelFrame for the checkboxes
        checkbox_frame = ttk.LabelFrame(self.master, text="Select Test Options:")
        checkbox_frame.pack(pady=20, padx=10, fill="both")

        # Create the additional text box and assign it to a variable
        self.additional_text_var = self.create_text_box(self.additional_text_frame, "Additional Options:")

        # Inside the LabelFrame, add checkboxes with tooltips
        self.demo_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Demo Mode",
                                                           "Slow down and visually see test actions as they occur.")

        self.slow_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Slow Mode",
                                                           "Slow down the automation.")

        self.report_checkbox_var = self.create_checkbox(checkbox_frame, "Generate Report",
                                                        "Creates a detailed pytest-html report after tests finish.")

        self.screenshot_checkbox_var = self.create_checkbox(checkbox_frame, "Save Screenshot",
                                                            "Save a screenshot at the end of each test.")

        self.incognito_mode_checkbox_var = self.create_checkbox(checkbox_frame, "Incognito Mode",
                                                                "Enable Chrome's Incognito mode.")
        self.start_window_maximize_var = self.create_checkbox(checkbox_frame, "Start Maximized",
                                                              "Start tests with the browser window maximized.")

        self.run_button = self.create_button("Run", lambda: self.run_pytest(), bg="green", fg="white", padx=20)
        self.quit_button = self.create_button("Quit", master.quit, bg="red", fg="white", padx=20)

    def create_text_box(self, frame, label_text):
        label = ttk.Label(frame, text=label_text, font=("Arial", 12, "bold"))
        label.pack(padx=10, pady=5)

        text_var = tk.StringVar()
        text_box = ttk.Entry(frame, textvariable=text_var, font=("Arial", 18))
        text_box.pack(fill="both", padx=10, pady=5)
        return text_var

    def create_label(self, text):
        label = tk.Label(self.master, text=text, font=("Arial", 18, "bold"), bg="lightgray")
        label.pack(pady=(20, 10))
        return label

    def create_label1(self, text):
        label = tk.Label(self.master, text=text, font=("Arial", 12, "bold"), bg="lightgray")
        label.pack(pady=(20, 10))
        return label

    def create_dropdown(self, values):

        def remove_highlight(event):
            event.widget.master.focus_set()

        dropdown_var = tk.StringVar()

        dropdown = ttk.Combobox(self.master, textvariable=dropdown_var, values=values, font=("Arial", 22),
                                state="readonly")
        dropdown.pack(fill="both", padx=10, pady=5)

        dropdown.bind("<FocusIn>", remove_highlight)
        return dropdown_var

    def create_checkbox(self, frame, text, tooltip_text):
        checkbox_var = tk.IntVar()
        checkbox = tk.Checkbutton(frame, text=text, variable=checkbox_var, font=("Arial", 12), bg="light gray", )
        checkbox.grid(column=0, row=len(frame.winfo_children()), sticky="w", pady=4)
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
        button = tk.Button(self.master, text=text, command=command, **kwargs, font=("Arial", 12, "bold"))
        button.pack(side="left", padx=(10, 10), pady=(0, 10), expand=True, fill="both")
        return button

    def run_pytest(self):

        additional_text = "--var1=" + self.additional_text_var.get()
        selected_test = self.select_a_test_dropdown_var.get()

        test_commands = {
            "Registration To Ready": ["pytest",
                                      "..//tests_compass_star/test_invitation_to_registration.py --rs -x -q -s",
                                      additional_text],
            "New Registration To Ready": ["pytest",
                                          "..//tests_compass_star/test_invitation_to_registration_new.py --rs -x -q -s",
                                          additional_text],
            "Transfer a Supplier": ["pytest",
                                    "..//tests_compass_star/test_transfer_a_supplier.py --rs -x -q -s",
                                    additional_text],
            "Pass to Due Diligence": ["pytest",
                                    "..//tests_supplier_land/test_pass_to_due_diligence.py --rs -x -q -s",
                                    additional_text],
            "Add Provisional Pre Request": ["pytest",
                                            "..//tests_supplier_land/test_add_provisional_pre_request.py --rs -x -q -s",
                                            additional_text],
            "Add Confirmed Pre Request": ["pytest",
                                          "..//tests_supplier_land/test_add_confirmed_pre_request.py --rs -x -q -s",
                                          additional_text],
            "BSC Order Package": ["pytest", "..//tests_bsc/test_bsc_redeem_package.py --rs -x -q -s",
                                  additional_text],
            "Practice Page": ["pytest", "..//test_runner/practice.py --rs -x -q -s", additional_text]
        }

        if selected_test in test_commands:
            pytest_command = test_commands[selected_test]
        else:
            print("Please Select a Test")

        options = {
            "--demo": self.demo_mode_checkbox_var.get(),
            "--html=report.html --dashboard": self.report_checkbox_var.get(),
            "--screenshot": self.screenshot_checkbox_var.get(),
            "--slow": self.slow_mode_checkbox_var.get(),
            "--incognito": self.incognito_mode_checkbox_var.get(),
            "--maximize": self.start_window_maximize_var.get()

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

        screen_log = subprocess.Popen(" ".join(pytest_command), shell=True)
        print(screen_log)


if __name__ == "__main__":
    root = tk.Tk()
    app = PytestRunnerApp(root)
    root.mainloop()
