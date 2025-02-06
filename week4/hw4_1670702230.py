import tkinter as tk

def root():
    root = tk.Tk()
    root.wm_geometry('1000x700+300+100')
    root.title('Pariwat Niranon')
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
    btn1 = tk.Button(top, text="Click Me!", font=('sans', 16))
    btn1.grid(row=0, column=0, ipadx=30, ipady=15, sticky='e')

    btn2 = tk.Button(top, text="Exit Program", font=('sans', 16), command=exit)
    btn2.grid(row=0, column=1, ipadx=30, ipady=15)

    fig1 = tk.Label(left, image=img1, bg='#EFE9D5')
    fig1.pack(pady=15)
    
    fig2 = tk.Label(left, image=img2, bg='#EFE9D5')
    fig2.pack(pady=15)

    fig3 = tk.Label(left, image=img3, bg='#EFE9D5')
    fig3.pack(pady=15)

    check1 = tk.Checkbutton(right, text='Skullpanda price = 380 THB', bg='#FFCDB2', font=('sans', 12))
    check1.grid(row=0, column=1, sticky='w', padx=20)

    check2 = tk.Checkbutton(right, text='Dimoo price = 450 THB', bg='#FFCDB2', font=('sans', 12))
    check2.grid(row=1, column=1, sticky='w', padx=20)

    check3 = tk.Checkbutton(right, text='Crybaby price = 350 THB', bg='#FFCDB2', font=('sans', 12))
    check3.grid(row=2, column=1, sticky='w', padx=20)

    total = tk.Label(bottom, text="", font=('sans', 18, 'bold'), bg='#E5989B', fg="#0000FF")
    total.pack(expand=True)
    
    return total

master = root()

# Source
img1 = tk.PhotoImage(file='image/fig1.png').subsample(4,4)
img2 = tk.PhotoImage(file='image/fig2.png').subsample(4,4)
img3 = tk.PhotoImage(file='image/fig3.png').subsample(3,3)

top,left,right,bottom = layout()
total = widgets()
master.mainloop()