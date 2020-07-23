#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import locale
import encode
from tkinter import messagebox

'''
Handles the single hash key functionality
'''

class Frame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        #print(parent)
        
        # Define string variables for text entry fields
        self.toHash = tk.StringVar()
    
        self.Hashed = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Key to Hash:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.toHash).grid(
            column=1, row=0)


        ttk.Label(self, text="Result:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.Hashed,
                  state="readonly").grid(
            column=1, row=3)


        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Hash", command=self.calculate) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="About", command=self.bt) \
            .grid(column=1, row=0, padx=5)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=2, row=0)

    def calculate(self):
        s = self.toHash.get()
        self.Hashed.set(encode.Hash(s))
        #print(encode.Hash(s))

    def bt(self):
        msg = messagebox.showinfo("About", "Type a key and save it. You can copy the encoded hash for a password. When you need it again, enter your key here to get the password hash.")
        
#End of class

def main():
    root = tk.Tk()
    root.title("Hash")
    Frame(root)
    root.mainloop()

    
if __name__ == "__main__":
    main()
