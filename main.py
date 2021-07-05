import tkinter
from tkinter import *
from datetime import datetime
import re
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Life Choices Online")
root.config(bg="")
root.resizable(0, 0)


def identity(age):
    if age >= 18:
        messagebox.showinfo("Welcome", "Select Yes To Start The Game.")
    elif age < 18:
        messagebox.showinfo("Error", "You Are Too Young To Proceed To The Game.")
    else:
        messagebox.showinfo()


class Information:
    def __init__(self, master):
        self.master = master
        self.root = root
        self.fullname = Label(root, text='Full Name:', bg="grey20", fg='white')
        self.fullname.place(x=10, y=250)
        self.fullname_entry = Entry(root, width=20)
        self.fullname_entry.place(x=150, y=250)
        self.email = Label(root, text='Email Address:', bg="grey20", fg='white')
        self.email.place(x=10, y=300)
        self.email_entry = Entry(root, width=20)
        self.email_entry.place(x=150, y=300)
        self.address = Label(root, text='Address:', bg="grey20", fg='white')
        self.address.place(x=10, y=350)
        self.address_entry = Entry(root, width=20)
        self.address_entry.place(x=150, y=350)
        self.identity = Label(root, text='Identity Number:', bg="grey20", fg='white')
        self.identity.place(x=10, y=400)
        self.identity_entry = Entry(root, width=20)
        self.identity_entry.place(x=150, y=400)
        self.clear_button = Button(root, text='Clear', bg="purple", borderwidth=10, font=('Georgia', 10, 'bold'),
                                   command=self.reset)
        self.clear_button.place(x=100, y=460)
        self.play_button = Button(root, text='Confirm', bg="purple", borderwidth=10, font=('Georgia', 10, 'bold'),
                                  command=self.player_id)
        self.play_button.place(x=200, y=460)
        self.exit_button = Button(root, text='Exit', bg="purple", borderwidth=10, font=('Georgia', 10, 'bold'),
                                  command=self.close)
        self.exit_button.place(x=320, y=460)

    def player_id(self):
        dt = datetime.today()
        ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        try:
            for i in range(len(self.email_entry.get())):
                if re.search(ex, self.email_entry.get()):
                    with open("Text-File.txt", "w+") as f:
                        f.write(self.email_entry.get())
                        f.write("\n")
                        f.write(self.fullname_entry.get())
                        f.write("\n")
                        f.write(self.identity_entry.get())
                        f.write("\n")
                        f.write(str(dt))
                        f.write("\n")
                else:
                    messagebox.showerror("Error", "Invalid Email Address Provided.")
                    root.destroy()
            for x in range(int(self.identity_entry.get())):
                res = int(self.identity_entry.get()[0:2]) - int(dt.strftime("%y"))
                if res >= 18:
                    messagebox.showinfo("Welcome", "Select Yes To Start The Game.")
                    root.destroy()
                elif len(self.identity_entry.get()) != 13:
                    messagebox.showerror("Error", "Invalid Identity Number Provided.")
                    break
                else:
                    messagebox.showerror("Error", "You Are Too Young To Proceed To The Game.")
                    break
        except ValueError:
            if self.identity_entry.get() != int:
                messagebox.showerror("Error", "Identity Number Must Only Be Provided Using Digits.")
            elif self.fullname_entry.get() != str:
                messagebox.showerror("Error", "Full Name Must Only Be Provided Using Alphabetical Letters.")

    def start(self):
        self.fullname = ["Zoe Strachan"]
        self.address = ["75 Black Crescent"]
        self.identity = ["9908080293088"]
        self.email = ["lizzystrachan99@gmail.com"]

    def reset(self):
        self.fullname_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.identity_entry.delete(0, END)

    def close(self):
        self.root.destroy()


information = Information(root)

root.mainloop()