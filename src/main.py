import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App():
    def __init__(self):
        self.master = ctk.CTk()
        self.master.title("PomoBlocker")
        self.master.iconbitmap(
            "..\\res\\media\\pomodoro.ico"
        )
        self.entries = []
        self.websites = []
        self.darkbgimage = ImageTk.PhotoImage(Image.open(
            "..\\res\\media\\bg.jpg"
        ))
        self.darkbgimagelabel = tk.Label(
            self.master,
            image = self.darkbgimage
        )
        self.darkbgimagelabel.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            rowspan = 3,
            sticky = "NSEW"
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
        self.mainframe = ctk.CTkFrame(
            self.master,
            width = 200
        )
        self.mainframe.grid(
            row = 1,
            column = 0,
            sticky = "NESW",
            padx = 20,
            pady = (0, 16)
        )

        self.topframe.grid_rowconfigure(0, minsize=10)
        self.topframe.grid_rowconfigure(5, weight=1)
        self.topframe.grid_rowconfigure(8, minsize=20)
        self.topframe.grid_rowconfigure(11, minsize=10)

        self.title_label = ctk.CTkLabel(
            self.topframe,
            text = "PomoBlocker",
            text_font = ("Roboto Medium", 18),
            text_color = "#FF775B"
        )
        self.title_label.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = (12, 2)
        )


def main():
    app = App()
    app.master.mainloop()


if __name__ == '__main__':
    main()
