# TK To Do list GUI
# TKinter selectable list sample GUI

import tkinter
from tkinter import ttk


root = tkinter.Tk()

fruit_list = ["Apple", "PineApple", "Banana", "Orange", "Lime"]
item = tkinter.StringVar(value=fruit_list)
listbox = tkinter.Listbox(root, height=15, listvariable=item)
listbox.grid(column=0, row=2, sticky=tkinter.W)

label = tkinter.Label(text="Fruit Juices List")
label.grid(column=0, row=0, sticky=tkinter.W)

root.mainloop()