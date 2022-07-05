import time
import threading
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class App():
    start = False
    work = 1500
    shortbreak = 300
    longbreak = 900
    pomocount = 0

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("800x600")
        self.root.grid_rowconfigure((0, 1, 2), weight = 1)
        self.root.grid_columnconfigure((0, 1), weight = 1)

        self.workframe = ctk.CTkFrame(
            self.root,
            width = 500
        )
        self.shortbreakframe = ctk.CTkFrame(
            self.root,
            width = 500
        )
        self.longbreakframe = ctk.CTkFrame(
            self.root,
            width = 500
        )
        for frame in (self.workframe, self.shortbreakframe, self.longbreakframe):
            frame.grid(
                row = 0,
                column = 1,
                rowspan = 3,
                sticky = "NSEW"
        )
        self.raise_frame(self.workframe)

        self.showworkframe = ctk.CTkButton(
            self.root,
            command = lambda: self.raise_frame(self.workframe),
            text = "Work",
            text_font = ("Roboto Medium", 12)
        )
        self.showworkframe.grid(
            row = 0,
            column = 0
        )
        self.showshortbreakframe = ctk.CTkButton(
            self.root,
            command = lambda: self.raise_frame(self.shortbreakframe),
            text = "Short break",
            text_font = ("Roboto Medium", 12)
        )
        self.showshortbreakframe.grid(
            row = 1,
            column = 0
        )
        self.showlongbreakframe = ctk.CTkButton(
            self.root,
            command = lambda: self.raise_frame(self.longbreakframe),
            text = "Long break",
            text_font = ("Roboto Medium", 12)
        )
        self.showlongbreakframe.grid(
            row = 2,
            column = 0
        )

        self.workframe.grid_rowconfigure((0, 1), weight = 1)
        self.workframe.grid_columnconfigure((0, 1, 2), weight = 1)
        self.shortbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.shortbreakframe.grid_columnconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1), weight = 1)

        self.worktimevar = tk.StringVar(value = f"{self.work // 60:02d} : {self.work % 60:02d}")
        self.worktime = ctk.CTkLabel(
            self.workframe,
            textvariable = self.worktimevar,
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
                self.worktimer()
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
            command = self.skipbutton,
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

    def skipbutton(self):
        self.pomocount += 1
        self.start_bool(False)
        self.worktimevar.set(value = "00 : 00")
        messagebox.showinfo(
            "Alert",
            "Time's up!"
        )
        self.raise_frame(self.shortbreakframe)

    def worktimer(self):
        if self.start:
            self.start_button.configure(state = tk.DISABLED)
        else:
            self.start_button.configure(state = tk.NORMAL)

        while self.work > -1 and self.start:
            seconds = self.work % 60
            minutes = self.work // 60
            self.worktimevar.set(value = f"{minutes:02d} : {seconds % 60:02d}")
            self.root.update()
            time.sleep(1)
            self.work -= 1
            if not seconds and not minutes:
                self.skipbutton()


def main():
    app = App()
    app.root.mainloop()
    print(app.pomocount)


if __name__ == "__main__":
    main()
