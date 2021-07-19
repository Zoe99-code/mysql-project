from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Life Choices User Login")
root.geometry("700x700")
root.config(bg="black")

label_logo = Label(root, text="Life Choices", width=70, font=("Serif", 20), bg="purple")
label_logo.place(x=0, y=0)

life_label = Label(root, text="Username: ")
life_label.place(x=500, y=100)

life_entry = Entry(root, width=40)
life_entry.place(x=400, y=150)

life_pass = Label(root, text="Password: ")
life_pass.place(x=500, y=200)

user_password = Entry(root, width=40, show="*")
user_password.place(x=400, y=250)


def logged():
    messagebox.showinfo("Welcome", "Login Granted." + life_entry.get())
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
            messagebox.showinfo("Welcome.", "Login Successful, Access Granted." + life_entry.get())

            root1.destroy()
        except ValueError:
            messagebox.showerror("ValueError", "Enter Digits only." + life_entry.get())

    sign_button = Button(root1, text="Sign In", width=10, command=sign)
    sign_button.place(x=0, y=100)


def failed():
    messagebox.showerror("Error.", "Unable To Proceed.")
    life_entry.delete(0, END)
    user_password.delete(0, END)


def login():
    user = life_entry.get()

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
            failed()


login_button = Button(root, text="Login", width=20, command=login)
login_button.place(x=50, y=350)


def out():
    username = life_entry.get()
    userpass = user_password.get()
    sql = 'Select * from Users where Username = %s and Password = %s'
    mycursor.execute(sql, [username, userpass])
    results = mycursor.fetchall()

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
            life_entry.delete(0, END)
            user_password.delete(0, END)


out_button = Button(root, text="Sign Out", width=20, command=out)
out_button.place(x=440, y=400)


def register():
    root.destroy()
    messagebox.showinfo("Unauthorised Access.", "Login Through The Administration Portal.")
    window = Tk()
    window.title("Admin Sign-in")
    window.geometry("500x500")
    window.config(bg="black")

    admin_username = Label(window, text="Username: ")
    admin_username.place(x=0, y=0)

    admin_entry = Entry(window, width=20)
    admin_entry.place(x=0, y=30)

    admin_password = Label(window, text="Password: ")
    admin_password.place(x=0, y=80)

    admin_entry2 = Entry(window, width=20, show="*")
    admin_entry2.place(x=0, y=110)

    def admin_login():

        username = admin_entry.get()
        userpass = admin_entry2.get()
        sql = 'Select * from Admin where Username = %s and Password = %s'
        mycursor.execute(sql, [username, userpass])
        results = mycursor.fetchall()

        if results:
            sql = 'UPDATE Admin SET Login_time = NOW() WHERE Username = %s'
            mycursor.execute(sql, [username])
            mydb.commit()

            if mycursor.rowcount > 0:
                pass

            for _ in results:
                messagebox.showinfo("Authorised Access Granted.", "Welcome To The Administration Portal.")
                window.destroy()

                admin = Tk()
                admin.title("Life Choices Administration Portal")
                admin.geometry("700x700")
                admin.config(bg="black")

                label_logo2 = Label(window, text="Life Choices", width=70, font=("Serif", 20), bg="purple")
                label_logo2.place(x=0, y=0)

                def logout():
                    sql = 'Select * from Admin where Username = %s and Password = %s'
                    mycursor.execute(sql, [username, userpass])
                    results = mycursor.fetchall()

                    if results:
                        sql = 'UPDATE Admin SET Logout_time = NOW() WHERE Username = %s'
                        mycursor.execute(sql, [username])
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            pass

                        for i in results:
                            messagebox.showinfo("Farewell.", "Exiting The Portal.")
                            root.destroy()
                            python = sys.executable
                            os.execl(python, python, *sys.argv)

                            break
                        else:
                            admin_entry.delete(0, END)
                            admin_entry2.delete(0, END)

                logout_button = Button(root, text="Exit", width=20, command=logout)
                logout_button.place(x=700, y=500)

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
                update_button.place(x=450, y=400)

                def add_User():
                    add = Tk()
                    add.title("Add User")
                    add.geometry("500x500")

                    head_label = Label(add)
                    full_name_label = Label(add, text="Full Name:")
                    user_name_label = Label(add, text="Username:")
                    password_label = Label(add, text="Password:")
                    full_name = Entry(add)
                    user_name = Entry(add)
                    password = Entry(add)

                    def create():
                        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                       host='localhost', database='lifechoicesonline')

                        mycursor = mydb.cursor()

                        x = full_name.get()
                        y = user_name.get()
                        z = password.get()

                        if x == '' or y == '' or z == '':
                            messagebox.showerror("TRY AGAIN", "Please do not leave the fields empty")
                            add.destroy()
                            create()
                        else:
                            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                                           host='localhost', database='lifechoicesonline')

                            try:
                                mycursor = mydb.cursor()
                                sql = "INSERT INTO Users(Fullname, Username, Password) VALUES(%s, %s, %s)"
                                mycursor.execute(sql, [(x), (y), (z)])
                                mydb.commit()
                            except:
                                messagebox.showerror("OOPS", "Error connecting to databases")
                            messagebox.showinfo("SUCCESS " + x + " has been added to the server")
                            add.destroy()

                    create_button = Button(add, text="Add User", command=create)

                    full_name_label.place(x=5, y=5)
                    user_name_label.place(x=5, y=45)
                    password_label.place(x=5, y=85)
                    full_name.place(x=5, y=25)
                    user_name.place(x=5, y=65)
                    password.place(x=5, y=105)
                    create_button.place(x=25, y=130)

                add_user_button = Button(root, text="Add User", width=20, command=add_User)
                add_user_button.place(x=100, y=500)

                    win = Tk()
                    win.title("DELETE")
                    win.geometry("200x200")

                    name = Label(win, text="Full Name:")
                    name.place(x=0, y=0)

                    full_name = Entry(win)
                    full_name.place(x=0, y=20)

                    name_user = Label(win, text="Username:")
                    name_user.place(x=0, y=40)

                    user_name = Entry(win)
                    user_name.place(x=0, y=60)

                    password_label = Label(win, text="Password:")
                    password_label.place(x=0, y=80)

                    password = Entry(win)
                    password.place(x=0, y=100)

                    def deleting():
                        fullname1 = full_name.get()
                        sql = "DELETE from Users where Fullname = %s"
                        messagebox.showinfo("DELETED", "Delete was a success")
                        win.destroy()

                    btn_delete = Button(win, text="Delete", width=20, command=deleting)
                    btn_delete.place(x=0, y=150)

                delete_user_button = Button(root, text="Delete User", width=20, command=delete_user)
                delete_user_button.place(x=400, y=500)

    admin_button = Button(window, text="Login", width=20, command=admin_login)
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
