from tkinter import*


def Final():
        ex1 = [float(i) for i in entryEx1.get().split()]
        ex2 = [float(i) for i in entryEx2.get().split()]
        ex3 = [float(i) for i in entryEx3.get().split()]
        val = [float(i) for i in entryValue.get().split()]
        usd = sum([v / ex for ex, v in zip(ex1, val)])
        eur = sum([v / ex for ex, v in zip(ex2, val)])
        grb =sum([v / ex for ex, v in zip(ex3, val)])
        usd = round(usd, 2)
        eur = round(eur, 2)
        grb = round(grb, 2)
        entryFV1.delete(0, END)
        entryFV1.insert(0, str(usd))
        entryFV2.delete(0, END)
        entryFV2.insert(0, str(eur))
        entryFV3.delete(0, END)
        entryFV3.insert(0, str(grb))


root = Tk()
root.title("Торгівельна база")
root.geometry('500x200')

labValue = Label(text = "Ціна товару в гривнях:")
labExchange = Label(text = "Курс валют:")
labFinValue = Label(text = "Ціна товару:")
labEx1 = Label(text = "USD/UAH")
labEx2 = Label(text = "EUR/UAH")
labEx3 = Label(text = "GBR/UAH")
labFV1 = Label(text = "USD")
labFV2 = Label(text = "EUR")
labFV3 = Label(text = "GBR")

entryValue = Entry(width = 15)
entryEx1 = Entry(width = 15)
entryEx2 = Entry(width = 15)
entryEx3 = Entry(width = 15)
entryFV1 = Entry(width = 15)
entryFV2 = Entry(width = 15)
entryFV3 = Entry(width = 15)

butReverse = Button(text = "Перевести", width = 8, height = 3, command = Final)

labValue.place(relx = 0.2, rely = 0.2)
labExchange.place(relx = 0.1, rely = 0.4)
labFinValue.place(relx = 0.6, rely = 0.4)
labEx1.place(relx = 0, rely = 0.5)
labEx2.place(relx = 0, rely = 0.6)
labEx3.place(relx = 0, rely = 0.7)
labFV1.place(relx = 0.5, rely = 0.5)
labFV2.place(relx = 0.5, rely = 0.6)
labFV3.place(relx = 0.5, rely = 0.7)

entryValue.place(relx = 0.47, rely = 0.2)
entryEx1.place(relx = 0.12, rely = 0.5)
entryEx2.place(relx = 0.12, rely = 0.6)
entryEx3.place(relx = 0.12, rely = 0.7)
entryFV1.place(relx = 0.57, rely = 0.5)
entryFV2.place(relx = 0.57, rely = 0.6)
entryFV3.place(relx = 0.57, rely = 0.7)

butReverse.place(relx = 0.32, rely = 0.5)

root.mainloop()