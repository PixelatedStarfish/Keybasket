#!/usr/bin/env python3

import ScrollText
import Create
import HashKey
import Select
import TwoKeyHash
import Menus
import Mod2
import File
import action
import tkinter
from tkinter import messagebox

'''
This manages the windows of the application by reading and writing to a file called "Output.txt"
Each window has a function to call it.
'''
file = "Sample.txt"
mainTitle = "Keybasket Account Generator"


def main():
    window = ""
    while (not window == 0 or window == 1):
        menu(["Generate", "Access Files", "About", "Quit"], mainTitle)
        window = processMenu(File.Read("Output.txt"))
    if (window == 1):
        menu(["Generate", "Access Files", "About", "Quit"], mainTitle)
        window = processMenu(File.Read("Output.txt"))

def processCreate(L):
    #if the file does not exist, create it
    if (not action.makeFile(L[0]) == 3):
        f = open("Words/" + L[0] + ".txt", "w")
        f.close()

def processSelect(L):
    global file
    file = L[0] + ".txt"

def processMenu(L):
    try:
        #Load the next menu based on the selected choice
        if (L[0] == "Generate"):
            menu(["Generate Account Names", "Generate Passwords", "Hash Key", "Two Key Hash", "Main Menu"], "Generate", 80)
            window = processMenu(File.Read("Output.txt"))
        if (L[0] == "Access Files"):
            menu(["Select File", "Create File", "Update File", "Main Menu"], "Files", -20)
            window = processMenu(File.Read("Output.txt"))

        if (L[0] == "Generate Account Names"):
            genName(file)

        if (L[0] == "Generate Passwords"):
            genPwd(file)

        if (L[0] == "Hash Key"):
            hash()

        if (L[0] == "Two Key Hash"):
            twoKeyHash()
        if (L[0] == "Select File"):
            select()
            processSelect(File.Read("Output.txt"))

        if (L[0] == "Create File"):
            create()
            processCreate(File.Read("Output.txt"))

        if (L[0] == "Update File"):
            modify()
        if (L[0] == "About"):
            s = ""
            with open("Messages/about.txt", "r") as a:
                s = a.readlines() #a.read() for messagebox, a.readlines() for scrollable
            with open("Messages/readme.txt", "r") as r:
                s += r.readlines()

                ScrollText.Scrollable(s, "Info", "Readme for Keybasket 1.4.1","850x320+0+0", False)
                a.close()
                r.close()



        if (L[0] == "Main Menu"):
            return 1

        if (L[0] == "Quit"):
            return 0
    except IndexError:
        pass


def menu(L, title, xcons = 0):
    root = rooter(title)
    root.protocol("WM_DELETE_WINDOW", Xprot())

    x = 270 + xcons
    y = 28 * len(L)

    root.geometry(str(x) + "x" + str(y))
    Menus.Frame(root, L).mainloop()

def hash():
    root = rooter("Hash")
    root.geometry("350x110+0+0")
    HashKey.Frame(root).mainloop()

def twoKeyHash():
    root = rooter("Two Key Hash")
    root.geometry("320x140+0+0")
    TwoKeyHash.Frame(root).mainloop()

def genName(file):
    ScrollText.Scrollable(action.genName(file),"Names" , "- " +  file.split(".")[0] + " -")

def genPwd(file):
    ScrollText.Scrollable(action.genPwd(file), "Passwords" , "- " +  file.split(".")[0] + " -")

def select():
    root = rooter("Select", False)
    root.geometry("430x180+0+0")
    Select.Frame(root, File.Read("Words/Files.txt"), "Select").mainloop()

    #Clears ups the output file to avoid bugs with Create/Select


    global file
    with open("Output.txt", "r") as f:
        if ( f.read().count(" ") > 0):
            with open("Output.txt", "w") as f:
                f.write(file.split(".")[0])
    f.close()


def create():
    root = rooter("Create", False)
    root.geometry("430x75+0+0")
    Create.Frame(root).mainloop()

    #Clears ups the output file to avoid bugs with Create/Select
    global file
    with open("Output.txt", "r") as f:
        if (f.read().count(" ") > 0):
            with open("Output.txt", "w") as f:
                f.write(file.split(".")[0])
    f.close()


def modify():
    print(file)
    if (file == "Sample.txt" or file == "Files.txt"):
        root = tkinter.Tk()
        root.geometry("0x0")
        root.withdraw
        msg = messagebox.showinfo("Operation Denied", "The selected file cannot be modified, please select another.")
        root.destroy()
    else:
        root = tkinter.Tk()
        root.title("Update")
        root.geometry("210x170+0+0")
        Mod2.Frame(root, action.showContents(file), "Update" , "With: \"" + file + "\"", file).mainloop()

def outputList(i):
    List = i
    File.Write(List, "Output.txt")

def output(i):
        List = [i]
        File.Write(List, "Output.txt")

def rooter(title, img = True):
    root = tkinter.Tk()
    root.withdraw
    root.title(title)
    root.resizable(False, False)
    root.geometry("350x110+0+0")

    if (img):
        root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file="Images/icon.gif"))

    root.deiconify
    return root

def Xprot():
    s = ""
    with open ("Output.txt", 'r') as f:
        s = f.read()
    f.close()

    with open ("Output.txt", "w") as f:
        if (not s == ""):
            f.write("")
        else:
            f.write("Quit")
    f.close()

if (__name__ == "__main__"):
    main()
