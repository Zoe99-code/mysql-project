from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("Life Choices User Login")
root.geometry("700x700")
root.config(bg="black")

label_logo = Label(root, text="Life Choices", width=70, font=("Serif", 20), bg="purple")
label_logo.place(x=0, y=0)

label1 = Label(root, text="Username: ")
label1.place(x=500, y=100)

entry1 = Entry(root, width=40)
entry1.place(x=400, y=150)

password1 = Label(root, text="Password: ")
password1.place(x=500, y=200)

user_password = Entry(root, width=40, show="*")
user_password.place(x=400, y=250)


def logged():
    messagebox.showinfo("Welcome", "Login Granted." + entry1.get())
    root1 = Tk()
    root1.title("Contact Details")
    root1.geometry("500x500")
    root1.config(bg="black")

    number_label = Label(root1, text="Contact Number: ")
    number_label.place(x=0, y=0)

    number_entry = Entry(root1, width=20)
    number_entry.place(x=0, y=40)

    def sign():
        try:
            messagebox.showinfo("Welcome.", "Login Successful, Access Granted." + entry1.get())
            root1.destroy()
        except ValueError:
            messagebox.showerror("ValueError", "Enter Digits only." + entry1.get())

    sign_button = Button(root1, text="Sign In", width=10, command=sign)
    sign_button.place(x=0, y=100)

    def fail():
        messagebox.showerror("Error.", "Unable To Proceed.")
        entry1.delete(0, END)
        user_password.delete(0, END)

        def log():
            user = entry1.get()

            if results:
                sql = 'UPDATE Users SET Login_time = NOW() WHERE Username = %s'
                mycursor.execute(sql, [user])
                mydb.commit()

                if mycursor.rowcount > 0:
                    pass

                    for _ in results:
                        logged()
                        break
                    else:
                        fail()

                        login_button = Button(root, text="Login", width=20, command=log)
                        login_button.place(x=50, y=350)

                        def out():
                            username = entry1.get()
                            userpass = user_password.get()
                            sql = 'Select * from Users where Username = %s and Password = %s'
                            mycursor.execute(sql, [username, userpass])
                            results = mycursor.fetchone()

                            if results:
                                sql = 'UPDATE Users SET Logout_time = NOW() WHERE Username = %s'
                                mycursor.execute(sql, [username])
                                mydb.commit()

                                if mycursor.rowcount > 0:
                                    pass

                                    for _ in results:
                                        messagebox.showinfo("Farewell.", "Log Out Successful.")
                                        break
                                    else:
                                        entry1.delete(0, END)
                                        user_password.delete(0, END)

                                        out_button = Button(root, text="Sign Out", width=20, command=out)
                                        out_button.place(x=440, y=400)


def register():
    root.destroy()
    messagebox.showinfo("Unauthorised Access.", "Login Through The Administration Portal.")

    root2 = Tk()
    root2.title("Admin Sign-in")
    root2.geometry("500x500")
    root2.config(bg="black")

    admin_username = Label(root2, text="Username: ")
    admin_username.place(x=0, y=0)

    admin_entry = Entry(root2, width=20)
    admin_entry.place(x=0, y=30)

    admin_password = Label(root2, text="Password: ")
    admin_password.place(x=0, y=80)

    admin_entry2 = Entry(root2, width=20, show="*")
    admin_entry2.place(x=0, y=110)


