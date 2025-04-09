from secrets import choice
import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('database/login.db')
    cursor = conn.cursor()


def mainwindow() :
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28b5b5')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() : #activity of week10
    global userentry
    global pwdentry
    global loginframe
    
    loginframe = Frame(root,bg='#8fd9a8')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    
    Label(loginframe,text="Login/Register Application",font="Garamond 26 bold",image=img1,compound=LEFT,bg='#8fd9a8',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="User name : ",bg='#8fd9a8',fg='#000000',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff', fg='#000000',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff', fg='#000000',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#8fd9a8',fg='#000000',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=loginclick).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)
    Button(loginframe,text="Register",width=10,command=regiswindow).grid(row=3,column=1,pady=20,ipady=15,sticky='w',padx=20)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def loginclick() :   #activity of week10
    global result
    print("Hello from loginclick")
    if userinfo.get() == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            if pwdinfo.get() == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from login where user=? and pwd=? "
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(result)
                    update_page(result[2],result[3])
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.focus_force()

def update_page(fname,lname) :
    global upatepage,left,right
    loginframe.grid_forget() # loginframe.destroy()
    root.title("Welcome to DIY Application")
    name = fname+" "+lname
    upatepage = Frame(root,bg='#709fb0')
    upatepage.option_add("*font","Garamond 20")
    upatepage.rowconfigure((0,1,2,3,4,5,6),weight=1)
    upatepage.columnconfigure((0,1,2),weight=1)

    left = Frame(upatepage,bg='#8fd9a8')
    left.columnconfigure((0,1,2,3),weight=1)
    left.grid(row=0,column=0,sticky='news',rowspan=7)
    right = Frame(upatepage,bg='#d2e69c')
    right.columnconfigure((0,1),weight=1)
    right.grid(row=0,column=1,columnspan=2,sticky='news',rowspan=7)

    heading = Label(right,text="Name : "+name,bg="#d2e69c",fg='blue')
    heading.grid(row=0,column=0,columnspan=2,pady=20)
    global findoption,search_box
    choice = ["User Name","First Name","Last Name"]
    findoption = StringVar()
    findoption.set("User Name")
    option = OptionMenu(left,findoption,"User Name","First Name","Last Name")
    option.grid(row=0,column=0,pady=20,sticky='e')

    search_box = Entry(left,width=25)
    search_box.grid(row=0,column=1,columnspan=2,pady=20,sticky='e')

    search_button = Button(left,image=img2,command=clickoption)
    search_button.grid(row=0,column=3,pady=20)

    upatepage.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def clickoption() :
    global result,userbox,pwdbox,fnamebox,lnamebox,searchspy
    print(findoption.get())
    optiondata = findoption.get()
    if optiondata == "User Name" :
        sql = "SELECT * FROM login WHERE user=?"
    elif optiondata == "First Name":
        sql = "SELECT * FROM login WHERE fname=?"
    else:
        sql = "SELECT * FROM login WHERE lname=?"
    cursor.execute(sql, [search_box.get()])
    result = cursor.fetchall()
    if result:
        leftnew = Frame(upatepage,bg='#8fd9a8')
        leftnew.columnconfigure((0,1,2,3),weight=1)
        leftnew.grid(row=1,column=0,sticky='news',rowspan=7)
        line = 0
        for i in result:
            userdata = f"{i[0]} {i[1]} {i[2]} {i[3]}"
            Radiobutton(leftnew,bg='#8fd9a8',text="",value=line,variable=searchspy,command=clickradio).grid(row=line+1,column=0,sticky='e')
            Label(leftnew,text=userdata,bg='#8fd9a8').grid(row=line+1,column=1,sticky='w',ipadx=30)
            line = line+1
    else:
        messagebox.showinfo("Admin", "User data not found")
        leftnew = Frame(upatepage,bg='#8fd9a8')
        leftnew.columnconfigure((0,1,2,3),weight=1)
        leftnew.grid(row=1,column=0,sticky='news',rowspan=7)
    

    #color hex code bg='#d2e69c' for userbox, pwdbox, fnamebox, lnamebox
    Label(right,text="User Name : ",bg='#d2e69c').grid(row=1,column=0,stick='e')
    userbox = Entry(right,width=20)
    userbox.grid(row=1,column=1,sticky='w',pady=10)
    Label(right,text="Password : ",bg='#d2e69c').grid(row=2,column=0,stick='e')
    pwdbox = Entry(right,width=20)
    pwdbox.grid(row=2,column=1,sticky='w',pady=10) 
    Label(right,text="First Name : ",bg='#d2e69c').grid(row=3,column=0,stick='e')
    fnamebox = Entry(right,width=20)
    fnamebox.grid(row=3,column=1,sticky='w',pady=10) 
    Label(right,text="Last Name : ",bg='#d2e69c').grid(row=4,column=0,stick='e')
    lnamebox = Entry(right,width=20)
    lnamebox.grid(row=4,column=1,sticky='w',pady=10) 

def clickradio() :
    row = searchspy.get()
    print(result[row][0],result[row][1],result[row][2],result[row][3])
    #clear old user data
    userbox['state'] = "normal"
    userbox.delete(0,END)
    pwdbox.delete(0,END)
    fnamebox.delete(0,END)
    lnamebox.delete(0,END)
    #insert new user data
    userbox.insert(0, result[row][0])
    pwdbox.insert(0, result[row][1])
    fnamebox.insert(0, result[row][2])
    lnamebox.insert(0, result[row][3])
    userbox['state'] = "readonly"

    update_button = Button(right,text="Update Now",command=updateclick)
    update_button.grid(row=5,column=1,ipadx=5,ipady=5,pady=20)
    login_button = Button(right,text="Back to Login",command=loginlayout)
    login_button.grid(row=5,column=0,ipadx=5,ipady=5,pady=20)

def updateclick() :
    sql = "UPDATE login SET pwd=?, fname=?, lname=? WHERE user=?"
    cursor.execute(sql, [pwdbox.get(), fnamebox.get(), lnamebox.get(), userbox.get()])
    messagebox.showinfo("Admin", "Update completed")


    #clear old data after update acton
    leftnew = Frame(upatepage,bg='#8fd9a8')
    leftnew.grid(row=1,column=0,sticky='news',rowspan=7)
    userbox['state'] = "normal"
    #clear old user data
    userbox.delete(0,END)
    pwdbox.delete(0,END)
    fnamebox.delete(0,END)
    lnamebox.delete(0,END)
    
def regiswindow() : #activity of week11
    global fullname,lastname,newuser,newpwd,cfpwd,regisframe
    #loginframe.destroy()
    root.title("Welcome to User Registration : ")
    root.config(bg='#d2e69c')
    regisframe = Frame(root,bg='#8fd9a8')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    Label(regisframe,text="Registration Form",font="Garamond 26 bold",fg='#e4fbff',image=img1,compound=LEFT,bg='#28b5b5').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Full name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=1,column=1,sticky='w',padx=10)
    Label(regisframe,text='Last name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=2,column=1,sticky='w',padx=10)
    Label(regisframe,text="Username : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=3,column=1,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=5,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=5,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register Submit",command=registration)
    regisaction.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,text="Back to Login",command=loginlayout)
    loginbtn.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')


def registration() :    #activity of week11 
    print("Hello from registration")
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin: ","Pleasse enter lastname")
        lastname.focus_force()
    elif newuser.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a new username")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a password")
        newpwd.focus_force()
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a confirm password")
        cfpwd.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : #a new pwd / confirm is correct 
                sql = "insert into login values (?,?,?,?)"
                param = [newuser.get(),newpwd.get(),fullname.get(),lastname.get()]
                cursor.execute(sql,param)
                conn.commit()
                retrivedata()
                messagebox.showinfo("Admin:","Registration Successfully")
                newuser.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                fullname.delete(0,END)
                lastname.delete(0,END)
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.selection_range(0,END)
                cfpwd.focus_force()

def retrivedata() :
    sql = "select * from login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

#------- main program ---------
createconnection()
root = mainwindow()
regisframe = Frame(root)
userinfo = StringVar()
pwdinfo = StringVar()
searchspy = IntVar()
img1 = PhotoImage(file='images/profile.png').subsample(5,5)
img2 = PhotoImage(file='images/search.png')
loginlayout()
root.mainloop()
# cursor.close()
# conn.close()