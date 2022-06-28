import time
import threading
import tkinter as tk
import customtkinter as ctk


class App():
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

        self.workminutes.set("00")
        self.workseconds.set("00")
        threading.Thread(target = self.worktimer).start()

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    def worktimer(self):
        while self.work > 0:
            self.minute, self.second = divmod(self.work, 60)
            self.workminutes.set(self.minute)
            self.workseconds.set(self.second)
            time.sleep(1)
            self.work -= 1
            self.root.update()


def main():
    app = App()
    app.root.mainloop()


if __name__ == '__main__':
    main()
