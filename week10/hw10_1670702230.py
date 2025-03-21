import tkinter
import tkinter.messagebox
import sqlite3

def root():
    root = tkinter.Tk()
    root.title('HW10_1670700230')
    root.geometry('800x600')
    root.rowconfigure((0,1,2), weight=1)
    root.columnconfigure((0,1,2), weight=1)
    root.configure(bg='#F5EFE7')
    return root


def layout(master):
    global usename, pwd
    login.columnconfigure((0,1), weight=1)
    login.rowconfigure((0,1,2,3,4), weight=1)
    login.grid(row=1, column=0, columnspan=3, sticky='nsew')
    tkinter.Label(login, image=img, bg='#F5EFE7').grid(row=0, rowspan=5, column=0)
    tkinter.Label(login, text='Username:', bg='#F5EFE7', font=('Arial', 16)).grid(row=0, column=1, sticky='w')
    usename = tkinter.Entry(login, width=25, font=('Arial', 16))
    usename.grid(row=1, column=1, sticky='wn')
    tkinter.Label(login, text='Password:', bg='#F5EFE7', font=('Arial', 16)).grid(row=2, column=1, sticky='w')
    pwd = tkinter.Entry(login, width=25, font=('Arial', 16), show='*')
    pwd.grid(row=3, column=1, sticky='wn')
    tkinter.Button(login, text='Login', font=('Arial', 16), command=loginCheck, width=10).grid(row=4, column=1, sticky='ws')
  

def loginCheck():
    if usename.get() == "":
        tkinter.messagebox.showwarning('Admin', 'Please enter your username!')
        usename.focus_force()
    elif pwd.get() == "":
        tkinter.messagebox.showwarning('Admin', 'Please enter your password!')
        pwd.focus_force()
    else:
        sql = "SELECT * FROM student WHERE username = ?"
        cursor.execute(sql, [usename.get()])
        result = cursor.fetchone()
        if result:
            sql = "SELECT * FROM student WHERE password = ?"
            cursor.execute(sql, [pwd.get()])
            result = cursor.fetchone()
            if result:
                tkinter.messagebox.showinfo('Admin', 'Login successfully!')
                profileWindow(result)
            else:
                tkinter.messagebox.showwarning('Admin', 'Password is incorrect!')
                pwd.delete(0, 'end')
                pwd.focus_force()
        else:
            tkinter.messagebox.showwarning('Admin', 'Username is incorrect!')
            usename.select_range(0, 'end')
            usename.focus_force()


def profileWindow(result):
    login.grid_forget()
    profile.columnconfigure((0,1), weight=1)
    profile.rowconfigure((1,2,3,4), weight=1)
    profile.rowconfigure((0,5), weight=2)
    profile.grid(row=0, rowspan=3, column=0, columnspan=3, sticky='nsew')

    score = result[3] + result[4]
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    tkinter.Label(profile, image=img, bg='#4F709C').grid(row=0, column=0, columnspan=2)
    tkinter.Label(profile, text='Student ID:', bg='#4F709C', font=('Arial', 16), fg="white").grid(row=1, column=0, sticky='e', padx=50)
    tkinter.Label(profile, text=result[0], bg='#4F709C', font=('Arial', 16), fg="white").grid(row=1, column=1, sticky='w', padx=10)
    tkinter.Label(profile, text='Name:', bg='#4F709C', font=('Arial', 16), fg="white").grid(row=2, column=0, sticky='e', padx=50)
    tkinter.Label(profile, text=result[1] + " " + result[2], bg='#4F709C', font=('Arial', 16), fg="white").grid(row=2, column=1, sticky='w', padx=10)
    tkinter.Label(profile, text='Score:', bg='#4F709C', font=('Arial', 16), fg="white").grid(row=3, column=0, sticky='e', padx=50)
    tkinter.Label(profile, text=f"{score}", bg='#4F709C', font=('Arial', 16), fg="white").grid(row=3, column=1, sticky='w', padx=10)
    tkinter.Label(profile, text='Grade:', bg='#4F709C', font=('Arial', 16), fg="white").grid(row=4, column=0, sticky='e', padx=50)
    tkinter.Label(profile, text=grade, bg='#4F709C', font=('Arial', 16), fg="white").grid(row=4, column=1, sticky='w', padx=10)
    tkinter.Button(profile, text='Logout', font=('Arial', 16), width=10, command=logout).grid(row=5, column=0, columnspan=2)


def logout():
    profile.grid_forget()
    login.grid(row=1, column=0, columnspan=3, sticky='nsew')
    usename.delete(0, 'end')
    pwd.delete(0, 'end')
    usename.focus_force()


# Sqlite3
conn = sqlite3.connect('db/db_week10.db')
cursor = conn.cursor()

master = root()
img = tkinter.PhotoImage(file='images/man.png').subsample(3)
login = tkinter.Frame(master, bg='#F5EFE7')
profile = tkinter.Frame(master, bg='#4F709C')
layout(master)
master.mainloop()