import tkinter as tk

def root():
    root = tk.Tk()
    root.title("Homework Week3 : Design layout Frame")
    root.wm_geometry("1000x700+300+100")
    root.rowconfigure((0,2), weight=1)
    root.rowconfigure(1, weight=2)
    root.columnconfigure(0, weight=1)
    root.option_add('*font', 'Garamond 20')
    return root


def layout():
    top = tk.Frame(master, bg="#3E5879")
    top.grid(row=0, sticky='news')
    
    mid = tk.Frame(master, bg="#F5EFE7")
    mid.rowconfigure(0, weight=1)
    mid.columnconfigure(0, weight=2)
    mid.columnconfigure(1, weight=1)
    mid.grid(row=1, sticky='news')

    left = tk.Frame(mid, bg="#FFFFFF")
    left.columnconfigure(0, weight=1)
    left.columnconfigure(1, weight=2)
    left.rowconfigure(0, weight=1)
    left.rowconfigure(1, weight=2)
    left.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    right = tk.Frame(mid, bg="#FFFFFF")
    right.grid(column=1, row=0, sticky='news', padx=10, pady=10)

    bottom = tk.Frame(master, bg="#D8C4B6")
    bottom.rowconfigure(0, weight=1)
    bottom.columnconfigure((0,1,2,3), weight=1)
    bottom.grid(row=2, sticky='news')

    return {'top': top, 'mid': mid, 'left': left, 'right': right, 'bottom': bottom}


def widget():
    text = "Name: Pariwat Niranon\n\nStudent\n\nInfomation Technology and Innovation"

    title = tk.Label(parts["top"], text="Dash DIY by Pariwat Niranon", fg="#FFFFFF", bg="#3E5879", font=('comic sans ms', 24, "bold"))
    title.pack(expand = True)

    profile = tk.Label(parts["left"], text=text, justify='left', bg="#FFFFFF", font=('sans ms', 16))
    profile.grid(row=0, column=1, sticky='w')

    avata = tk.Label(parts["left"], image=avataImg, bg="#FFFFFF")
    avata.grid(row=0, column=0)

    bar = tk.Label(parts["left"], image=barColor, bg="#FFFFFF")
    bar.grid(row=1, columnspan=2)

    skill = tk.Label(parts["right"], image=skillImg, bg="#FFFFFF")
    skill.pack(expand= True, padx=10)

    btn1 = tk.Button(parts["bottom"], text="Click 1", font=('sans ms', 16))
    btn1.grid(row=0, column=0, padx=10, pady=10, ipadx=25, ipady=10)

    btn2 = tk.Button(parts["bottom"],  text="Click 2", font=('sans ms', 16))
    btn2.grid(row=0, column=1, padx=10, pady=10, ipadx=25, ipady=10)

    btn3 = tk.Button(parts["bottom"],  text="Click 3", font=('sans ms', 16))
    btn3.grid(row=0, column=2, padx=10, pady=10, ipadx=25, ipady=10)

    exitBtn = tk.Button(parts["bottom"], text="Exit Program", font=('sans ms', 16), command=exit)
    exitBtn.grid(row=0, column=3, padx=10, pady=10, ipadx=25, ipady=10)


master = root()
parts = layout()

# Source
avataImg = tk.PhotoImage(file="image/avataaars.png").subsample(3,3)
barColor = tk.PhotoImage(file="image/barcolor.png").subsample(2,2)
skillImg = tk.PhotoImage(file="image/skill.png")

widget()
master.mainloop()