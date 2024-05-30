import customtkinter
import tkinterDnD


class TkinterControls:


    def segmented_button(self, frame, update_label):
        segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame, values=["CSL PROCESS", "SL PROCESS", "BSC PROCESS", "BROMSGROVE PROCESS"], command=update_label)
        segmented_button_1.pack(pady=30, padx=30)

    def select_module_label(self, frame):
        module_label = customtkinter.CTkLabel(master=frame, justify=customtkinter.LEFT, text="Select a module", font=("Arial", 30))
        module_label.pack(pady=5, padx=10)

    def select_a_process_dropdown(self, frame):
        process_dropdown = customtkinter.CTkOptionMenu(frame, values=["Registration To Ready", "Add Provisional Pre Request", "Add Confirmed Pre Request"], width=442, height=40, font=("Arial", 25))
        process_dropdown.pack(pady=10, padx=10)
        process_dropdown.set("Select a process")

    def demo_mode_checkbox(self, frame):
        checkbox_1 = customtkinter.CTkCheckBox(master=frame, text="Demo Mode")
        checkbox_1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def create_segmented_button(self, frame, command):
        return customtkinter.CTkSegmentedButton(master=frame, values=["CSL PROCESS", "SL PROCESS", "BSC PROCESS", "BROMSGROVE PROCESS"], command=command)
