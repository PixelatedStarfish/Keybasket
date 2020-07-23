#!/usr/bin/env python3


import tkinter as tk
from tkinter import ttk
import locale
from tkinter import messagebox
import ScrollText
import HashKey
import TwoKeyHash
import File
import Controller

'''
This is the class that creates menus.
'''

class Frame(ttk.Frame):
    def __init__(self, parent, L, pad = 70):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.pad = pad
        self.makeButtons(L)
        self.pack()
    
    def makeButtons(self, sArr):
        # Create a frame to store the buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=1, columnspan=2, sticky=tk.E)

        # Add buttons to the button frame
        c = -1
        mainPad = self.pad
        for i in sArr: #Lamdba funcs only take constants correctly...
            c = c + 1
            if ( i == "Generate"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Generate")) \
                    .grid(column=0, row=c, padx= mainPad)
                continue
            if ( i == "Access Files"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Access Files")) \
                    .grid(column=0, row=c, padx= mainPad)
                continue
            if ( i == "About"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("About")) \
                    .grid(column=0, row=c, padx= mainPad)
                continue
            if ( i == "Generate Account Names"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Generate Account Names")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if ( i == "Generate Passwords"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Generate Passwords")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue

            if ( i == "Hash Key"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Hash Key")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if ( i == "Two Key Hash"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Two Key Hash")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if ( i == "Select File"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Select File")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if (i == "Create File"):
                ttk.Button(buttonFrame, text=i, command=lambda: self.output("Create File")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if (i == "Update File"):
                ttk.Button(buttonFrame, text=i, command=lambda: self.output("Update File")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if ( i == "Main Menu"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Main Menu")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue
            if ( i == "Quit"):
                ttk.Button(buttonFrame, text= i, command = lambda: self.output("Quit")) \
                    .grid(column=0, row=c, padx=mainPad)
                continue


            else:
                ttk.Button(buttonFrame, text=i, command=self.bt) \
                    .grid(column=0, row=c, padx=5)
    def output(self, i):
        self.parent.withdraw()
        Controller.output(i)
        self.parent.destroy()

    def bt(self):
        msg = messagebox.showinfo("About", "Generic Message")
        
#End of class

def main():
    root = tk.Tk()
    root.title("Two Key Hash")
    root.geometry("480x360")
    frame = Frame(root, ["Option1", "Option2"])
    frame.pack(fill = tk.BOTH, expand = True)
    root.mainloop()

    
if __name__ == "__main__":
    main()
