from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("dark")


class App():
    start = False
    work = 1500
    shortbreak = 300
    longbreak = 900
    workstring = f"{work // 60:02d} : {work % 60:02d}"
    shortbreakstring = f"{shortbreak // 60:02d} : {shortbreak % 60:02d}"
    longbreakstring = f"{longbreak // 60:02d} : {longbreak % 60:02d}"
    pomocount = 0
    cycle_length = 7

    def __init__(self):
        self.master = ctk.CTk()
        self.master.geometry("800x600")
        self.master.title("PomoBlocker")
        self.master.iconbitmap(
            Path(__file__).parent / "..\\res\\media\\pomodoro.ico"
        )
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(1, weight = 1)

        self.topframe = ctk.CTkFrame(
            self.master,
            width = 150,
            corner_radius = 8,
        )
        self.topframe.grid(
            row = 0,
            column = 0,
            sticky = "EW",
            padx = 20,
            pady = 15
        )
        self.topframe.grid_rowconfigure((0, 1), weight = 1)
        self.topframe.grid_columnconfigure(0, weight = 1)
        self.title_label = ctk.CTkLabel(
            self.topframe,
            text = "PomoBlocker",
            text_font = ("Roboto Medium", 18),
            text_color = "#F48269"
        )
        self.title_label.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = (20, 5)
        )

        self.buttonsframe = ctk.CTkFrame(
            self.topframe,
            height = 100,
            width = 800
        )
        self.buttonsframe.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = 20,
            sticky = "NESW"
        )
        self.buttonsframe.grid_rowconfigure(0, weight = 1)
        self.buttonsframe.grid_columnconfigure((0, 1, 2), weight = 1)

        self.showworkframe = ctk.CTkButton(
            self.buttonsframe,
            text = "Work",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            text_font = ("Roboto Medium", 10)
        )
        self.showworkframe.grid(
            row = 0,
            column = 0,
            padx = 20
        )
        self.showshortbreakframe = ctk.CTkButton(
            self.buttonsframe,
            text = "Short Break",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            text_font = ("Roboto Medium", 10)
        )
        self.showshortbreakframe.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 20
        )
        self.showlongbreakframe = ctk.CTkButton(
            self.buttonsframe,
            text = "Long Break",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            text_font = ("Roboto Medium", 10)
        )
        self.showlongbreakframe.grid(
            row = 0,
            column = 2,
            padx = 20
        )

        self.workframe = ctk.CTkFrame(
            self.master
        )
        self.workframe.grid(
            row = 1,
            column = 0,
            sticky = "NESW",
            padx = 20,
            pady = (0, 16)
        )
        self.shortbreakframe = ctk.CTkFrame(
            self.master
        )
        self.longbreakframe = ctk.CTkFrame(
            self.master
        )
        self.workframe.grid_rowconfigure((0, 1), weight = 1)
        self.workframe.grid_columnconfigure((0, 1, 2), weight = 1)
        self.shortbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.shortbreakframe.grid_columnconfigure((0, 1, 2), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1, 2), weight = 1)


def main():
    app = App()
    app.master.mainloop()


if __name__ == '__main__':
    main()
