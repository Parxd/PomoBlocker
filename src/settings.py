import threading
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
from playsound import playsound

ctk.set_appearance_mode("Dark")


class Settings():
    def __init__(self):
        self.master = ctk.CTk()
        self.master.title("Settings")
        self.master.geometry("800x740")
        self.master.iconbitmap(
            Path(__file__).parent / "../res/media/settings.ico"
        )
        self.master.grid_rowconfigure(0, weight = 1)
        self.master.grid_rowconfigure(1, weight = 1)
        self.master.grid_columnconfigure((1, 2, 3), weight = 1)
        self.entries = []
        self.websites = []

        ''' ----- Initialize tab frame & main three buttons ----- '''
        self.tabframe = ctk.CTkFrame(
            self.master,
            width = 150,
            corner_radius = 0,
        )
        self.tabframe.grid(
            row = 0,
            column = 0,
            rowspan = 3,
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
            rowspan = 3,
            columnspan = 2,
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
                rowspan = 2,
                columnspan = 3,
                sticky = "NSEW",
                padx = 35,
                pady = 35,
        )
        self.raise_frame(self.time_settings_frame)

        ''' ----- Initialize widgets inside the time settings frame ----- '''
        self.time_settings_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.time_settings_frame.grid_columnconfigure((0, 1, 2), weight = 1)

        self.time_settings_instructions = ctk.CTkLabel(
            self.time_settings_frame,
            text = "Customize times for each timer",
            text_font = ("Roboto Medium", 12),
            width = 150
        )
        self.time_settings_instructions.grid(
            row = 0,
            column = 0,
            columnspan = 3,
            pady = (15, 0)
        )

        self.workimg = ImageTk.PhotoImage(Image.open(
            Path(__file__).parent / "../res/media/working.png"
            ))
        self.workimglabel = ctk.CTkLabel(
            self.time_settings_frame,
            image = self.workimg,
            width = 5,
            height = 5
        )
        self.workimglabel.grid(
            row = 1,
            column = 0,
        )
        self.worklabel = ctk.CTkLabel(
            self.time_settings_frame,
            text = "Work time",
            text_font = ("Helvetica Medium", 11),
        )
        self.worklabel.grid(
            row = 1,
            column = 1,
        )
        self.workinput = ctk.CTkOptionMenu(
            self.time_settings_frame,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(15, 31)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.workinput.grid(
            row = 1,
            column = 2,
            padx = (0, 15)
        )
        self.workinput.set("")

        self.shortbreakimg = ImageTk.PhotoImage(Image.open(
            Path(__file__).parent / "../res/media/coffee.png"
        ))
        self.shortbreakimglabel = ctk.CTkLabel(
            self.time_settings_frame,
            image = self.shortbreakimg
        )
        self.shortbreakimglabel.grid(
            row = 2,
            column = 0,
        )
        self.shortbreaklabel = ctk.CTkLabel(
            self.time_settings_frame,
            text = "Short break time",
            text_font = ("Helvetica Medium", 11)
        )
        self.shortbreaklabel.grid(
            row = 2,
            column = 1,
        )
        self.shortbreakinput = ctk.CTkOptionMenu(
            self.time_settings_frame,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(0, 11)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.shortbreakinput.grid(
            row = 2,
            column = 2,
            padx = (0, 15)
        )
        self.shortbreakinput.set("")

        self.longbreakimg = ImageTk.PhotoImage(Image.open(
          Path(__file__).parent / "../res/media/pillow.png"  
        ))
        self.longbreakimglabel = ctk.CTkLabel(
            self.time_settings_frame,
            image = self.longbreakimg
        )
        self.longbreakimglabel.grid(
            row = 3,
            column = 0,
        )
        self.longbreaklabel = ctk.CTkLabel(
            self.time_settings_frame,
            text = "Long break time",
            text_font = ("Helvetica Medium", 11)
        )
        self.longbreaklabel.grid(
            row = 3,
            column = 1,
        )
        self.longbreakinput = ctk.CTkOptionMenu(
            self.time_settings_frame,
            width = 120,
            text_font = ("Helvetica Medium", 11),
            values = [i for i in range(15, 26)],
            fg_color = "grey35",
            button_color = "#FF775B",
            button_hover_color = "#FF8B6F"
        )
        self.longbreakinput.grid(
            row = 3,
            column = 2,
            padx = (0, 15)
        )
        self.longbreakinput.set("")

        self.autostartinput = ctk.CTkCheckBox(
            self.time_settings_frame,
            text = "Auto-start cycles?",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.autostartinput.grid(
            row = 4,
            column = 2,
            padx = (0, 15),
            pady = (10, 0)
        )

        self.save = ctk.CTkButton(
            self.master,
            command = self.save_inputs,
            text = "Save",
            text_font = ("Roboto Medium", 10),
            width = 150,
            corner_radius = 4,
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.save.grid(
            row = 2,
            column = 3,
            padx = (0, 35),
            pady = (0, 40),
            sticky = "E"
        )
        self.reset = ctk.CTkButton(
            self.tabframe,
            command = self.reset_inputs,
            text = "Reset",
            text_font = ("Roboto Medium", 10),
            width = 120,
            corner_radius = 4,
            text_color = "#FF775B",
            fg_color = "grey20",
            hover_color = "grey28"
        )
        self.reset.grid(
            row = 8,
            column = 0,
            pady = (0, 40)
        )

        self.init_website_frame()
        self.init_notifications_frame()

    def save_inputs(self):
        self.worktime = self.workinput.get()
        self.shortbreaktime = self.shortbreakinput.get()
        self.longbreaktime = self.longbreakinput.get()
        self.autostart = self.autostartinput.get()
        for entry in self.entries:
            self.websites.append(entry.get())
        self.parse(self.websites)
        self.notification = self.radiovar.get()

        if not self.worktime and not self.shortbreaktime and not self.longbreaktime:
            self.proceed1 = messagebox.askyesno(
                "Warning",
                "Are you sure you want to proceed with default Pomodoro times?"
            )
            self.worktime = 25
            self.shortbreaktime = 5
            self.longbreaktime = 15
        elif not self.worktime or not self.shortbreaktime or not self.longbreaktime:
            self.proceed1 = False
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
        else:
            self.proceed1 = True

        if self.proceed1:
            if all(flag == "" for flag in self.websites):
                self.proceed2 = messagebox.askyesno(
                    "Warning",
                    "Are you sure you want to proceed without blocking any websites?"
                )
                if self.proceed2:
                    messagebox.showinfo(
                        "Notice",
                        "Information saved!"
                    )
                    self.master.destroy()

    def reset_inputs(self):
        if messagebox.askyesno(
            "Warning",
            "Are you sure you want to reset all settings to default?"
        ) == True:
            # Reset settings in times settings frame
            self.workinput.set("")
            self.shortbreakinput.set("")
            self.longbreakinput.set("")
            self.autostartinput.deselect()

            # Reset settings in website settings frame
            self.workblock.deselect()
            self.shortbreakblock.deselect()
            self.longbreakblock.deselect()
            for entry in self.entries:
                entry.destroy()

            # Reset settings in notifications settings frame
            self.nonotification.select()
        else:
            pass

    def raise_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    def init_website_frame(self):
        self.websites_settings_frame.grid_columnconfigure((0, 1, 2), weight = 1)

        self.instructions = ctk.CTkLabel(
            self.websites_settings_frame,
            text = "Modify website access",
            text_font = ("Roboto Medium", 12)
        )
        self.instructions.grid(
            row = 0,
            column = 0,
            columnspan = 3,
            pady = 25
        )
        self.instructions2 = ctk.CTkLabel(
            self.websites_settings_frame,
            text = "Block the below websites during:",
            text_font = ("Roboto Medium", 10)
        )
        self.instructions2.grid(
            row = 1,
            column = 0,
            columnspan = 3,
            pady = (0, 12)
        )
        self.workblock = ctk.CTkCheckBox(
            self.websites_settings_frame,
            text = "Work",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.workblock.grid(
            row = 2,
            column = 0
        )
        self.shortbreakblock = ctk.CTkCheckBox(
            self.websites_settings_frame,
            text = "Short break",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.shortbreakblock.grid(
            row = 2,
            column = 1
        )
        self.longbreakblock = ctk.CTkCheckBox(
            self.websites_settings_frame,
            text = "Long break",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.longbreakblock.grid(
            row = 2,
            column = 2
        )

        self.addwebsiteimage = ImageTk.PhotoImage(Image.open(
            Path(__file__).parent / "../res/media/add.png"
        ))
        self.addwebsite = ctk.CTkButton(
            self.websites_settings_frame,
            command = self.add_site,
            text = "",
            image = self.addwebsiteimage,
            text_font = ("Roboto Medium", 10),
            fg_color = "#99ff99",
            hover_color = "#b2ffb2",
            height = 45
        )
        self.addwebsite.grid(
            row = 3,
            column = 0,
            padx = 30,
            pady = (25, 5),
            sticky = "EW"
        )
        self.removewebsiteimage = ImageTk.PhotoImage(Image.open(
            Path(__file__).parent / "../res/media/remove.png"
        ))
        self.removewebsite = ctk.CTkButton(
            self.websites_settings_frame,
            command = self.remove_site,
            text = "",
            image = self.removewebsiteimage,
            text_font = ("Roboto Medium", 10),
            fg_color = "#ff7f7f",
            hover_color = "#ff9999",
            height = 45
        )
        self.removewebsite.grid(
            row = 3,
            column = 2,
            padx = 30,
            pady = (25, 5),
            sticky = "EW"
        )

    def add_site(self):
        self.entry = ctk.CTkEntry(
            self.websites_settings_frame,
            text_font = ("Roboto Medium", 10),
            justify = "center"
        )
        self.entries.append(self.entry)
        for i in range(len(self.entries)):
            self.entries[i].grid(
                row = 4 + i,
                column = 0,
                columnspan = 3,
                padx = 30,
                pady = 2,
                sticky = "EW"
            )

    def remove_site(self):
        try:
            self.entries.pop().destroy()
        except IndexError:
            messagebox.showerror(
                "Error",
                "No websites to remove!"
            )

    def parse(self, websites):
        self.sites = []
        self.input = websites
        for i in self.input:
            if i == '':
                self.input.remove(i)
            elif i[0:4] != "www." and i[-4:] == ".com":
                self.sites.append(i)
                self.sites.append("www." + i)
            elif i[0:4] == "www." and i[-4:] == ".com":
                self.sites.append(i)
                self.sites.append(i[4:])
            else:
                self.sites.append(i + ".com")
                self.sites.append("www." + i + ".com")

    def init_notifications_frame(self):
        self.notifications_settings_frame.grid_columnconfigure(0, weight = 1)
        self.notifinstructions = ctk.CTkLabel(
            self.notifications_settings_frame,
            text = "Set preferences for notifications",
            text_font = ("Roboto Medium", 12)
        )
        self.notifinstructions.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            pady = 38
        )
        self.radiovar = tk.IntVar()
        self.nonotification = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 0,
            text = "No notification",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.nonotification.grid(
            row = 6,
            column = 0,
            pady = 10
        )
        self.windownotification = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 1,
            text = "Pop-up notification",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.windownotification.grid(
            row = 5,
            column = 0,
            pady = 10
        )
        self.bell1sound = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 2,
            text = "Bell 1",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.bell1sound.grid(
            row = 1,
            column = 0,
            pady = 10
        )
        self.bell2sound = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 3,
            text = "Bell 2",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.bell2sound.grid(
            row = 2,
            column = 0,
            pady = 10
        )
        self.alarm1sound = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 4,
            text = "Alarm 1",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.alarm1sound.grid(
            row = 3,
            column = 0,
            pady = 10
        )
        self.alarm2sound = ctk.CTkRadioButton(
            self.notifications_settings_frame,
            variable = self.radiovar,
            value = 5,
            text = "Alarm 2",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.alarm2sound.grid(
            row = 4,
            column = 0,
            pady = 10
        )

        self.samplesoundbutton = ctk.CTkButton(
            self.notifications_settings_frame,
            command = lambda: threading.Thread(target = self.play_sound).start(),
            text = "Play sound",
            text_font = ("Roboto Medium", 10),
            fg_color = "#FF775B",
            hover_color = "#FF9579"
        )
        self.samplesoundbutton.grid(
            row = 8,
            column = 0,
            pady = 20
        )

    def play_sound(self):
        if self.radiovar.get() == 2:
            playsound(str(Path(__file__).parent / "../res/media/sounds/bell1.wav"))
        elif self.radiovar.get() == 3:
            playsound(str(Path(__file__).parent / "../res/media/sounds/bell2.wav"))
        elif self.radiovar.get() == 4:
            playsound(str(Path(__file__).parent / "../res/media/sounds/alarm1.wav"))
        elif self.radiovar.get() == 5:
            playsound(str(Path(__file__).parent / "../res/media/sounds/alarm2.wav"))


def main():
    settings = Settings()
    settings.master.mainloop()


if __name__ == '__main__':
    main()
