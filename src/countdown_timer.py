import time
import threading
import tkinter as tk
from turtle import goto
import customtkinter as ctk


class App():
    go = False
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
        self.workframe.grid_columnconfigure((0, 1), weight = 1)
        self.shortbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.shortbreakframe.grid_columnconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1), weight = 1)

        self.workminutes = tk.StringVar()
        self.workminutelabel = ctk.CTkLabel(
            self.workframe,
            textvariable = self.workminutes,
            text_font = ("Roboto Medium", 30)
        )
        self.workminutelabel.grid(
            row = 0,
            column = 0
        )
        self.workseconds = tk.StringVar()
        self.worksecondlabel = ctk.CTkLabel(
            self.workframe,
            textvariable = self.workseconds,
            text_font = ("Roboto Medium", 30)
        )
        self.worksecondlabel.grid(
            row = 0,
            column = 1
        )

        self.workminutes.set("25")
        self.workseconds.set("00")

        self.start = ctk.CTkButton(
            self.workframe,
            command = lambda: [self.start_bool(True), threading.Thread(target = self.worktimer).start()],
            text = "Start",
            text_font = ("Roboto Medium", 10)
        )
        self.start.grid(
            row = 1,
            column = 0
        )
        self.stop = ctk.CTkButton(
            self.workframe,
            command = lambda: [self.start_bool(False), threading.Thread(target = self.worktimer).start()],
            text = "Stop",
            text_font = ("Roboto Medium", 10)
            )
        self.stop.grid(
            row = 1,
            column = 1
        )

    def start_bool(self, state):
        self.go = state

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    def worktimer(self):
        while self.work and self.go:
            self.minute = self.work // 60
            self.second = self.work % 60
            self.workminutes.set(self.minute)
            self.workseconds.set(self.second)
            self.workminutes.set(f"{self.minute:02d}")
            self.workseconds.set(f"{self.second:02d}")
            self.root.update()
            time.sleep(1)
            self.work -= 1


def main():
    app = App()
    app.root.mainloop()


if __name__ == '__main__':
    main()
