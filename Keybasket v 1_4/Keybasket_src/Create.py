#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import action
import Controller

'''
Handles Create window
'''

class Frame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        #print(parent)
        
        # Define string variables for text entry fields
        self.name = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="File Name (no extension):").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.name).grid(
            column=1, row=0)




        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Create", command=self.create) \
            .grid(column=0, row=0, padx=5)

        #ttk.Button(buttonFrame, text="About", command=self.bt) \
         #   .grid(column=1, row=0, padx=5)

        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=2, row=0)

    def create(self):
        #a bit of a bodge, but it works with a "loop" to get round these if bugs
        s = " "
        for i in s:
            i = action.makeFile(self.name.get())
            if (i == 0):
                self.invalidChar()
                continue
            if (i == 1):
                self.Blank()
                continue
            if (i == 2):
                self.Reserved()
                continue
            if (i == 3):
                self.Taken()
                continue
            else:
                self.complete(self.name.get())

    def makeWindow(self):
      root = tk.Tk()
      root.title("Create File")
      Frame(root)
      root.mainloop()
   
        
    def complete(self, s):
        msg = messagebox.showinfo("Complete", "A new file \"" + s + ".txt\" has been created. Please add terms")
        Controller.output(s)
        
    def Taken(self):
         msg = messagebox.showinfo("Taken", "File name is taken")

    def Blank(self):
         msg = messagebox.showinfo("Blank", "File name is blank")

    def Reserved(self):
        msg = messagebox.showinfo("Reserved", "The file name \"Files\" is reserved name. Please select another one.")

    def invalidChar(self):
        msg = messagebox.showinfo("Invalid Character", "An invalid character has been included in the file name. \n\nPlease do not include the following: space, tab, return, ! @ # $ % ^ & * ( ) ~ ` ? > < / , . : ; { } [ ] | \" ' - ")
        
#End of class

def main():
      root = tk.Tk()
      root.title("Create File")
      Frame(root)
      root.mainloop()
   

    
if __name__ == "__main__":
    main()
