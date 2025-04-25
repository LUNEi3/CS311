import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/login.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1100
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28b5b5')
    root.title("Week13 Insert/Update/Delete Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,3),weight=1)
    root.rowconfigure((1,2),weight=2)
    root.columnconfigure((0,3),weight=1)
    root.columnconfigure((1,2),weight=2)
    return root

def loginlayout() :
    global userentry,pwdentry
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    Label(loginframe,text="Account Login",font="Garamond 26 bold",image=img3,compound=LEFT,bg='#8fd9a8',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="Username : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=40)
    Button(loginframe,text="Exit",width=10,command=root.quit).grid(row=3,column=0,pady=10,ipady=15,sticky='w',padx=45)

def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force()
    else :
        sql = "select * from student where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from student where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()


def welcomepage(result) :
    global top,left,right,bottom
    loginframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#FCC2FC"
    welcomeframe.grid_rowconfigure((0),weight=1)
    welcomeframe.grid_rowconfigure((1),weight=5)
    welcomeframe.grid_rowconfigure((2),weight=1)
    welcomeframe.grid_columnconfigure((0),weight=1)
    welcomeframe.grid_columnconfigure((1),weight=5)
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    top = Frame(welcomeframe,bg='#FFF1D5')
    top.grid_rowconfigure((0,1),weight=1)
    top.grid_columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    left = Frame(welcomeframe,bg='#BDDDE4')
    left.grid_rowconfigure((0,1,2,3),weight=1)
    left.grid_rowconfigure((4),weight=3)
    left.grid_columnconfigure(0,weight=1)
    left.grid(row=1,column=0,sticky='news')
    right = Frame(welcomeframe,bg='#9EC6F3')
    right.grid_rowconfigure((0),weight=1)
    right.grid_columnconfigure(0,weight=1)
    right.grid(row=1,column=1,sticky='news')
    bottom = Frame(welcomeframe,bg='#FFF1D5')
    bottom.grid(row=2,columnspan=2,sticky='news')
    #create widgets
    Label(top,image=img1,bg='#FFF1D5',text="Student ID : "+str(result[0])+"\n"+"Name : "+result[1]+" "+result[2],compound=LEFT).grid(row=0)
    Button(left,text="Add Course",width=10,command=addclick).grid(row=1,ipady=10)
    Button(left,text="Update Course",width=10,command=updateclick).grid(row=2,ipady=10)
    Button(left,text="Delete Course",width=10,command=deleteclick).grid(row=3,ipady=10)
    Button(left,text="Logout",width=10,command=logoutclick).grid(row=4,ipady=10)
    Label(right,image=img4,bg='#BDDDE4').grid(row=0)

def addclick() :
    global addframe
    global codebox,namebox,daybox,roombox
    right.grid_forget()
    updateframe.grid_forget()
    deleteframe.grid_forget()
    addframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    addframe.grid_columnconfigure((0,1),weight=1)
    addframe.grid(row=1,column=1,sticky='news')
    Label(addframe,text="Add Course",font="Garamond 26 bold",image=img5,compound=LEFT,bg='#9EC6F3').grid(row=0,columnspan=2)
    Label(addframe,text="Course Code : ",bg='#9EC6F3').grid(row=1,column=0,sticky='e')
    codebox = Entry(addframe,bg="#DAF5FF")
    codebox.grid(row=1,column=1,sticky='w',padx=20)
    Label(addframe,text="Course Name : ",bg='#9EC6F3').grid(row=2,column=0,sticky='e')
    namebox = Entry(addframe,bg="#DAF5FF")
    namebox.grid(row=2,column=1,sticky='w',padx=20)
    Label(addframe,text="Day : ",bg='#9EC6F3').grid(row=3,column=0,sticky='e')
    daybox = Entry(addframe,bg="#DAF5FF")
    daybox.grid(row=3,column=1,sticky='w',padx=20)
    Label(addframe,text="Room : ",bg='#9EC6F3').grid(row=4,column=0,sticky='e')
    roombox = Entry(addframe,bg="#DAF5FF")
    roombox.grid(row=4,column=1,sticky='w',padx=20)
    Button(addframe,text="Add",width=10,command=addcourse).grid(row=5,columnspan=2,ipady=10)

def addcourse() :
    if codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else : 
        #define sql select command of course code or course name for duplicating
        sql = "SELECT * FROM course WHERE course_code=? OR course_name=?"
        #execute step
        cursor.execute(sql, [codebox.get(), namebox.get()])
        
        #fetch result
        result = cursor.fetchone()
        if result :
            messagebox.showwarning("Admin: ","Course code or name already exist.")
            codebox.select_range(0,END)
            codebox.focus_force()
        else :
            #define insert command for insert a new record into the table
            sql = "INSERT INTO course VALUES (NULL,?,?,?,?)"
            #execute step
            cursor.execute(sql, [codebox.get(), namebox.get(), daybox.get(), roombox.get()])
            #commit step
            conn.commit()
            
            messagebox.showinfo("Admin:","Add course successfully")
            clearclick()

def searchclick() :
    sql = "select * from course where course_code=? COLLATE NOCASE"
    #execute step
    cursor.execute(sql,[searchbox.get()])
    #fetch result
    result = cursor.fetchone()
    if result :
        codebox.config(state='normal')
        codebox.delete(0,END)
        codebox.insert(0,result[1])
        codebox.config(state='readonly')
        namebox.delete(0,END)
        namebox.insert(0,result[2])
        daybox.delete(0,END)
        daybox.insert(0,result[3])
        roombox.delete(0,END)
        roombox.insert(0,result[4])
    else :
        messagebox.showwarning("Admin: ","Course code not found\n Try again.")
        searchbox.select_range(0,END)
        searchbox.focus_force()
        codebox.config(state='normal')
        namebox.delete(0,END)
        daybox.delete(0,END)
        roombox.delete(0,END)
        codebox.delete(0,END)
 
def updateclick() :
    global searchbox,codebox,namebox,daybox,roombox
    right.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    updateframe.grid_rowconfigure((0,1,2,3,4,5,6),weight=1)
    updateframe.grid_columnconfigure((0,1),weight=1)
    updateframe.grid(row=1,column=1,sticky='news')
    Label(updateframe,text="Update Course",font="Garamond 26 bold",image=img5,compound=LEFT,bg='#9EC6F3').grid(row=0,columnspan=2)
    Label(updateframe,text="Course Code : ",bg='#9EC6F3').grid(row=1,column=0,sticky='e')
    searchbox = Entry(updateframe,bg="#DAF5FF")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(updateframe,text="Search",command=searchclick).grid(row=1,column=1,ipady=10)
    Label(updateframe,text="Course Code : ",bg='#9EC6F3').grid(row=2,column=0,sticky='e')
    codebox = Entry(updateframe,bg="#DAF5FF")
    codebox.grid(row=2,column=1,sticky='w',padx=20)
    Label(updateframe,text="Course Name : ",bg='#9EC6F3').grid(row=3,column=0,sticky='e')
    namebox = Entry(updateframe,bg="#DAF5FF")
    namebox.grid(row=3,column=1,sticky='w',padx=20)
    Label(updateframe,text="Day : ",bg='#9EC6F3').grid(row=4,column=0,sticky='e')
    daybox = Entry(updateframe,bg="#DAF5FF")
    daybox.grid(row=4,column=1,sticky='w',padx=20)
    Label(updateframe,text="Room : ",bg='#9EC6F3').grid(row=5,column=0,sticky='e')
    roombox = Entry(updateframe,bg="#DAF5FF")
    roombox.grid(row=5,column=1,sticky='w',padx=20)
    Button(updateframe,text="Update Course",width=10,command=updatecourse).grid(row=6,columnspan=2,ipady=10)

def updatecourse() :
    global codebox,namebox,daybox,roombox
    if codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else :
        #define sql select command to checking course code exist or not
        sql = "select * from course where course_code=? "
        #execute step
        cursor.execute(sql,[codebox.get()])
        #fetch result
        result = cursor.fetchone()
        if result :
            #define sql select command of course name for duplicating
            sql = "select * from course where course_name=?"
            #execute step
            cursor.execute(sql,[namebox.get()])
            #fetch result
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated course name")
                #define sql for updating only day and room fields
                sql = """ 
                    UPDATE course 
                    SET day=?, 
                        room=?
                    WHERE course_code=?
                """
                #execute step
                cursor.execute(sql, [daybox.get(), roombox.get(), codebox.get()])            

                #commit step
                conn.commit()
               
                messagebox.showinfo("Admin:","Update course successfully")
                clearclick()

            else :
                #define sql update command for updating course name, day and room
                sql = """
                    UPDATE course
                    SET course_name=?,
                        day=?,
                        room=?
                    WHERE course_code=?
                """
                #execute step
                cursor.execute(sql, [namebox.get(), daybox.get(), roombox.get(), codebox.get()])

                #commit step
                conn.commit()
                
                messagebox.showinfo("Admin:","Update course successfully")
                clearclick()
        else :
            messagebox.showwarning("Admin: ","Course code not found\n Try again.")
            codebox.select_range(0,END)
            codebox.focus_force()


def deleteclick() :
    global searchbox,codebox,namebox,daybox,roombox
    updateframe.grid_forget()
    addframe.grid_forget()
    right.grid_forget()
    deleteframe.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    deleteframe.grid_columnconfigure((0,1),weight=1)
    deleteframe.grid(row=1,column=1,sticky='news')
    Label(deleteframe,text="Delete Course",font="Garamond 26 bold",image=img5,compound=LEFT,bg='#9EC6F3').grid(row=0,columnspan=2)
    Label(deleteframe,text="Course Code : ",bg='#9EC6F3').grid(row=1,column=0,sticky='e')
    searchbox = Entry(deleteframe,bg="#DAF5FF")
    searchbox.grid(row=1,column=1,sticky='w',padx=20)
    Button(deleteframe,text="Search",command=searchclick).grid(row=1,column=1,ipady=10)
    Label(deleteframe,text="Course Code : ",bg='#9EC6F3').grid(row=2,column=0,sticky='e')
    codebox = Entry(deleteframe,bg="#DAF5FF")
    codebox.grid(row=2,column=1,sticky='w',padx=20)
    Label(deleteframe,text="Course Name : ",bg='#9EC6F3').grid(row=3,column=0,sticky='e')
    namebox = Entry(deleteframe,bg="#DAF5FF")
    namebox.grid(row=3,column=1,sticky='w',padx=20)
    Label(deleteframe,text="Day : ",bg='#9EC6F3').grid(row=4,column=0,sticky='e')
    daybox = Entry(deleteframe,bg="#DAF5FF")
    daybox.grid(row=4,column=1,sticky='w',padx=20)
    Label(deleteframe,text="Room : ",bg='#9EC6F3').grid(row=5,column=0,sticky='e')
    roombox = Entry(deleteframe,bg="#DAF5FF")
    roombox.grid(row=5,column=1,sticky='w',padx=20)
    Button(deleteframe,text="Delete Course",width=10,command=deletecourse).grid(row=6,columnspan=2,ipady=10)

def deletecourse() :
    if codebox.get() == "":
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else :
        cf = messagebox.askquestion("Admin : ","Confirm to delete (Yes/No)")
        if cf == 'yes' :
            #define sql command or sql statement for deletion
            sql = "DELETE FROM course WHERE course_code=?"
            #execute sql using cursor
            cursor.execute(sql, [codebox.get()])
            #confirm/save data updated using commit() method
            conn.commit()
            messagebox.showinfo("Admin : ","Delete Successfully")
            clearclick()

def clearclick() :
    codebox.config(state='normal')
    codebox.delete(0,END)
    namebox.delete(0,END)
    daybox.delete(0,END)
    roombox.delete(0,END)
       
def logoutclick() :
    updateframe.grid_forget()
    addframe.grid_forget()
    deleteframe.grid_forget()
    right.grid_forget()
    top.grid_forget()
    bottom.grid_forget()
    left.grid_forget()
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    loginlayout() 

connection()
root = mainwindow()
loginframe = Frame(root,bg='#8fd9a8')
welcomeframe = Frame(root,bg='#FCC2FC')
updateframe = Frame(root,bg="#E5FDD1")
pwdframe = Frame(root,bg='#28b5b5')
addframe = Frame(welcomeframe,bg='#9EC6F3')
updateframe = Frame(welcomeframe,bg='#9EC6F3')
deleteframe = Frame(welcomeframe,bg='#9EC6F3')
selectoption = StringVar()
title = ["Course Code:","Course Name:","Day:","Room:"]
img1 = PhotoImage(file='images/profile.png').subsample(6,6)
img2 = PhotoImage(file='images/search.png')
img3 = PhotoImage(file="images/login.png").subsample(6,6)
img4 = PhotoImage(file='images/books.png')
img5 = PhotoImage(file='images/books.png').subsample(6,6)
loginlayout()
root.mainloop()
cursor.close()
conn.close()