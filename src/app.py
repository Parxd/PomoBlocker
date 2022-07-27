import time
import threading
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter as ctk
from playsound import playsound
from win10toast import ToastNotifier
from settings import Settings
from blocker import block

ctk.set_appearance_mode("dark")


class App():
    start = False
    work_const = 1500
    work = work_const
    shortbreak_const = 300
    shortbreak = shortbreak_const
    longbreak_const = 900
    longbreak = longbreak_const
    workstring = f"{work_const // 60:02d} : {work_const % 60:02d}"
    shortbreakstring = f"{shortbreak_const // 60:02d} : {shortbreak_const % 60:02d}"
    longbreakstring = f"{longbreak_const // 60:02d} : {longbreak_const % 60:02d}"
    workcount = 0
    workcycles = 4
    notification = 1

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x700")
        self.root.title("PomoBlocker")
        self.root.iconbitmap(
            Path(__file__).parent / "..\\res\\media\\pomodoro.ico"
        )
        self.root.grid_columnconfigure(0, weight = 1, uniform = "column")
        self.root.grid_columnconfigure(1, weight = 1, uniform = "column")
        self.root.grid_columnconfigure(2, weight = 1, uniform = "column")
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_rowconfigure(1, weight = 2)
        self.root.grid_rowconfigure(2, weight = 12)

        self.title_label = ctk.CTkLabel(
            self.root,
            text = "PomoBlocker",
            text_font = ("Roboto Medium", 24),
            text_color = "#FFFFFF"
        )
        self.title_label.grid(
            row = 0,
            column = 1,
            sticky = "S"
        )

        self.workframe = ctk.CTkFrame(
            self.root
        )
        self.workframe.grid(
            row = 1,
            column = 0,
            sticky = "NESW",
            padx = 20,
            pady = (0, 16)
        )
        self.shortbreakframe = ctk.CTkFrame(
            self.root
        )
        self.longbreakframe = ctk.CTkFrame(
            self.root
        )
        self.workframe.grid_rowconfigure((0, 1, 2), weight = 1)
        self.workframe.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.shortbreakframe.grid_rowconfigure((0, 1, 2), weight = 1)
        self.shortbreakframe.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.longbreakframe.grid_rowconfigure((0, 1, 2), weight = 1)
        self.longbreakframe.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        for frame in (self.workframe, self.shortbreakframe, self.longbreakframe):
                    frame.grid(
                        row = 2,
                        column = 0,
                        columnspan = 3,
                        sticky = "NESW",
                        padx = 20,
                        pady = (0, 20)
                    )
        self.raise_frame(self.workframe)

        self.buttonsframe = ctk.CTkFrame(
            self.root,
            height = 100
        )
        self.buttonsframe.grid(
            row = 1,
            column = 0,
            columnspan = 3,
            padx = 20,
            sticky = "EW"
        )
        self.buttonsframe.grid_rowconfigure(0, weight = 1)
        self.buttonsframe.grid_columnconfigure((0, 1, 2), weight = 1)

        self.showworkframe = ctk.CTkButton(
            self.buttonsframe,
            command = lambda: self.raise_frame(self.workframe),
            text = "Work",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            hover_color = "#FF8B6F",
            text_font = ("Roboto Medium", 11)
        )
        self.showworkframe.grid(
            row = 0,
            column = 0,
            padx = 20
        )
        self.showshortbreakframe = ctk.CTkButton(
            self.buttonsframe,
            command = lambda: self.raise_frame(self.shortbreakframe),
            text = "Short Break",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            hover_color = "#FF8B6F",
            text_font = ("Roboto Medium", 11)
        )
        self.showshortbreakframe.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 20
        )
        self.showlongbreakframe = ctk.CTkButton(
            self.buttonsframe,
            command = lambda: self.raise_frame(self.longbreakframe),
            text = "Long Break",
            width = 200,
            height = 35,
            fg_color = "#FF775B",
            hover_color = "#FF8B6F",
            text_font = ("Roboto Medium", 11)
        )
        self.showlongbreakframe.grid(
            row = 0,
            column = 2,
            padx = 20
        )

        menuimage = ImageTk.PhotoImage(Image.open(
            Path(__file__).parent / "../res/media/menu.png"
            ))
        self.showmenu = ctk.CTkButton(
            self.root,
            command = self.show_menu,
            text = "",
            image = menuimage,
            width = 60,
            fg_color = "#212325",
            hover_color = "#FF775B"
        )
        self.showmenu.grid(
            row = 0,
            column = 0,
            sticky = "SW",
            padx = (30, 0)
        )
        self.menuframe = ctk.CTkFrame(
            self.root,
            fg_color = "#26282A"
        )
        self.menuframe.grid_rowconfigure(0, weight = 2)
        self.menuframe.grid_rowconfigure(1, weight = 3)
        self.menuframe.grid_rowconfigure(2, weight = 3)
        self.menuframe.grid_rowconfigure(3, weight = 3)
        self.menuframe.grid_columnconfigure(0, weight = 1)
        closeimage = ImageTk.PhotoImage(Image.open(
           Path(__file__).parent / "../res/media/close.png"
            ))
        self.closemenu = ctk.CTkButton(
            self.menuframe,
            command = self.close,
            text = "",
            image = closeimage,
            fg_color = "#26282A",
            hover_color = "#26282A"
        )
        self.closemenu.grid(
            row = 0,
            column = 0,
            padx = 35
        )
        loginimage = ImageTk.PhotoImage(Image.open(
           Path(__file__).parent / "../res/media/login.png"
            ))
        self.login = ctk.CTkButton(
            self.menuframe,
            command = self.open_login,
            text = "",
            image = loginimage,
            height = 75,
            text_font = ("Roboto Medium", 10),
            fg_color = "#26282A",
            hover_color = "#FF775B"
        )
        self.login.grid(
            row = 3,
            column = 0,
            padx = 35
        )
        reportimage = ImageTk.PhotoImage(Image.open(
           Path(__file__).parent / "../res/media/report.png"
            ))
        self.report = ctk.CTkButton(
            self.menuframe,
            command = self.open_summary,
            text = "",
            image = reportimage,
            height = 75,
            text_font = ("Roboto Medium", 10),
            fg_color = "#26282A",
            hover_color = "#FF775B"
        )
        self.report.grid(
            row = 2,
            column = 0,
            padx = 35
        )
        settingsimage = ImageTk.PhotoImage(Image.open(
           Path(__file__).parent / "../res/media/settings_menu.png"
            ))
        self.settings = ctk.CTkButton(
            self.menuframe,
            command = self.open_settings,
            text = "",
            image = settingsimage,
            height = 75,
            text_font = ("Roboto Medium", 10),
            fg_color = "#26282A",
            hover_color = "#FF775B"
        )
        self.settings.grid(
            row = 1,
            column = 0,
            padx = 35
        )

        self.worktimevar = tk.StringVar(value = self.workstring)
        self.worktime = ctk.CTkLabel(
            self.workframe,
            textvariable = self.worktimevar,
            text_font = ("Roboto Medium", 40)
        )
        self.worktime.grid(
            row = 0,
            column = 0,
            columnspan = 4
        )
        self.shortbreaktimevar = tk.StringVar(value = self.shortbreakstring)
        self.shortbreaktime = ctk.CTkLabel(
            self.shortbreakframe,
            textvariable = self.shortbreaktimevar,
            text_font = ("Roboto Medium", 40)
        )
        self.shortbreaktime.grid(
            row = 0,
            column = 0,
            columnspan = 4
        )
        self.longbreaktimevar = tk.StringVar(value = self.longbreakstring)
        self.longbreaktime = ctk.CTkLabel(
            self.longbreakframe,
            textvariable = self.longbreaktimevar,
            text_font = ("Roboto Medium", 40)
        )
        self.longbreaktime.grid(
            row = 0,
            column = 0,
            columnspan = 4
        )

        self.workcounterw = ctk.CTkLabel(
            self.workframe,
            text = f"0 / {self.workcycles}",
            text_font = ("Roboto Medium", 15)
        )
        self.workcounterw.grid(
            row = 1,
            column = 0,
            columnspan = 4
        )
        self.workcountersb = ctk.CTkLabel(
            self.shortbreakframe,
            text = f"0 / {self.workcycles}",
            text_font = ("Roboto Medium", 15)
        )
        self.workcountersb.grid(
            row = 1,
            column = 0,
            columnspan = 4
        )
        self.workcounterlb = ctk.CTkLabel(
            self.longbreakframe,
            text = f"0 / {self.workcycles}",
            text_font = ("Roboto Medium", 15)
        )
        self.workcounterlb.grid(
            row = 1,
            column = 0,
            columnspan = 4
        )

        self.work_start_button = ctk.CTkButton(
            self.workframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.work_start_button.grid(
            row = 2,
            column = 0
        )
        self.work_stop_button = ctk.CTkButton(
            self.workframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
            )
        self.work_stop_button.grid(
            row = 2,
            column = 1
        )
        self.work_skip_button = ctk.CTkButton(
            self.workframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.work_skip_button.grid(
            row = 2,
            column = 2)
        self.work_restart_button = ctk.CTkButton(
            self.workframe,
            command = self.restart,
            text = "Restart",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.work_restart_button.grid(
            row = 2,
            column = 3
        )

        self.short_start_button = ctk.CTkButton(
            self.shortbreakframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.short_start_button.grid(
            row = 2,
            column = 0
        )
        self.short_stop_button = ctk.CTkButton(
            self.shortbreakframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.short_stop_button.grid(
            row = 2,
            column = 1
        )
        self.short_skip_button = ctk.CTkButton(
            self.shortbreakframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.short_skip_button.grid(
            row = 2,
            column = 2
        )
        self.short_restart_button = ctk.CTkButton(
            self.shortbreakframe,
            command = self.restart,
            text = "Restart",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.short_restart_button.grid(
            row = 2,
            column = 3
        )

        self.long_start_button = ctk.CTkButton(
            self.longbreakframe,
            command = self.startbutton,
            text = "Start",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.long_start_button.grid(
            row = 2,
            column = 0
        )
        self.long_stop_button = ctk.CTkButton(
            self.longbreakframe,
            command = lambda: [
                self.start_bool(False), 
                self.timer()
                ],
            text = "Stop",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.long_stop_button.grid(
            row = 2,
            column = 1
        )
        self.long_skip_button = ctk.CTkButton(
            self.longbreakframe,
            command = self.skipbutton,
            text = "Skip",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.long_skip_button.grid(
            row = 2,
            column = 2
        )
        self.long_restart_button = ctk.CTkButton(
            self.longbreakframe,
            command = self.restart,
            text = "Restart",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF8B6F"
        )
        self.long_restart_button.grid(
            row = 2,
            column = 3
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
                self.workcount += 1
                self.workcounterw.configure(text = f"{self.workcount} / {self.workcycles}")
                self.workcountersb.configure(text = f"{self.workcount} / {self.workcycles}")
                self.workcounterlb.configure(text = f"{self.workcount} / {self.workcycles}")
                self.work = self.work_const
                self.showshortbreakframe.configure(state = tk.NORMAL)
                self.showlongbreakframe.configure(state = tk.NORMAL)
                if self.workcount == self.workcycles:
                    self.longbreak = self.longbreak_const
                    self.longbreaktimevar.set(self.longbreakstring)

                    self.workcounterw.configure(text_color = "#FF775B")
                    self.workcountersb.configure(text_color = "#FF775B")
                    self.workcounterlb.configure(text_color = "#FF775B")
                    self.raise_frame(self.longbreakframe)
                    self.worktimevar.set(self.workstring)
                    self.work_start_button.configure(state = tk.NORMAL)
                    self.showworkframe.configure(state = tk.DISABLED)
                    self.showshortbreakframe.configure(state = tk.DISABLED)
                else:
                    self.shortbreak = self.shortbreak_const
                    self.shortbreaktimevar.set(self.shortbreakstring)

                    self.raise_frame(self.shortbreakframe)
                    self.start_bool(False)
                    self.worktimevar.set(self.workstring)
                    self.work_start_button.configure(state = tk.NORMAL)
        elif self.frame == self.shortbreakframe:
            if skip:
                self.shortbreak = self.shortbreak_const
                self.showworkframe.configure(state = tk.NORMAL)
                self.showlongbreakframe.configure(state = tk.NORMAL)
                self.raise_frame(self.workframe)
                self.start_bool(False)

                self.work = self.work_const
                self.worktimevar.set(self.workstring)
                self.shortbreaktimevar.set(self.shortbreakstring)
                self.short_start_button.configure(state = tk.NORMAL)
        else:
            if skip:
                self.showworkframe.configure(state = tk.NORMAL)
                self.showshortbreakframe.configure(state = tk.NORMAL)
                self.longbreak = self.longbreak_const
                self.raise_frame(self.workframe)
                self.start_bool(False)

                self.work = self.work_const
                self.worktimevar.set(self.workstring)
                self.longbreaktimevar.set(self.longbreakstring)
                self.long_start_button.configure(state = tk.NORMAL)
                if self.workcount == self.workcycles:
                    self.workcount = 0
                    self.workcounterw.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.workcountersb.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.workcounterlb.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.workcounterw.configure(text_color = "#FFFFFF")
                    self.workcountersb.configure(text_color = "#FFFFFF")
                    self.workcounterlb.configure(text_color = "#FFFFFF")

    def timer(self):
        if self.frame == self.workframe:
            if self.start:
                self.work_start_button.configure(state = tk.DISABLED)
                self.showshortbreakframe.configure(state = tk.DISABLED)
                self.showlongbreakframe.configure(state = tk.DISABLED)
            else:
                self.work_start_button.configure(state = tk.NORMAL)

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
                    self.workcount += 1
                    self.workcounterw.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.workcountersb.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.workcounterlb.configure(text = f"{self.workcount} / {self.workcycles}")
                    self.work = self.work_const
                    self.showshortbreakframe.configure(state = tk.NORMAL)
                    self.showlongbreakframe.configure(state = tk.NORMAL)
                    if self.workcount == self.workcycles:
                        self.workcounterw.configure(text_color = "#FF775B")
                        self.workcountersb.configure(text_color = "#FF775B")
                        self.workcounterlb.configure(text_color = "#FF775B")
                        self.raise_frame(self.longbreakframe)
                        self.worktimevar.set(self.workstring)
                        self.work_start_button.configure(state = tk.NORMAL)
                        self.showworkframe.configure(state = tk.DISABLED)
                        self.showshortbreakframe.configure(state = tk.DISABLED)
                        try:
                            self.notifications()
                        except AttributeError:
                            pass
                    else:
                        self.raise_frame(self.shortbreakframe)
                        self.worktimevar.set(self.workstring)
                        self.work_start_button.configure(state = tk.NORMAL)

                        try:
                            self.notifications()
                        except AttributeError:
                            pass
            except UnboundLocalError: # To prevent errors when using stop button
                pass

        elif self.frame == self.shortbreakframe:
            if self.start:
                self.short_start_button.configure(state = tk.DISABLED)
                self.showworkframe.configure(state = tk.DISABLED)
                self.showlongbreakframe.configure(state = tk.DISABLED)
            else:
                self.short_start_button.configure(state = tk.NORMAL)

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
                    self.shortbreak = self.shortbreak_const
                    self.showworkframe.configure(state = tk.NORMAL)
                    self.showlongbreakframe.configure(state = tk.NORMAL)
    
                    self.raise_frame(self.workframe)
                    self.work = self.work_const
                    self.worktimevar.set(self.workstring)
                    self.shortbreaktimevar.set(self.shortbreakstring)
                    self.short_start_button.configure(state = tk.NORMAL)

                    try:
                        self.notifications()
                    except AttributeError:
                        pass
            except UnboundLocalError:
                pass

        else:
            if self.start:
                self.long_start_button.configure(state = tk.DISABLED)
                self.showworkframe.configure(state = tk.DISABLED)
                self.showshortbreakframe.configure(state = tk.DISABLED)
            else:
                self.long_start_button.configure(state = tk.NORMAL)

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
                    self.showworkframe.configure(state = tk.NORMAL)
                    self.showshortbreakframe.configure(state = tk.NORMAL)
                    self.longbreak = self.longbreak_const

                    self.raise_frame(self.workframe)
                    self.work = self.work_const
                    self.worktimevar.set(self.workstring)
                    self.longbreaktimevar.set(self.longbreakstring)
                    self.long_start_button.configure(state = tk.NORMAL)
                    if self.workcount == self.workcycles:
                        self.workcount = 0
                        self.workcounterw.configure(text = f"{self.workcount} / {self.workcycles}")
                        self.workcountersb.configure(text = f"{self.workcount} / {self.workcycles}")
                        self.workcounterlb.configure(text = f"{self.workcount} / {self.workcycles}")
                        self.workcounterw.configure(text_color = "#FFFFFF")
                        self.workcountersb.configure(text_color = "#FFFFFF")
                        self.workcounterlb.configure(text_color = "#FFFFFF")

                    try:
                        self.notifications()
                    except AttributeError:
                        pass
            except UnboundLocalError:
                pass
    
    def restart(self):
        if self.frame == self.workframe:
            self.work = self.work_const
            self.worktimevar.set(self.workstring)
            self.start_bool(False)
            self.work_start_button.configure(state = tk.NORMAL)
        elif self.frame == self.shortbreakframe:
            self.shortbreak = self.shortbreak_const
            self.shortbreaktimevar.set(self.shortbreakstring)
            self.start_bool(False)
            self.short_start_button.configure(state = tk.NORMAL)
        else:
            self.longbreak = self.longbreak_const
            self.longbreaktimevar.set(self.longbreakstring)
            self.start_bool(False)
            self.long_start_button.configure(state = tk.NORMAL)
    
    def show_menu(self):
        self.menuframe.grid(
            row = 0,
            rowspan = 3,
            column = 0,
            sticky = "NWS"
        )
        self.menuframe.tkraise()

    def close(self):
        self.menuframe.grid_forget()

    def open_settings(self):
        self.settings = Settings(self.root)
        self.settings.focus_set()
        self.settings.grab_set()
        self.settings.wait_window()
        if self.settings.worktime: # To make sure that opening settings without changing anything does not reset the timer
            try:
                self.work_const = self.settings.worktime * 60
                self.work = self.work_const
                self.shortbreak_const = self.settings.shortbreaktime * 60
                self.shortbreak = self.shortbreak_const
                self.longbreak_const = self.settings.longbreaktime * 60
                self.longbreak = self.longbreak_const

                self.workstring = f"{self.work_const // 60:02d} : {self.work_const % 60:02d}"
                self.shortbreakstring = f"{self.shortbreak_const // 60:02d} : {self.shortbreak_const % 60:02d}"
                self.longbreakstring = f"{self.longbreak_const // 60:02d} : {self.longbreak_const % 60:02d}"

                self.worktimevar.set(tk.StringVar(value = self.workstring).get())
                self.shortbreaktimevar.set(tk.StringVar(value = self.shortbreakstring).get())
                self.longbreaktimevar.set(tk.StringVar(value = self.longbreakstring).get())

                self.workcycles = self.settings.workcycles
                self.workcounterw.configure(text = f"{self.workcount} / {self.workcycles}")
                self.workcountersb.configure(text = f"{self.workcount} / {self.workcycles}")
                self.workcounterlb.configure(text = f"{self.workcount} / {self.workcycles}")

                self.blockcycles = self.settings.blockcyles

                self.notification = self.settings.notification
            except AttributeError:
                pass
    
    def notifications(self):
        # Notifications
        if self.notification == 1:
            notification = ToastNotifier()
            notification.show_toast(
                "PomoBlocker",
                "Time's up!",
                icon_path = Path(__file__).parent / "..\\res\\media\\pomodoro.ico",
                duration = 5
            )
        elif self.notification == 2:
            playsound(str(Path(__file__).parent / "../res/media/sounds/bell1.wav"))
        elif self.notification == 3:
            playsound(str(Path(__file__).parent / "../res/media/sounds/bell2.wav"))
        elif self.notification == 4:
            playsound(str(Path(__file__).parent / "../res/media/sounds/alarm1.wav"))
        elif self.notification == 5:
            playsound(str(Path(__file__).parent / "../res/media/sounds/alarm2.wav"))        

    def open_login(self):
        messagebox.showinfo(
            "PomoBlocker",
            "Login feature coming soon!"
        )

    def open_summary(self):
        messagebox.showinfo(
            "PomoBlocker",
            "Pomodoro summary feature coming soon!"
        )


def main():
    app = App()
    app.root.mainloop()


if __name__ == '__main__':
    main()
