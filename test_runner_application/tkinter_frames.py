import customtkinter
import tkinterDnD


class TkinterFrames:

    def main_page_frame(self, frame):
        frame_1 = customtkinter.CTkFrame(master=frame)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    def check_box_frame(self, frame):
        checkbox_frame = customtkinter.CTkFrame(master=frame)
        checkbox_frame.pack(pady=10, padx=10)


