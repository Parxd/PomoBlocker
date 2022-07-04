import time
import threading
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import settings as settings


class App():
    start = False
    work = 1500
    shortbreak = 300
    longbreak = 900

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("800x600")
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure((0, 1), weight = 1)

        self.workframe = ctk.CTkFrame(
            self.root,
            width = 400
        )
        self.shortbreakframe = ctk.CTkFrame(
            self.root,
            width = 400
        )
        self.longbreakframe = ctk.CTkFrame(
            self.root,
            width = 400
        )
        for frame in (self.workframe, self.shortbreakframe, self.longbreakframe):
            frame.grid(
                row = 0,
                column = 1,
                sticky = "NSEW"
        )
        self.raise_frame(self.workframe)

        self.workframe.grid_rowconfigure((0, 1), weight = 1)
        self.workframe.grid_columnconfigure((0, 1, 2), weight = 1)
        self.shortbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.shortbreakframe.grid_columnconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1), weight = 1)

        self.worktime = ctk.CTkLabel(
            self.workframe,
            text = f"{self.work // 60} : 00",
            text_font = ("", 40)
        )
        self.worktime.grid(
            row = 0,
            column = 0,
            columnspan = 3
        )

        self.start_button = ctk.CTkButton(
            self.workframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10)
        )
        self.start_button.grid(
            row = 1,
            column = 0
        )
        self.stop_button = ctk.CTkButton(
            self.workframe,
            command = lambda: [
                self.start_bool(False), 
                self.start_bool
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10)
            )
        self.stop_button.grid(
            row = 1,
            column = 1
        )
        self.skip_button = ctk.CTkButton(
            self.workframe,
            text = "Skip",
            text_font = ("Roboto Medium", 10)
        )
        self.skip_button.grid(
            row = 1,
            column = 2)

    def start_bool(self, state):
        self.start = state

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    def startbutton(self):
        self.start_bool(True)
        thread = threading.Thread(target = self.worktimer)
        thread.daemon = True
        thread.start()

    def worktimer(self):
        while self.work > -1 and self.start:
            self.minute = self.work // 60
            self.second = self.work % 60
            self.worktime.configure(text = f"{self.minute:02d} : {self.second:02d}")
            self.root.update()
            time.sleep(1)
            self.work -= 1
            if self.start:
                self.start_button.config(state = tk.DISABLED)
            else:
                self.start_button.config(state = tk.NORMAL)


def main():
    app = App()
    app.root.mainloop()
    settings.Settings()


if __name__ == '__main__':
    main()
