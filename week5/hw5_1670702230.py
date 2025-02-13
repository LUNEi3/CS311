import tkinter as tk 

def root():
    root = tk.Tk()
    root.wm_geometry('1000x700+300+100')
    root.title('Dream Fashion (hw5) By Pariwat Niranon')
    root.rowconfigure((0,2), weight=1)
    root.rowconfigure(1, weight=4)
    root.columnconfigure((0,1), weight=1)
    return root


def layouts():
    top = tk.Frame(master, bg='#AB886D')
    top.grid(row=0, columnspan=2, sticky='news')

    left = tk.Frame(master, bg='#D6C0B3')
    left.rowconfigure((0,1,2,3), weight=1)
    left.columnconfigure((0,1), weight=1)
    left.grid(row=1, column=0, sticky='news')

    right = tk.Frame(master, bg='#E4E0E1')
    right.rowconfigure((0,1,2,3), weight=1)   
    right.columnconfigure((0,1), weight=1)
    right.grid(row=1, column=1, sticky='news')

    bottom = tk.Frame(master, bg='#AB886D')
    bottom.rowconfigure(0, weight=1)
    bottom.columnconfigure((0,1), weight=1)
    bottom.grid(row=2, columnspan=2, sticky='news')

    return top,left,right,bottom



def widget():
    tk.Label(top, text='Dream Fashion by Pariwat Niranon', bg='#AB886D', font=("Garamond",24)).pack(expand=True)

    shirtSpy = [tk.IntVar() for i in (shirtTexts)]
    for i,item in enumerate(shirtTexts):
        tk.Label(left, image=shirts[i], bg='#D6C0B3').grid(row=i, column=0)
        tk.Checkbutton(left, text=item, bg='#D6C0B3', font=("Garamond",12), variable=shirtSpy[i], command=handleClick).grid(row=i, column=1)

    shoeSpy = [tk.IntVar() for i in (shoeTexts)]
    for i,item in enumerate(shoeTexts):
        tk.Label(right, image=shoes[i], bg='#E4E0E1').grid(row=i, column=0)
        tk.Checkbutton(right, text=item, bg='#E4E0E1', font=("Garamond",12), variable=shoeSpy[i], command=handleClick).grid(row=i, column=1)

    lbt = tk.Label(bottom, bg='#AB886D', font=("Garamond",12))
    lbt.grid(row=0, column=0)
    rbt = tk.Label(bottom, bg='#AB886D', font=("Garamond",12))
    rbt.grid(row=0, column=1)

    return shoeSpy,shirtSpy,lbt,rbt


def handleClick(): 
    shirtPrice = 0
    shoePrice = 0
    for i,item in enumerate(shirtTexts):
        if shirtSpy[i]:
            shirtPrice += shirtSpy[i].get() * int(item.split('\n')[1].split(' ')[0])
        if shoeSpy[i]:
            shoePrice += shoeSpy[i].get() * int(shoeTexts[i].split('\n')[1].split(' ')[0])

    lbt['text'] = f"Shirt Total Amount = {shirtPrice:.2f} Bahts"
    lbt['bg'] = '#D6C0B3'
    rbt['text'] = f"Shoes Total Amount = {shoePrice:.2f} Bahts"
    rbt['bg'] = '#D6C0B3'



master = root()

# Sources 
shirt1 = tk.PhotoImage(file="./image/shirt1.png")
shirt2 = tk.PhotoImage(file="./image/shirt2.png")
shirt3 = tk.PhotoImage(file="./image/shirt3.png")
shirt4 = tk.PhotoImage(file="./image/shirt4.png")
shirtTexts = ['Pink T-Shirt\n225 B.', 'Blue T-Shirt\n210 B.', 'Lemon T-Shirt\n215 B.', 'Orange T-Shirt\n1000 B.']
shirts = [shirt1, shirt2, shirt3, shirt4]

shoe1 = tk.PhotoImage(file='./image/shoe1.png')
shoe2 = tk.PhotoImage(file='./image/shoe2.png')
shoe3 = tk.PhotoImage(file='./image/shoe3.png')
shoe4 = tk.PhotoImage(file='./image/shoe4.png')
shoeTexts = ['VAN Black Color\n2800 B.', 'VAN Blue Color\n2750 B.', 'VAN Red Color\n3000 B.', 'VAN Green Color\n2900 B.']
shoes = [shoe1, shoe2, shoe3, shoe4]

top,left,right,bottom = layouts()
shoeSpy,shirtSpy,lbt,rbt = widget()
master.mainloop()