def login(admin_entry=root, admin_entry2=root, root2=None):
    username = admin_entry.get()
    userpass = admin_entry2.get()
    sql = 'Select * from Admin where Username = %s and Password = %s'
    mycursor.execute(sql, [username, userpass])
    results = mycursor.fetchone()

    if results:
        sql = 'UPDATE Admin SET Login_time = NOW() WHERE Username = %s'
        mycursor.execute(sql, [username])
        mydb.commit()

        if mycursor.rowcount > 0:
            pass

            for _ in results:
                messagebox.showinfo("Authorised Access Granted.", "Welcome To The Administration Portal.")
                root2.destroy()

                root3 = Tk()
                root3.title("Life Choices Administration Portal")
                root3.geometry("700x700")
                root3.config(bg="black")

                label_logo2 = Label(root2, text="Life Choices", width=70, font=("Serif", 20), bg="purple")
                label_logo2.place(x=0, y=0)

                def logout():
                    sql = 'Select * from Admin where Username = %s and Password = %s'
                    mycursor.execute(sql, [username, userpass])
                    results = mycursor.fetchone()

                    if results:
                        sql = 'UPDATE Admin SET Logout_time = NOW() WHERE Username = %s'
                        mycursor.execute(sql, [username])
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            pass

                        for i in results:
                            messagebox.showinfo("Farewell.", "Exiting The Portal.")
                            root.destroy()

                            break
                        else:
                            admin_entry.delete(0, END)
                            admin_entry2.delete(0, END)

                            user_id_list = Label(root, text="User Id")
                            user_id_list.place(x=50, y=100)
                            listBox = Listbox(root, width=20)
                            listBox.place(x=50, y=150)

                            username_list = Label(root, text="Username")
                            username_list.place(x=250, y=100)
                            listBox3 = Listbox(root, width=20)
                            listBox3.place(x=250, y=150)

                            password_list = Label(root, text="Password")
                            password_list.place(x=450, y=100)
                            listBox4 = Listbox(root, width=20)
                            listBox4.place(x=450, y=150)

                            login_list = Label(root, text="Login")
                            login_list.place(x=650, y=100)
                            listBox5 = Listbox(root, width=20)
                            listBox5.place(x=650, y=150)

                            logout_list = Label(root, text="Logout")
                            logout_list.place(x=850, y=100)
                            listbox6 = Listbox(root, width=20)
                            listbox6.place(x=850, y=150)

                def populatebox():
                    global time, name, pass1, time2, add
                    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                                   database='lifechoicesonline')
                    mycursor = mydb.cursor()
                    sql = "select UserId FROM Users"
                    mycursor.execute(sql)
                    for i in mycursor:
                        listBox.insert("end", i)
                        mycursor.execute("SELECT Username FROM Users")
                        name = mycursor.fetchone()

                    for i in name:
                        listBox3.insert(END, i)
                        mycursor.execute("SELECT Password FROM Users")
                        pass1 = mycursor.fetchone()

                    for i in pass1:
                        listBox4.insert(END, i)
                        mycursor.execute("SELECT Login_time FROM Users")
                        time = mycursor.fetchone()

                    for i in time:
                        listBox5.insert(END, i)
                        mycursor.execute("SELECT Logout_time FROM Users")
                        time2 = mycursor.fetchall()

                    for i in time2:
                        listbox6.insert(END, i)

                        update_button = Button(root, text="Update list", command=lambda: populatebox())
                        update_button.place(x=450, y=400)

                def add():
                    root4 = Tk()
                    root4.title("Add User")
                    root4.geometry("500x500")

                full_name_label = Label(root3, text="Full Name:")
                user_name_label = Label(root3, text="Username:")
                password_label = Label(root3, text="Password:")
                fullname = Entry(root3)
                username = Entry(root3)
                password = Entry(root3)

                def create():
                    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                   host='localhost', database='lifechoicesonline')
                    mycursor = mydb.cursor()
                    x = fullname.get()
                    y = username.get()
                    z = password.get()

                    if x == '' or y == '' or z == '':
                        messagebox.showerror("Retry.", "Do not leave any fields empty.")
                        root3.destroy()
                        create()

                    else:
                        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                       host='localhost', database='lifechoicesonline')
                        try:
                            mycursor = mydb.cursor()
                            sql = "INSERT INTO Users(Fullname, Username, Password) VALUES(%s, %s, %s)"
                            mycursor.execute(sql, [x, y, z])
                            mydb.commit()
                        except:
                            messagebox.showerror("Unsuccessful.", "Error connecting to the database.")
                            messagebox.showinfo("Success" + x + " has been entered into the server")
                            root3.destroy()

                    create_button = Button(root3, text="Add User", command=create)
                    full_name_label.place(x=5, y=5)
                    user_name_label.place(x=5, y=45)
                    password_label.place(x=5, y=85)
                    fullname.place(x=5, y=25)
                    username.place(x=5, y=65)
                    password.place(x=5, y=105)
                    create_button.place(x=25, y=130)

                    add_user_button = Button(root, text="Add User", width=20, command=add)
                    add_user_button.place(x=100, y=500)


