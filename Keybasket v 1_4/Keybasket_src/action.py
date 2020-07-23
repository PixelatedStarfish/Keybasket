#!/usr/bin/env python3
'''
Performs various actions for windows or commands as needed
'''

import File
import gen
import random
def genName(f):
    if (File.isEmpty("Words/" + f)):
        Ll = ["File is Empty"]
        return Ll
    c = 1
    q = 2
    textList = []
    textList.append("Names:\n")
    while c < 56:
        textList.append(gen.Generate("Words/" + f, q))
        c += 1
        q += 1

        if (q == 6):
            q = 1
    return textList
def genPwd(f):
    if (File.isEmpty("Words/" + f)):
        Ll = ["File is Empty"]
        return Ll

    c = 1
    q = 2
    textList = []
    textList.append("Passwords:\n")
    while c < 56:
        textList.append(gen.Generate("Words/" + f, (q + 6)))
        c = c + 1
        q = q + 1
        if (q == 6):
            q = 1
    return textList
def showContents(f):
    if (File.isEmpty("Words/" + f)):
        Ll = ["File is Empty"]
        return Ll

    if (not f == "Sample.txt"): 
        return File.Read("Words/" + f)
    else:
        print("Sample Contents Not Shown. Select another File")
        return "None"
def InvChars(s):
    Inv = "!@#$%^&*()~`?></,.:;{}[]|\"'-\n\t "
    Vv = False
    for c in Inv:
        if (s.count(c) > 0):
            Vv = True
    return Vv

def removeTerm(f):
    if (File.isEmpty("Words/" + f)):
        Ll = ["File is Empty"]
        return Ll

    showContents(f)
    t = input("Term to Remove?\n")
    l = File.Read("Words/" + f)
    ll = len(l)
    for i in l:
        if (t == i):
            l.remove(i)
            print("Term Removed")
    if (ll == len(l)):
        print("No term removed")


    File.Write(l, ("Words/" + f))
    File.main("Words/" + f)

def addTerms(file): #keep adding until a term is empty

    print("To stop adding terms, enter a blank term")

    L = []
    i = 0
    while (True):
        q = input("Term " + str(i + 1) + "\n")
        if (not q.isspace() and len(q) > 0):
            L.append(q)
            print("Added \"" + q + "\"\n")
            i = i + 1
            q = ""
        else:
            print("This term is blank. No more terms will be added.")
            break

        File.Write(L, ("Words/" + file), File.isEmpty("Words/" + file))  # False = appendMode
        File.main("Words/" + file)

def makeFile(s):

#Underscores are allowed, remember that!
    if (InvChars(s)):
        return 0
    if (s.isspace() or len(s) == 0):
        return 1
    if (s == "Files"):
        return 2



    #Set up to Update the Files File
    L = File.Read("Words/Files.txt")

    #Check if the name is available
    for i in L:
        if s == i:
            print("Three")
            return 3


    L.append(s)

   #Delete blanks
    i = 0
    while i < len(L):
        if (L[i].isspace()):
            L.remove(i)
        i = i + 1
    #Update
    File.Write(File.cleanUp(L), "Words/Files.txt")




    #Write file
    File.Write("", "Words/" + s + ".txt")
    print("The File " + (s + ".txt") + " has been Created. Please Add Terms")
