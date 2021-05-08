from tkinter import *

root = Tk()
root.title('Прямовал')


def addFigure():
    fig = Toplevel()
    fig.title('Фигура')
    fig.resizable(0, 0)

    Label(fig, text='x1').grid(row=0, column=0, sticky=E)
    x1 = Entry(fig, width=3)
    x1.grid(row=0, column=1, pady=10, sticky=W)
    Label(fig, text='y1').grid(row=0, column=2, sticky=E)
    y1 = Entry(fig, width=3)
    y1.grid(row=0, column=3, sticky=W)

    Label(fig, text='x2').grid(row=1, column=0, sticky=E)
    x2 = Entry(fig, width=3)
    x2.grid(row=1, column=1, sticky=W)
    Label(fig, text='y2').grid(row=1, column=2, sticky=E)
    y2 = Entry(fig, width=3)
    y2.grid(row=1, column=3, sticky=W)

    Frame(fig, height=15).grid(row=2, column=0)

    v = IntVar()
    v.set(1)
    r1 = Radiobutton(fig, text='Прямоугольник', variable=v, value=1)
    r1.grid(row=3, column=0, columnspan=4, pady=10, padx=20)
    r2 = Radiobutton(fig, text='Овал', variable=v, value=0)
    r2.grid(row=4, column=0, columnspan=4, sticky=W, padx=20)

    def paint():
        x = int(x1.get())
        y = int(y1.get())
        xx = int(x2.get())
        yy = int(y2.get())
        if v.get() == 0:
            c.create_oval(x, y, xx, yy, width=2)
        elif v.get() == 1:
            c.create_rectangle(x, y, xx, yy, width=2)
        fig.destroy()

    button_draw = Button(fig, text='Нарисовать', command=paint)
    button_draw.grid(row=5, column=0, columnspan=4, pady=10)


c = Canvas(width=300, height=300, bg='white')
c.pack()
Button(text='Добавить фигуру', command=addFigure).pack()
root.mainloop()
