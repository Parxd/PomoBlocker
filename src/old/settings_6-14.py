import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("System")


class Settings():
    def __init__(self):
        self.master = ctk.CTk()
        self.master.title("Settings")
        self.master.geometry("800x600")
        self.master.iconbitmap(
            "C:\\Users\\14253\\Important\\Interests\\Coding Projects\\PomoBlocker\\settings.ico"
        )
        self.master.resizable(False, False)
        self.master.grid_rowconfigure(0, weight = 1)
        self.master.grid_columnconfigure(1, weight = 1)
        self.entries = []
        self.websites = []

        self.darkbgimage = ImageTk.PhotoImage(Image.open(
            "C:\\Users\\14253\\Important\\Interests\\Coding Projects\\PomoBlocker\\bg.jpg"
        ))
        self.darkbgimagelabel = tk.Label(
            self.master,
            image = self.darkbgimage
        )
        self.darkbgimagelabel.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "NSEW"
        )

        ''' ----- Initialize tab frame & main three buttons ----- '''
        self.tabframe = ctk.CTkFrame(
            self.master,
            width = 150,
            corner_radius = 0,
        )
        self.tabframe.grid(
            row = 0,
            column = 0,
            sticky = "NESW"
        )
        self.tabframe.grid_rowconfigure(0, minsize=2)
        self.tabframe.grid_rowconfigure(5, weight=1)
        self.tabframe.grid_rowconfigure(7, minsize=20)
        self.tabframe.grid_rowconfigure(11, minsize=2)

        self.settings_title = ctk.CTkLabel(
            self.tabframe,
            text = "Settings",
            text_font = ("Roboto Medium", 18)
        )
        self.settings_title.grid(
            row = 1,
            column = 0,
            padx = 12,
            pady = 35
        )
        self.buttons_frame = ctk.CTkFrame(
            self.tabframe,
            width = 100,
            corner_radius = 8,
        )
        self.buttons_frame.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            rowspan = 3,
            padx = 10,
            pady = (10, 0),
            sticky = "NESW"
        )
        self.buttons_frame.rowconfigure(0, weight = 1)
        self.buttons_frame.columnconfigure(0, weight = 1)
        self.time_settings_button = ctk.CTkButton(
            self.buttons_frame,
            command = lambda : self.raise_frame(self.time_settings_frame),
            text = "Timers",
            text_font = ("Roboto Medium", 10),
            height = 40,
            width = 120,
            text_color = "#F4F0DB",
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.time_settings_button.grid(
            row = 2,
            column = 0,
            padx = 12,
            pady = (15, 55)
        )
        self.websites_settings_button = ctk.CTkButton(
            self.buttons_frame,
            command = lambda : self.raise_frame(self.websites_settings_frame),
            text = "Websites",
            text_font = ("Roboto Medium", 10),
            height = 40,
            width = 120,
            text_color = "#F4F0DB",
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.websites_settings_button.grid(
            row = 3,
            column = 0,
            padx = 12,
            pady = (0, 55)
        )
        self.notification_settings_button = ctk.CTkButton(
            self.buttons_frame,
            command = lambda : self.raise_frame(self.notifications_settings_frame),
            text = "Notifications",
            text_font = ("Roboto Medium", 10),
            height = 40,
            width = 120,
            text_color = "#F4F0DB",
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.notification_settings_button.grid(
            row = 4,
            column = 0,
            padx = 12,
            pady = (0, 15)
        )

        ''' -------- Initialize main three frames -------- '''
        self.time_settings_frame = ctk.CTkFrame(
            self.master,
            width = 200,
            corner_radius = 8
        )
        self.websites_settings_frame = ctk.CTkFrame(
            self.master,
            width = 200,
            corner_radius = 8
        )
        self.notifications_settings_frame = ctk.CTkFrame(
            self.master,
            width = 200,
            corner_radius = 8
        )
        for frame in (
            self.time_settings_frame,
            self.websites_settings_frame,
            self.notifications_settings_frame
            ):
            frame.grid(
                row = 0,
                column = 1,
                sticky = "NSEW",
                padx = 35,
                pady = 35
        )
        self.raise_frame(self.time_settings_frame)

        ''' ----- Initialize widgets inside the time settings frame ----- '''
        self.time_settings_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight = 1)
        self.time_settings_frame.grid_rowconfigure(3, weight = 10)
        self.time_settings_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight = 1)
        self.time_settings_frame.grid_columnconfigure(2, weight = 0)

        self.time_settings_instructions = ctk.CTkLabel(
            self.time_settings_frame,
            text = "Set custom times for each timer",
            text_font = ("Roboto Medium", 12),
            width = 150
        )
        self.time_settings_instructions.grid(
            row = 1,
            column = 0,
            columnspan = 5,
            padx = 12,
            pady = 18
        )

        self.inputsframe = ctk.CTkFrame(
            self.time_settings_frame,
            corner_radius = 10,
            width = 200,
            fg_color = "grey23"
        )
        self.inputsframe.grid(
            row = 2,
            column = 0,
            columnspan = 5,
            padx = 12,
            pady = (12, 0),
            sticky = "NESW"
        )
        self.inputsframe.grid_rowconfigure((0, 1, 2), weight = 1)
        self.inputsframe.grid_columnconfigure((0, 1, 2, 3), weight = 1)

        self.workimg = ImageTk.PhotoImage(Image.open(
            "C:\\Users\\14253\\Important\\Interests\\Coding Projects\\PomoBlocker\\working.png"
            ))
        self.workimglabel = ctk.CTkLabel(
            self.inputsframe,
            image = self.workimg,
            width = 5,
            height = 5
        )
        self.workimglabel.grid(
            row = 0,
            column = 0,
            pady = (30, 12)
        )
        self.worklabel = ctk.CTkLabel(
            self.inputsframe,
            text = "Work time",
            text_font = ("Helvetica Medium", 11),
        )
        self.worklabel.grid(
            row = 0,
            column = 1,
            pady = 10
        )
        self.workinput = ctk.CTkOptionMenu(
            self.inputsframe,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(15, 31)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.workinput.grid(
            row = 0,
            column = 2,
            pady = 10
        )
        self.workinput.set(25)

        self.shortbreakimg = ImageTk.PhotoImage(Image.open(
            "C:\\Users\\14253\\Important\\Interests\\Coding Projects\\PomoBlocker\\coffee.png"
        ))
        self.shortbreakimglabel = ctk.CTkLabel(
            self.inputsframe,
            image = self.shortbreakimg
        )
        self.shortbreakimglabel.grid(
            row = 1,
            column = 0,
            pady = 13
        )
        self.shortbreaklabel = ctk.CTkLabel(
            self.inputsframe,
            text = "Short break time",
            text_font = ("Helvetica Medium", 11)
        )
        self.shortbreaklabel.grid(
            row = 1,
            column = 1,
            pady = 6
        )
        self.shortbreakinput = ctk.CTkOptionMenu(
            self.inputsframe,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(5, 11)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.shortbreakinput.grid(
            row = 1,
            column = 2,
            pady = 10
        )

        self.longbreakimg = ImageTk.PhotoImage(Image.open(
          "C:\\Users\\14253\\Important\\Interests\\Coding Projects\\PomoBlocker\\pillow.png"  
        ))
        self.longbreakimglabel = ctk.CTkLabel(
            self.inputsframe,
            image = self.longbreakimg
        )
        self.longbreakimglabel.grid(
            row = 2,
            column = 0,
            pady = (12, 30)
        )
        self.longbreaklabel = ctk.CTkLabel(
            self.inputsframe,
            text = "Long break time",
            text_font = ("Helvetica Medium", 11)
        )
        self.longbreaklabel.grid(
            row = 2,
            column = 1,
            pady = 10
        )
        self.longbreakinput = ctk.CTkOptionMenu(
            self.inputsframe,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(15, 26)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.longbreakinput.grid(
            row = 2,
            column = 2,
            pady = 10
        )
        self.longbreakinput.set(15)

        self.autostart = ctk.CTkCheckBox(
            self.time_settings_frame,
            text = "Auto-start cycles?",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.autostart.grid(
            row = 3,
            column = 4,
            columnspan = 2,
            padx = (0, 35),
            pady = (0, 30)
        )

        # self.save = ctk.CTkButton(
        #     self.time_settings_frame,
        #     text = "Save",
        #     text_font = ("Roboto Medium", 10),
        #     width = 60,
        #     fg_color = "#FF775B",
        #     hover_color = "#FF9579"
        # )
        # self.save.grid(
        #     row = 4,
        #     column = 4,
        #     padx = 20,
        #     pady = (0, 18)
        # )
        # self.reset = ctk.CTkButton(
        #     self.time_settings_frame,
        #     command = self.reset_inputs,
        #     text = "Reset",
        #     text_font = ("Roboto Medium", 10),
        #     width = 60,
        #     text_color = "#FF775B",
        #     fg_color = "#2A2D2E",
        #     hover_color = "grey35"
        # )
        # self.reset.grid(
        #     row = 4,
        #     column = 3,
        #     padx = (0, 10),
        #     pady = (0, 18)
        # )

    def reset_inputs(self):
        self.workinput.set(25)
        self.shortbreakinput.set(5)
        self.longbreakinput.set(15)
        self.autostart.deselect()

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()


def main():
    settings = Settings()
    settings.master.mainloop()


if __name__ == '__main__':
    main()
