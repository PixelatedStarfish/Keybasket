#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import ttk
import File

'''
This is the class that handles file modification and updating for the user.
'''


class Frame(ttk.Frame):
    def __init__(self, parent, printable, title, label, file):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        print(parent)

        frame = ttk.Frame(parent, width=10, height=100, padding="10 10 10 10")
        frame.pack_propagate(0)
        frame.pack(fill=tk.X, expand=False)

        self.printable = printable
        self.title = title
        self.label = label
        self.file = file
        self.textbox = Text(frame)
        self.textbox.state = NORMAL



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
            self.makeButtons()

        ttk.Label(self, text= "- " + self.file.split(".")[0] + " -").grid(
            column=0, row=0, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
        self.pack()

    def makeButtons(self):

        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Update", command= lambda:  self.update()) \
            .grid(column=0, row=0, padx=5)

        ttk.Button(buttonFrame, text="Exit", command = lambda: self.parent.destroy()) \
            .grid(column=2, row=0)

    def update(self):
        # get strings
        L = []
        String = ""
        for i in self.textbox.get("1.0", END):
            String += i
        L = String.split("\n")
        # remove redundant newlines
        for i in L:
            if (len(i.strip("\n")) == 0):
                L.remove(i)
        # update file and textbox
        self.textbox.delete("1.0", END)
        File.Write(File.cleanUp(L), "Words/" + self.file)
        self.printable = File.Read("Words/" + self.file)
        for i in self.printable:
            self.textbox.insert(END, (i + "\n"))

    def makeWindow(self):
      root = tk.Tk()
      root.title("Create File")
      Frame(root)
      root.mainloop()

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
