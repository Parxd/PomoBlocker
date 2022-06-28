import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class Settings():
    work = 25
    shortbreak = 5
    longbreak = 15

    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Settings")
        self.master.geometry("500x500")

        self.timeoptions = [i for i in range(15, 31)]
        self.timeoptions.insert(0, "")
        self.clicked = tk.StringVar()
        self.clicked.set(self.timeoptions[0])

        self.entries = []
        self.websites = []

        self.worklabel = tk.Label(
            self.master,
            text = "Work time", 
            font = ("TimesNewRoman", 10)
            )
        self.worklabel.pack()

        self.workentryvar = tk.IntVar()
        self.workentry = tk.OptionMenu(
            self.master,
            self.clicked,
            *self.timeoptions
            )
        self.workentry.pack()

        self.breakshortlabel = tk.Label(
            self.master,
            text = "Short break time", 
            font = ("TimesNewRoman", 10)
            )
        self.breakshortlabel.pack()

        self.breakshortentry = tk.OptionMenu(
            self.master, 
            self.clicked,
            *self.timeoptions
            )
        self.breakshortentry.pack()

        self.breaklonglabel = tk.Label(
            self.master,
            text = "Long break time", 
            font = ("TimesNewRoman", 10)
            )
        self.breaklonglabel.pack()

        self.breaklongentry = tk.OptionMenu(
            self.master, 
            self.clicked,
            *self.timeoptions
            )
        self.breaklongentry.pack()

        self.websiteslabel = tk.Label(
            self.master,
            text = "Enter the websites you want to block during work periods:",
            font = ("TimesNewRoman", 10),
            pady = 10
            )
        self.websiteslabel.pack()

        self.addbutton = tk.Button(
            self.master,
            text = "+",
            width = 5,
            borderwidth = 2,
            command = self.add_site,
            font = ("TimesNewRoman", 10)
            )
        self.addbutton.pack()

        self.removebutton = tk.Button(
            self.master,
            text = "-",
            width = 5,
            borderwidth = 2,
            command = self.remove_site,
            font = ("TimesNewRoman", 10)
        )
        self.removebutton.pack()

        self.submit = tk.Button(self.master,
            text = "Save",
            padx = 2,
            pady = 2,
            font = ("TimesNewRoman", 10),
            command = self.savebutton)
        self.submit.pack()

    def add_site(self):
        self.entry = tk.Entry(
            self.master,
            width = 40,
            borderwidth = 2,
            justify = "center",
        )
        self.entry.pack()
        self.entries.append(self.entry)

    def remove_site(self):
        try:
            self.entries.pop().destroy()
        except IndexError:
            pass

    def savebutton(self):
        self.work = self.workentry.get().strip()
        self.shortbreak = self.breakshortentry.get().strip()
        self.longbreak = self.breaklongentry.get().strip()
        for entry in self.entries:
            self.websites.append(entry.get().strip())
        if not self.work.isnumeric() or not self.shortbreak.isnumeric() or \
            not self.longbreak.isnumeric():
            messagebox.showerror(
                "Error",
                "Please enter valid numbers."
                )
        else:
            self.proceed = False
            if not self.websites or all(flag == "" for flag in self.websites):
                self.proceed = messagebox.askyesno(
                    "Notice",
                    "Do you wish to proceed without blocking any websites?"
                    )
            else:
                messagebox.showinfo("Notice", "Information saved!")
                self.workentry.delete(0, tk.END)
                self.breakshortentry.delete(0, tk.END)
                self.breaklongentry.delete(0, tk.END)
                for entry in self.entries:
                    entry.delete(0, tk.END)

            if self.proceed == True:
                messagebox.showinfo("Notice", "Information saved!")
                self.workentry.delete(0, tk.END)
                self.breakshortentry.delete(0, tk.END)
                self.breaklongentry.delete(0, tk.END)
                for entry in self.entries:
                    entry.delete(0, tk.END)
            self.parse(self.websites)

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


def main():
    settings = Settings()
    settings.master.mainloop()


if __name__ == '__main__':
    main()
