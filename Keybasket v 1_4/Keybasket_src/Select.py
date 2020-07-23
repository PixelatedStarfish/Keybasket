#!/usr/bin/env python3

import tkinter as tk
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import action
import File
import Controller

'''
A class that handles the "Select" Window
'''

class Frame(ttk.Frame):
    def __init__(self, parent, printable, title):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        # Define string variables for text entry fields
        self.name = tk.StringVar()

        frame = ttk.Frame(parent, width = 10, height = 100, padding="10 10 10 10")
        frame.pack_propagate(0)
        frame.pack(fill=tk.X, expand=False)

        self.printable = printable
        self.title = title
        self.textbox = Text(frame)
        self.textbox.state = DISABLED



        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill = Y)
        self.textbox.pack()

        #right now the size of the text box varies based on text size, so it will stay at 12 until that is sorted out
        self.textbox.configure(font=("Courier", 16))

        self.textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textbox.yview)

        L = self.printable
        for i in L:
            self.textbox.insert(END, (i + "\n"))
        

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="File Name (no extension):").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.name).grid(
            column=1, row=0)

        self.makeButtons(self.name)
        


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
        self.pack()

    def makeButtons(self, name):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Select", command= lambda:  self.slec(name)) \
            .grid(column=0, row=0, padx=5)


        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=2, row=0)


    def slec(self, name):
        i = action.makeFile(self.name.get())



        if (i == 0):
            self.invalidChar()
            return None

        if (i == 1):
            self.Blank()
            return None

        if (i == 2):
            self.Reserved()
            return None

        if (i == 3 and File.arrayContains(File.Read("Words/Files.txt"), self.name.get())):
            self.Selected(name)
            return None
        else:
            self.NotFound(name)
            self.textbox.delete("1.0", END)
            self.printable = File.Read("Words/Files.txt")
        for i in self.printable:
            self.textbox.insert(END, (i + "\n"))

    def makeWindow(self):
      root = tk.Tk()
      root.title("Create File")
      Frame(root)
      root.mainloop()

        
    def Selected(self, name):
         msg = messagebox.showinfo("Selected", "File Selected")
         Controller.output(name.get())

    def Blank(self):
         msg = messagebox.showinfo("Blank", "File name is blank")

    def invalidChar(self):
        msg = messagebox.showinfo("Invalid Character", "An invalid character has been included in the file name. \n\nPlease do not include the following: space, tab, return, ! @ # $ % ^ & * ( ) ~ ` ? > < / , . : ; { } [ ] | \" ' - ")
    
    def NotFound(self, name):
        msg = messagebox.showinfo("Created", "This file is not listed, so it has been created")
        Controller.output(name.get())
    def Reserved(self):
        msg = messagebox.showinfo("Reserved", "The file name \"Files\" is reserved name. Please select another one.")

        
#End of class

def main():
      root = tk.Tk()
      root.title("Select File")
      Frame(root, File.Read("Words/Files.txt"), "Select")
      root.geometry("440x200")
      root.title("Select")
      root.mainloop()
   

    
if __name__ == "__main__":
    main()
