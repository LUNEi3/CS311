import tkinter as tk
from tkinter import messagebox

def root():
    root = tk.Tk()
    root.wm_geometry('1000x700+300+100')
    root.title('Homework of Week 4: Figure Shop by Pariwat Niranon')
    root.rowconfigure((0,2), weight=1)
    root.rowconfigure(1, weight=2)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    return root


def layout():
    top = tk.Frame(master, bg="#E5989B")
    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=2)
    top.rowconfigure(0, weight=1)
    top.grid(row=0, columnspan=2, sticky='news')
    
    left = tk.Frame(master, bg="#EFE9D5")
    left.rowconfigure((0,1,2), weight=1)
    left.grid(row=1, column=0, sticky='news')

    right = tk.Frame(master, bg="#FFCDB2")
    right.rowconfigure((0,1,2), weight=1)
    right.columnconfigure(0, weight=1)
    right.columnconfigure(1, weight=1)
    right.grid(row=1, column=1, sticky='news')

    bottom = tk.Frame(master, bg="#E5989B")
    bottom.grid(row=2, columnspan=2, sticky='news')

    return top,left,right,bottom


def widgets():
    btn1 = tk.Button(top, text="Click Me!", font=('sans', 16), image=icon2, compound='left', command=btnOnclick)
    btn1.grid(row=0, column=0, ipadx=30, ipady=5, sticky='e')

    btn2 = tk.Button(top, text="Exit Program", font=('sans', 16), image=icon2, compound='left', command=exit)
    btn2.grid(row=0, column=1, ipadx=30, ipady=5)

    fig1 = tk.Label(left, image=img1, bg='#EFE9D5')
    fig1.pack(pady=15)
    
    fig2 = tk.Label(left, image=img2, bg='#EFE9D5')
    fig2.pack(pady=15)

    fig3 = tk.Label(left, image=img3, bg='#EFE9D5')
    fig3.pack(pady=15)

    check1 = tk.Checkbutton(right, text='Skullpanda price = 380 THB', bg='#FFCDB2', font=('sans', 12), variable=spy1, command=showTotal)
    check1.grid(row=0, column=1, sticky='w')

    check2 = tk.Checkbutton(right, text='Dimoo price = 450 THB', bg='#FFCDB2', font=('sans', 12), variable=spy2, command=showTotal)
    check2.grid(row=1, column=1, sticky='w')

    check3 = tk.Checkbutton(right, text='Crybaby price = 350 THB', bg='#FFCDB2', font=('sans', 12), variable=spy3, command=showTotal)
    check3.grid(row=2, column=1, sticky='w')

    total = tk.Label(bottom, text="", font=('sans', 18, 'bold'), bg='#E5989B', fg="#0000FF")
    total.pack(expand=True)
    
    return total


def btnOnclick():
    messagebox.showinfo('About Shop', 'Welcome to Art Toy Shop by Popmart Official Store:\n1.Skullpanda\n2.Dimoo\n3.Crybaby')


def showTotal():
    sum = 0
    if spy1.get() == 1:
        sum += 380
    if spy2.get() == 1:
        sum += 450
    if spy3.get() == 1:
        sum += 350
    total['text'] = f"Total Price = {sum} Bahts"
    total['bg'] = '#EFE9D5'
    


master = root()

# Spy
spy1 = tk.IntVar()
spy2 = tk.IntVar()
spy3 = tk.IntVar()

# Source
img1 = tk.PhotoImage(file='image/fig1.png').subsample(4,4)
img2 = tk.PhotoImage(file='image/fig2.png').subsample(4,4)
img3 = tk.PhotoImage(file='image/fig3.png').subsample(3,3)
icon1 = tk.PhotoImage(file='image/icon1.png')
icon2 = tk.PhotoImage(file='image/icon2.png')

top,left,right,bottom = layout()
total = widgets()
master.mainloop()