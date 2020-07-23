#!/usr/bin/env python3

import tkinter as tkin
from tkinter import ttk
from tkinter import *
import action

'''
Handles scrollable windows without additional widgets
'''
class Scrollable():
    def __init__(self, printable, title, label = "Generic Label" , geo = "300x300+0+0", showlabel = True):

        root = tkin.Tk()
        self.printable = printable
        self.title = title
        self.label = label
        self.geo = geo
        self.showlabel = showlabel



        root.geometry(self.geo)
        root.resizable(True, True)
        root.title(self.title)
        frame = ttk.Frame(root, padding="10 10 10 10")
        frame.pack(fill=tkin.BOTH, expand=True)

        self.textbox = Text(root)
        self.textbox.config(wrap = WORD)
        self.textbox.state = DISABLED

        if (self.showlabel):
            lab = ttk.Label(frame, text=self.label)
            lab.pack()


        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill = Y)
        self.textbox.pack()

        self.textbox.configure(font=("Courier", 16))
        self.textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textbox.yview)

        L = self.printable
        for i in L:
            self.textbox.insert(END, (i + "\n"))


        root.mainloop()


def userNames(file):
    s = Scrollable(action.genName(file), "Names", "File: " + file)
    
def passwords(file):
    s = Scrollable(action.genPwd(file), "Names", "File: " + file)

def main():
    passwords("Sample.txt")

if (__name__ == "__main__"):    
    main()
    
