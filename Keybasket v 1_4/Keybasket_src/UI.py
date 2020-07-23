#!/usr/bin/env python3
'''
UI for the shell, not used in GUI.
See Console_main
'''

import File
import encode
import action

def checkForFile(f):
	if File.CheckForFile(f):
		return f
	else:
		print("The Current File \"" + f +  "\" has been Deleted. Selected File is now \"Sample.txt\"")
		return "Sample.txt"

def menus(f):
    Stack = []
    Stack.append("main")

    while (Stack[len(Stack) - 1] == "main"):
        i = requestInput(0)
        if (i == 1):
            Stack.append("gen")
        if (i == 2):
            Stack.append("file")
        if (i == 3):
            return None
    while (Stack[len(Stack) - 1] == "gen"):
        i = requestInput(1)
        f = checkForFile(f)
        L = process(i, f, 1)
        printData(1, i, L)

        if (L == "None"):
            Stack.pop(1)
            menus(f)
    while (Stack[len(Stack) - 1] == "file"):
        i = requestInput(2)
        f = checkForFile(f)
        L = process(i, f, 2)
        printData(2, i, L)

        if (L == "None"):
            Stack.pop(1)
            menus(f)
        if (i == 1):
           f = subMenu(L)
           print("The File is Now \"" + f + "\"")


def printData(menu, ii, Data):
        if (not Data == None or Data == "None"):
                if  (menu == 1 and ii < 3):
                        for c in Data:
                                print(c)
		
                if (menu == 2 and ii == 2):
                        for c in Data:
                                print(c)

def subMenu(L):

    i = 0
    while (i < len(L)):

        if (len(L[i]) == 0 or not L[i].isalnum()):
            L.remove(L[i])
        i = i + 1

    q = 0
    while (q < len(L)):
        print(str(q + 1) + ". " + L[q])
        q = q + 1
    file = L[HandleIO(L, 1, input()) - 1] + ".txt"
    return file



def printMenu(L):
    q = 0
    for l in L:
        q += 1
        print(str(q) + ".", l)
    qq = input()
    return HandleIO(L, -1, qq)

def requestInput(menu):
    MultiList = [["Generate", "Manage Files", "Quit" ], ["Generate Username", "Generate Password", "Hash Key", "Two Key Hash", "Main Menu"], ["Select File", "Show File Contents", "Add to File", "Remove from File", "Create File", "Delete File", "Erase File Contents", "Main Menu"], []]

    if(menu == 0):
        print("\n-Main Menu-")
    if (menu == 1):
        print("\n-Generate-")
    if (menu == 2):
        print("\n-File Management-")

    return printMenu(MultiList[menu])

def process(inputt, f, menuu):

    if (menuu == 1):
        if (inputt == 1):
            print("Current File " + "\"" + f + "\"")
            return action.genName(f)
        if (inputt == 2):
            print("Current File " + "\"" + f + "\"")
            return action.genPwd(f)
        if (inputt == 3):
            key = input("Give Text Key to Encrypt\n")
            print("Encoded \"" + key + "\" as\n" + encode.Hash(key))
            print("\nYour key has been encoded. You can copy the encoded string for a password. When you need it again, enter your key here to get the password")

        if (inputt == 4):
            key = input("Enter Key 1\n")
            key2 = input("Enter Key 2\n")
            print("Encoded \"" + key + "\" as\n" + encode.Hash(key, key2))
            print("\nYour key has been encoded. You can copy the encoded string for a password. When you need it again, enter Key 1 and Key 2 here to get the password")

        if (inputt == 5):
            return "None"

    if (menuu == 2):
        if (inputt == 1):
            return File.Read("Words/Files.txt")
        if (inputt == 2):
            print("Current File " + "\"" + f + "\"")
            return action.showContents(f)
        if (inputt == 3):
            print("Current File " + "\"" + f + "\"")
            action.addTerms(f)
        if (inputt == 4):
            print("Current File " + "\"" + f + "\"")
            action.removeTerm(f)
        if (inputt == 5):
            action.makeFile()
        if (inputt == 6):
            print("Current File " + "\"" + f + "\"")
            c = input("Would you like to delete " + f + "? (y/n)\n")
            c = c.strip()
            if (c.lower() == "y" or c.lower() == "yes"):
                File.Remove(f)

            else:
                print("Okay, the File will Stay")
        if (inputt == 7):
            print("Current File " + "\"" + f + "\"")
            c = input("Would you like to empty " + f + "? (y/n)\n")
            c = c.strip()
            if (c.lower() == "y" or c.lower() == "yes"):
                File.eraseFile(f)
            else:
                print("Okay,The File will not be Erased.")
        if (inputt == 8):
            return "None"

    else:
        return None

def HandleIO(L, f, inputt):
    try:
        ii = int(inputt)
        if ((-1 < ii <= len(L))):
            return ii
        else:
            print("Select an available number")
            return f
    except Exception:
        print("Please Type a Number")
        return f
