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
    workstring = f"{work // 60:02d} : {work % 60:02d}"
    shortbreakstring = f"{shortbreak // 60:02d} : {shortbreak % 60:02d}"
    longbreakstring = f"{longbreak // 60:02d} : {longbreak % 60:02d}"
    pomocount = 0
    cycle_length = 7

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
        self.shortbreakframe.grid_columnconfigure((0, 1, 2), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1, 2), weight = 1)

        self.worktimevar = tk.StringVar(value = self.workstring)
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

        self.shortbreaktimevar = tk.StringVar(value = self.shortbreakstring)
        self.shortbreaktime = ctk.CTkLabel(
            self.shortbreakframe,
            textvariable = self.shortbreaktimevar,
            text_font = ("", 40)
        )
        self.shortbreaktime.grid(
            row = 0,
            column = 0,
            columnspan = 3
        )

        self.longbreaktimevar = tk.StringVar(value = self.longbreakstring)
        self.longbreaktime = ctk.CTkLabel(
            self.longbreakframe,
            textvariable = self.longbreaktimevar,
            text_font = ("", 40)
        )
        self.longbreaktime.grid(
            row = 0,
            column = 0,
            columnspan = 3
        )

        self.work_start_button = ctk.CTkButton(
            self.workframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10)
        )
        self.work_start_button.grid(
            row = 1,
            column = 0
        )
        self.work_stop_button = ctk.CTkButton(
            self.workframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10)
            )
        self.work_stop_button.grid(
            row = 1,
            column = 1
        )
        self.work_skip_button = ctk.CTkButton(
            self.workframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10)
        )
        self.work_skip_button.grid(
            row = 1,
            column = 2)

        self.short_start_button = ctk.CTkButton(
            self.shortbreakframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10)
        )
        self.short_start_button.grid(
            row = 1,
            column = 0
        )
        self.short_stop_button = ctk.CTkButton(
            self.shortbreakframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10)
        )
        self.short_stop_button.grid(
            row = 1,
            column = 1
        )
        self.short_skip_button = ctk.CTkButton(
            self.shortbreakframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10)
        )
        self.short_skip_button.grid(
            row = 1,
            column = 2
        )

        self.long_start_button = ctk.CTkButton(
            self.longbreakframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10)
        )
        self.long_start_button.grid(
            row = 1,
            column = 0
        )
        self.long_stop_button = ctk.CTkButton(
            self.longbreakframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10)
        )
        self.long_stop_button.grid(
            row = 1,
            column = 1
        )
        self.long_skip_button = ctk.CTkButton(
            self.longbreakframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10)
        )
        self.long_skip_button.grid(
            row = 1,
            column = 2
        )

    def start_bool(self, state):
        self.start = state

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    def startbutton(self):
        self.start_bool(True)
        thread = threading.Thread(target = self.timer)
        thread.daemon = True
        thread.start()

    def skipbutton(self):
        skip = messagebox.askyesno(
            "Warning",
            "Are you sure you want to skip the remaining time?"
        )
        if self.frame == self.workframe:
            if skip:
                self.pomocount += 1
                if not self.pomocount % self.cycle_length:
                    self.raise_frame(self.longbreakframe)
                    self.worktimevar.set(self.workstring)
                    self.work_start_button.configure(state = tk.NORMAL)
                else:
                    self.raise_frame(self.shortbreakframe)
                    self.start_bool(False)
                    self.worktimevar.set(self.workstring)
                    self.work_start_button.configure(state = tk.NORMAL)
        elif self.frame == self.shortbreakframe:
            if skip:
                self.pomocount += 1
                self.raise_frame(self.workframe)
                self.start_bool(False)
                self.shortbreaktimevar.set(self.shortbreakstring)
                self.short_start_button.configure(state = tk.NORMAL)
        elif self.frame == self.longbreakframe:
            if skip:
                self.raise_frame(self.workframe)
                self.start_bool(False)
                self.longbreaktimevar.set(self.longbreakstring)
                self.long_start_button.configure(state = tk.NORMAL)

    def timer(self):
        if self.frame == self.workframe:
            if self.start:
                self.work_start_button.configure(state = tk.DISABLED)
            else:
                self.work_start_button.configure(state = tk.NORMAL)

            # self.work = 1500
            while self.work > -1 and self.start:
                seconds = self.work % 60
                minutes = self.work // 60
                self.worktimevar.set(value = f"{minutes:02d} : {seconds % 60:02d}")
                self.root.update()
                time.sleep(1)
                self.work -= 1
            try:
                if not seconds and not minutes:
                    self.start_bool(False)
                    self.pomocount += 1
                    if not self.pomocount % self.cycle_length:
                        self.raise_frame(self.longbreakframe)
                        self.worktimevar.set(self.workstring)
                        self.work_start_button.configure(state = tk.NORMAL)
                    else:
                        self.raise_frame(self.shortbreakframe)
                        self.worktimevar.set(self.workstring)
                        self.work_start_button.configure(state = tk.NORMAL)
            except UnboundLocalError:
                pass

        elif self.frame == self.shortbreakframe:
            if self.start:
                self.short_start_button.configure(state = tk.DISABLED)
            else:
                self.short_start_button.configure(state = tk.NORMAL)

            self.shortbreak = 300
            while self.shortbreak > -1 and self.start:
                seconds = self.shortbreak % 60
                minutes = self.shortbreak // 60
                self.shortbreaktimevar.set(value = f"{minutes:02d} : {seconds % 60:02d}")
                self.root.update()
                time.sleep(1)
                self.shortbreak -= 1
            try:
                if not seconds and not minutes:
                    self.start_bool(False)
                    self.pomocount += 1
                    self.raise_frame(self.workframe)
                    self.shortbreaktimevar.set(self.shortbreakstring)
                    self.short_start_button.configure(state = tk.NORMAL)
            except UnboundLocalError:
                pass

        else:
            if self.start:
                self.long_start_button.configure(state = tk.DISABLED)
            else:
                self.long_start_button.configure(state = tk.NORMAL)

            self.longbreak = 900
            while self.longbreak > -1 and self.start:
                seconds = self.longbreak % 60
                minutes = self.longbreak // 60
                self.longbreaktimevar.set(value = f"{minutes:02d} : {seconds % 60:02d}")
                self.root.update()
                time.sleep(1)
                self.longbreak -= 1
            try:
                if not seconds and not minutes:
                    self.start_bool(False)
                    self.raise_frame(self.workframe)
                    self.longbreaktimevar.set(self.longbreakstring)
                    self.long_start_button.configure(state = tk.NORMAL)
            except UnboundLocalError:
                pass


def main():
    app = App()
    app.root.mainloop()


if __name__ == "__main__":
    main()
