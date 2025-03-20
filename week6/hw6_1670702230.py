import tkinter as tk

def root():
    root = tk.Tk()
    root.geometry('800x700+300+100')
    root.title('Homework Week 6 : Sweet Home Cafe Application by Pariwat Niranon')
    root.config(bg='#D9EAFD')
    root.rowconfigure((0), weight=1)
    root.columnconfigure((0), weight=1)
    root.columnconfigure((1), weight=6)
    return root

def layouts():
    left.rowconfigure((0,1,2,), weight=1)
    left.columnconfigure(0, weight=1)
    left.grid(row=0, column=0, sticky='news')

def leftframe():
    tk.Button(left, text='Product Menu', font=('comic sans ms',16), command=menuClick, image=icon1, compound='top').grid(row=0, column=0, sticky='news')
    tk.Button(left, text='Check Out', font=('comic sans ms',16), command=checkoutClick, image=icon2, compound='top').grid(row=1, column=0, sticky='news')
    tk.Button(left, text='Close Program', command=exit, font=('comic sans ms',16), image=icon3, compound='left').grid(row=2, column=0, sticky='news')

def menuClick():
    checkout.grid_forget()
    menu.rowconfigure((0,1,2), weight=1)
    menu.columnconfigure((0,1), weight=1)
    menu.grid(row=0, column=1, sticky='news')
    cakeImg = [c1,c2,c3]
    drinkImg = [d1,d2,d3]
    for i in range(len(cakemenu)):
        tk.Label(menu, bg="#D9EAFD", text=f"{cakemenu[i]}\nPrice:{price1[i]}", font=('comic sans ms', 10), image=cakeImg[i], compound='right').grid(row=i, column=0)
        tk.Label(menu, bg="#D9EAFD", text=f"{drinkmenu[i]}\nPrice:{price2[i]}", font=('comic sans ms', 10), image=drinkImg[i], compound='right').grid(row=i, column=1)
        tk.Spinbox(menu, from_=0, to=100, textvariable=cakeSpy[i], justify='center', width=15).grid(row=i, column=0, sticky='s', pady=25)
        tk.Spinbox(menu, from_=0, to=100, textvariable=drinkSpy[i], justify='center', width=15).grid(row=i, column=1, sticky='s', pady=25)

def checkoutClick():
    menu.grid_forget()
    sumCake = 0
    sumDrink = 0
    for i in range(len(price1)):
        sumCake += cakeSpy[i].get() * price1[i]
        sumDrink += drinkSpy[i].get() * price2[i]
    

    checkout.rowconfigure((0,3), weight=2)
    checkout.rowconfigure((1,2), weight=1)
    checkout.columnconfigure(0, weight=1)
    checkout.grid(row=0, column=1, sticky='news')
    tk.Label(checkout, text='~ Summary of Cake/Drink Menu ~', font=('comic sans ms', 16, 'bold'), bg="#D9EAFD").grid(row=0, column=0, sticky='news')
    tk.Label(checkout, text=f'Total cake price is {sumCake:,.2f} Bath', font=('comic sans ms', 12, 'bold'), bg="#F7CFD8").grid(row=1, column=0, sticky='news')
    tk.Label(checkout, text=f'Total drink price is {sumDrink:,.2f} Bath', font=('comic sans ms', 12, 'bold'), bg="#A6F1E0").grid(row=2, column=0, sticky='news')
    tk.Label(checkout, text=f'Total price of your order is {sumDrink + sumCake:,.2f} Bath', font=('comic sans ms', 16, 'bold'), bg="#D9EAFD").grid(row=3, column=0, sticky='news')



master = root()
left = tk.Frame(master, bg="#D9EAFD")
menu = tk.Frame(master, bg="#D9EAFD")
checkout = tk.Frame(master, bg="#FFFFFF")

# Sources
c1 = tk.PhotoImage(file="image\cake1.png")
c2 = tk.PhotoImage(file="image/cake2.png")
c3 = tk.PhotoImage(file="image/cake3.png")
d1 = tk.PhotoImage(file="image/drink1.png")
d2 = tk.PhotoImage(file="image/drink2.png")
d3 = tk.PhotoImage(file="image/drink3.png")
icon1 = tk.PhotoImage(file="image/cake-button.png")
icon2 = tk.PhotoImage(file="image/checkout.png")
icon3 = tk.PhotoImage(file="image/exit.png")


# list
cakemenu = [' Strawberry Cake \n'," Cheese   Cake  \n","Newyork Cheese Cake\n"]
drinkmenu = ['| Orange   Mixed |\n',' Lemonade Mixed \n',"| Mojito  Miexd  Berry |\n"]
price1 = [145, 120, 130]
price2 = [120, 100, 90]
cakeSpy = [tk.IntVar() for i in price1]
drinkSpy = [tk.IntVar() for i in price2]


layouts()
leftframe()
master.mainloop()