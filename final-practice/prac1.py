import sqlite3
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

def connection():
    global conn, cursor
    conn = sqlite3.connect("database/login.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1100
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#94B4C1')
    root.title("Practice 1")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,3),weight=1)
    root.rowconfigure((1,2),weight=2)
    root.columnconfigure((0,3),weight=1)
    root.columnconfigure((1,2),weight=2)
    return root
    

def loginPage():
    global userEntry, pwdEntry
    loginFrame.rowconfigure((0,1,2,3), weight=1)
    loginFrame.columnconfigure((0,1), weight=1)
    loginFrame.grid(row=1, rowspan=2, column=1, columnspan=2, sticky='news')
    Label(loginFrame, bg="#94B4C1", fg="black", text="Login Account:", font="Garamond 26 bold").grid(row=0, columnspan=2, sticky="news")
    Label(loginFrame, bg="#94B4C1", fg="black", text="Username:").grid(row=1, column=0, sticky="e")
    userEntry = Entry(loginFrame, bg="white", fg="black", width=20)
    userEntry.grid(row=1, column=1, sticky="w", padx=20)
    Label(loginFrame, bg="#94B4C1", fg="black", text="Password:").grid(row=2, column=0, sticky="e")
    pwdEntry = Entry(loginFrame, bg="white", fg="black", width=20, show="*")
    pwdEntry.grid(row=2, column=1, sticky="w", padx=20)
    Button(loginFrame, bg="white", fg="black", text="Exit", width=20, command=exit).grid(row=3, column=0, ipady=15)
    Button(loginFrame, bg="white", fg="black", text="Login", width=20, command=loginClick).grid(row=3, column=1, ipady=15)

def loginClick():
    global result
    result = [1670702230, "Pariwat", "Niranon", "pariwat.nira", "pariwat123"]
    welcomePage(result)
    # if userEntry.get() == "" or pwdEntry.get() == "":
    #     messagebox.showerror("Admin", "Please enter Username or Password")
    #     userEntry.focus_force()
    # else:
    #     sql = "SELECT * FROM student where username=? AND password=?"
    #     cursor.execute(sql, [userEntry.get(), pwdEntry.get()])
    #     result = cursor.fetchone()
    #     if result:
    #         messagebox.showinfo("Admin", "Login Successfully")
    #         welcomePage(result)
    #     else:
    #         messagebox.showerror("Admin", "Invalid Username or Password")
    #         userEntry.focus_force()

def welcomePage(result):
    loginFrame.grid_forget()
    welcomeFrame.rowconfigure((0,2), weight=1)
    welcomeFrame.rowconfigure(1, weight=2)
    welcomeFrame.columnconfigure((0,1), weight=1)
    welcomeFrame.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="news")

    Label(welcomeFrame, bg="#ECEFCA", fg="black", text=f"Student ID: {result[0]}\nName: {result[1]} {result[2]}").grid(row=0, column=0, columnspan=2)
    menuFrame.rowconfigure((0,1,2), weight=1)
    menuFrame.rowconfigure(3, weight=2)
    menuFrame.columnconfigure(0, weight=1)
    menuFrame.grid(row=1, column=0, sticky="news")
    Button(menuFrame, bg="white", fg="black", width=20, text="Add", command=addClick).grid(row=0, column=0, ipady=10)
    Button(menuFrame, bg="white", fg="black", width=20, text="Update", command=updateClick).grid(row=1, column=0, ipady=10)
    Button(menuFrame, bg="white", fg="black", width=20, text="Delete", command=deleteClick).grid(row=2, column=0, ipady=10)
    Button(menuFrame, bg="white", fg="black", width=20, text="Logout", command=logoutClick).grid(row=3, column=0, ipady=10)

    bodyFrame.rowconfigure(0, weight=1)
    bodyFrame.columnconfigure(0, weight=1)
    bodyFrame.grid(row=1, column=1, sticky="news")
    Label(bodyFrame, text="Welcome Page Loaded!", bg="#94B4C1", fg="black").grid(row=0, column=0, sticky="news")


def addClick():
    bodyFrame.grid_forget()
    updateFrame.grid_forget()
    deleteFrame.grid_forget()
    addFrame.rowconfigure((0,1,2,3), weight=1)
    addFrame.columnconfigure((0,1), weight=1)
    addFrame.grid(row=1, column=1, sticky="news")
    Label(addFrame, bg="#94B4C1", fg="black", text="Add Course", font="Garamond 26 bold").grid(row=0, column=0, columnspan=2)
    Label(addFrame, bg="#94B4C1", fg="black", text="Course Code: ").grid(row=1, column=0, sticky="e")
    codeEntry = Entry(addFrame, bg="white", fg="black")
    codeEntry.grid(row=1, column=1)
    Label(addFrame, bg="#94B4C1", fg="black", text="Course Name: ").grid(row=2, column=0, sticky="e")
    nameEntry = Entry(addFrame, bg="white", fg="black")
    nameEntry.grid(row=2, column=1)
    Button(addFrame, bg="white", fg="black", text="Add", width=10).grid(row=3, column=0, columnspan=2)


def updateClick():
    bodyFrame.grid_forget()
    addFrame.grid_forget()
    deleteFrame.grid_forget()


def deleteClick():
    bodyFrame.grid_forget()
    addFrame.grid_forget()
    updateFrame.grid_forget()


def logoutClick():
    welcomeFrame.grid_forget()
    userEntry.delete(0, END)
    pwdEntry.delete(0, END)
    loginPage()
    userEntry.focus_force()


connection()
root = mainwindow()
# Frame
loginFrame = Frame(root, bg="#94B4C1")
welcomeFrame = Frame(root, bg="#ECEFCA")
menuFrame = Frame(welcomeFrame, bg="#547792")
bodyFrame = Frame(welcomeFrame, bg="#94B4C1")
addFrame = Frame(welcomeFrame, bg="#94B4C1")
updateFrame = Frame(welcomeFrame, bg="#94B4C1")
deleteFrame = Frame(welcomeFrame, bg="#94B4C1")

loginPage()
root.mainloop()