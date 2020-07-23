#!/usr/bin/env python3

import os

'''
Run this file to clean up the sample backup
'''



'''
Switches between txt and bin files
'''
def changeFileExent(file, b):

    if b:
        base = os.path.splitext(file)[0]
        os.rename(file, base + ".bin")
    else:
        base = os.path.splitext(file)[0]
        os.rename(file, base + ".txt")
    
def CheckForFile(f):
    try:
        with open("Words/" + f, "r") as File:
            File.close()
        return True

    except FileNotFoundError as fnf:
        #print("Words/" + f)
        return False


def FileNotFound(f):

    try:
        with open(f, "r") as File:
            File.close()

    except FileNotFoundError:
        print("File not found")

def Read(InputFile):
    FileNotFound(InputFile)

    try:
                with open(InputFile, "r") as File:
                        f = File.read().split("\n")
                        for i in f:
                            if (len(i) == 0 or i.isspace()):
                                f.remove(i)
                        return f
    except (Exception):
        print("File Read Error")

def Write(L, n, WriteMode = True): #defaults to writeMode

        s = ""
        i = -1
        while (i < len(L) - 1):
                i = i+1
                s += (str(L[i]) + "\n")
        if (WriteMode):
                f = open(n, "w") #overwrites
        else:
                f = open(n, "a") #appends
        f.write(s)
        f.close()

def cleanUp(L): #sorts and removes duplicates
        ls = sorted(L)
        l = []

        i = 0
        while (i < len(ls)):
                if (not arrayContains(l, ls[i])):
                        l.append(ls[i])
                i = i + 1
        return l


def arrayContains(L, target):
    try:
        L.index(target)  # if it can be found, no exception
        return True
    except ValueError:
        return False


def main(w):
        changeFileExent(w, False)
        Write(cleanUp(Read(w)), w)
        changeFileExent(w, True)

if (__name__ == "__main__"):
    try:
        main("Sample.bin")
    except FileNotFoundError:
        main("Sample.txt")
    except FileNotFoundError:
        print("Please stop goofing around in here.")



