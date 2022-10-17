from tkinter import*
def title_1():
    global entry_title
    t = entry_title.get()
    root.title(t)
def font_1():
    fo = entry_font.get()
    entry_title.config(font = f'Arial {fo}')
    entry_font.config(font = f'Arial {fo}')
def purple():
    if color.get()==1 and color.get()!=0:
        root.configure(bg = 'purple')
def yellow():
    if color.get()==3 and color.get()!=0:
        root.configure(bg = 'yellow')
def black():
    if color.get()==2 and color.get()!=0:
        root.configure(bg = 'black')
def red():
    if color.get()==4 and color.get()!=0:
        root.configure(bg = 'red')
root = Tk()
lab_title = Label(text = 'Заголовок:', font = ('Sans-serif 12'))
lab_title.place(x=200,y=100)
entry_title = Entry()
entry_title.place(x=300,y=105)
lab_font = Label(text = 'Розмір шрифта:', font = ('Sans-serif 12'))
lab_font.place(x=200,y=200)
entry_font = Entry()
entry_font.place(x=330,y=205)
color = IntVar()
choice1 = Radiobutton(text = 'Фіолетовий',variable = color, value=1)
choice1.place(x=200,y=250)
choice2 = Radiobutton(text = 'Чорний',variable = color, value=2)
choice2.place(x=200,y=280)
choice3 = Radiobutton(text = 'Жовтий',variable = color, value=3)
choice3.place(x=200,y=310)
choice4 = Radiobutton(text = 'Червоний',variable = color, value=4)
choice4.place(x=200,y=340)
but_click = Button(text = 'Тицяй!', width = 16, height = 3, command=lambda:[title_1(), purple(), yellow(), black(), red(), font_1()])
but_click.place(x=300,y=380)
root.title('Тут покищо нічого :(')
root.geometry('1000x600')
root.mainloop()
