from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def del_text():
    answer = mb.askokcancel('Удаление текста',
                            'Реально удалить?')
    if answer:
        text.delete(1.0, END)


def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
    except (FileNotFoundError, TypeError):
        mb.showinfo("Открытие файла",
                    "Файл не выбран!")
    else:
        s = f.read()
        text.insert(1.0, s)
        f.close()


def extract_text():
    file_name = fd.asksaveasfilename()
    try:
        f = open(file_name, 'w')
    except (FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла",
                    "Файл не сохранен!")
    else:
        s = text.get(1.0, END)
        f.write(s)
        f.close()


root = Tk()
b3 = Button(text="Очистить", command=del_text)
b3.grid(column=1, sticky=E)
text = Text(width=50, height=25)
text.grid(row=1, columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=2, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=2, column=1, sticky=W)
root.mainloop()
