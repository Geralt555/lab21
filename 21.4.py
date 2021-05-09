#!/usr/bin/env python3
# -*- config: utf-8 -*-

# за рамками данного курса было оставлено несколько классов пакета
# tkinter . Среди них PhotoImage , позволяющий использовать в программе внешние
# изображения форматов GIF и PGM. Экземпляры PhotoImage можно размещать на
# различных виджетах через опцию image .

from tkinter import *
from random import random


def move():
    b.place(relx=random(), rely=random())


root = Tk()
root['bg'] = 'white'
root.geometry('300x200')
img = PhotoImage(file='smile.gif')
b = Button(image=img, command=move)
b.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
