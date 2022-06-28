import tkinter as tk
from tkinter import messagebox


class Settings():
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Settings")
        self.master.geometry("800x600")
        self.entries = []
        self.websites = []

        self.askinput = tk.Label(
            self.master,
            text = "Enter your desired times:",
        )
        self.askinput.grid(
            row = 0,
            column = 2,
            pady = (30, 10)
        )

        self.worklabel = tk.Label(
            self.master,
            text = "Work time", 
            )
        self.worklabel.grid(
            row = 1,
            column = 1
            )

        self.workentry = tk.Entry(
            self.master,
            width = 10,
            borderwidth = 2,
            justify = "center"
            )
        self.workentry.grid(
            row = 2,
            column = 1
            )

        self.breakshortlabel = tk.Label(
            self.master,
            text = "Short break time", 
            )
        self.breakshortlabel.grid(
            row = 1,
            column = 2
            )

        self.breakshortentry = tk.Entry(
            self.master, 
            width = 10,
            borderwidth = 2, 
            justify = "center"
            )
        self.breakshortentry.grid(
            row = 2,
            column = 2
            )

        self.breaklonglabel = tk.Label(
            self.master,
            text = "Long break time", 
            )
        self.breaklonglabel.grid(
            row = 1,
            column = 3
            )

        self.breaklongentry = tk.Entry(
            self.master, 
            width = 10,
            borderwidth = 2, 
            justify = "center"
            )
        self.breaklongentry.grid(
            row = 2,
            column = 3
            )

        self.var = tk.BooleanVar()
        self.cyclecontrol = tk.Checkbutton(
            self.master,
            text = "Auto-start cycles?",
            pady = 5,
            variable = self.var
        )
        self.cyclecontrol.grid(
            row = 3,
            column = 2,
            pady = (5, 30)
            )

        self.websiteslabel = tk.Label(
            self.master,
            text = "Enter the websites \nyou want to block:",
            pady = 10
            )
        self.websiteslabel.grid(
            row = 4,
            column = 2
            )

        self.addbutton = tk.Button(
            self.master,
            text = "+",
            width = 8,
            borderwidth = 2,
            command = self.add_site,
            )
        self.addbutton.grid(
            row = 5,
            column = 1,
            )

        self.removebutton = tk.Button(
            self.master,
            text = "-",
            width = 8,
            borderwidth = 2,
            command = self.remove_site,
        )
        self.removebutton.grid(
            row = 5,
            column = 3,
            )

        self.submit = tk.Button(
            self.master,
            text = "Save",
            padx = 2,
            pady = 2,
            command = self.savebutton)
        self.submit.grid(
            row = 31,
            column = 2
            )

    def add_site(self):
        self.entry = tk.Entry(
            self.master,
            width = 27,
            borderwidth = 2,
            justify = "center",
        )
        self.entries.append(self.entry)
        for i in range(len(self.entries)):
            self.entry.grid(
                row = 6 + i,
                column = 1,
                columnspan = 3,
                sticky = "EW",
                pady = 2
            )

    def remove_site(self):
        try:
            self.entries.pop().destroy()
        except IndexError:
            messagebox.showerror(
                "Error",
                "No websites to remove!"
            )

    def savebutton(self):
        try:
            self.work = int(self.workentry.get().strip())
            self.shortbreak = int(self.breakshortentry.get().strip())
            self.longbreak = int(self.breaklongentry.get().strip())
            self.startstop = self.var.get()
            for entry in self.entries:
                self.websites.append(entry.get().strip())

            if self.work <= 0 or self.shortbreak <= 0 or self.longbreak <= 0:
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
                    self.cyclecontrol.deselect()

                if self.proceed == True:
                    messagebox.showinfo("Notice", "Information saved!")
                    self.workentry.delete(0, tk.END)
                    self.breakshortentry.delete(0, tk.END)
                    self.breaklongentry.delete(0, tk.END)
                    for entry in self.entries:
                        entry.delete(0, tk.END)
                    self.cyclecontrol.deselect()
                self.parse(self.websites)
        except ValueError:
            messagebox.showerror(
                    "Error",
                    "Please enter valid numbers."
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


def main():
    settings = Settings()
    settings.master.mainloop()
    print(settings.entries)


if __name__ == '__main__':
    main()
