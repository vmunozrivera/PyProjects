# TK Radio Button GUI
# TKinter radio button sample GUI

import tkinter
from tkinter import ttk


def select_option():
    monitor.config(text="{}".format(opt_var.get()))


def reset():
    monitor.config(text="")


root = tkinter.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

opt_var = tkinter.StringVar()

r1 = ttk.Radiobutton(root, text="Option 1", variable=opt_var,
                     value='option_1', command=select_option)

r2 = ttk.Radiobutton(root, text="Option 2", variable=opt_var,
                     value='option_2', command=select_option)

r3 = ttk.Radiobutton(root, text="Option 3", variable=opt_var,
                     value='option_3', command=select_option)

r4 = ttk.Radiobutton(root, text="Option 4", variable=opt_var,
                     value='option_4', command=select_option)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
r4.grid(column=0, row=4, padx=5, pady=5)

monitor = ttk.Label(root)
monitor.grid(column=0, row=5, padx=5, pady=5)

btn_reset = ttk.Button(root, text="Reset", command=reset)
btn_reset.grid(column=0, row=6, padx=5, pady=5)

root.mainloop()