root5 = Tk()
root5.title("Next Of Kin")
root5.geometry("500x500")
root5.config(bg="black")

kin_name = Entry(root5)
kin_name.config(width=15, font="Serif, 20", bg="purple")
kin_name.place(x=150, y=245)
kin_contact = Entry(root5)
kin_contact.config(width=15, font="Serif, 20", bg="purple")
kin_contact.place(x=450, y=245)

root6 = Tk()
root6.title("Remove")
root6.geometry("200x200")

name = Label(root5, text="Full Name:")
name.place(x=0, y=0)

full_name = Entry(root5)
full_name.place(x=0, y=20)

name_user = Label(root5, text="Username:")
name_user.place(x=0, y=40)

user_name = Entry(root5)
user_name.place(x=0, y=60)

password_label = Label(root5, text="Password:")
password_label.place(x=0, y=80)

password = Entry(root5)
password.place(x=0, y=100)


def delete():
    sql = "DELETE from Users where Fullname = %s"
    messagebox.showinfo("DELETED", "Delete was a success")
    root6.destroy()


delete_button = Button(root, text="Delete User", width=20, command=delete)
delete_button.place(x=400, y=500)

admin_button = Button(root, text="Login", width=20, command=login)
admin_button.place(x=0, y=250)

register_button = Button(root, text="Register Here", width=20, command=register)
register_button.place(x=800, y=350)
userid_list = Label(root, text="UserId")
userid_list.place(x=50, y=500)
listBox = Listbox(root, width=20)
listBox.place(x=50, y=550)

username_list = Label(root, text="Username")
username_list.place(x=250, y=500)
listBox3 = Listbox(root, width=20)
listBox3.place(x=250, y=550)

password_list = Label(root, text="Password")
password_list.place(x=450, y=500)
listBox4 = Listbox(root, width=20)
listBox4.place(x=450, y=550)

login_list = Label(root, text="Login")
login_list.place(x=650, y=500)
listBox5 = Listbox(root, width=20)
listBox5.place(x=650, y=550)

logout_list = Label(root, text="Logout")
logout_list.place(x=850, y=500)
listbox6 = Listbox(root, width=20)
listbox6.place(x=850, y=550)


def populatebox():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                   database='lifechoicesonline')
    mycursor = mydb.cursor()
    sql = "select UserId FROM Users"
    mycursor.execute(sql)
    for i in mycursor:
        listBox.insert("end", i)

    mycursor.execute("SELECT Username FROM Users")
    name = mycursor.fetchall()

    for i in name:
        listBox3.insert(END, i)

    mycursor.execute("SELECT Password FROM Users")
    pass1 = mycursor.fetchall()

    for i in pass1:
        listBox4.insert(END, i)

    mycursor.execute("SELECT Login_time FROM Users")
    time = mycursor.fetchall()

    for i in time:
        listBox5.insert(END, i)

    mycursor.execute("SELECT Logout_time FROM Users")
    time2 = mycursor.fetchall()

    for i in time2:
        listbox6.insert(END, i)


update_button = Button(root, text="Update list", command=lambda: populatebox())
update_button.place(x=450, y=800)

root.mainloop()
