#!/usr/bin/env python3

import os
import Error_Handler


'''
Performs various file manipulations
Produces an error for file not found
'''

#no errors here
def getEmptyFiles():
    L = Read("Words/Files.txt")
    L.remove("Sample")
    for i in L:
        #print("Words/" + i + ".txt")
        #print(L)
        if (not isEmpty("Words/" + i + ".txt")):
            L.remove(i)
        #print(L)
    return L

def allFileExChange(b):
    
    if os.path.exists("Words/Files.bin"):
        changeFileExent("Words/Files.bin", False)
        print("File Conversion Successful")
    try:    
        L = Read("Words/Files.txt") 
        L.append("Files")
    except FileNotFoundError:
        Error_Handler.Terminate("File Conversion Error", FileNotFoundError)
    if b:
        
        for i in L:
            i = "Words/" + i + ".txt"
            changeFileExent(i, b)
    else:
        for i in L:
            i = "Words/" + i + ".bin"
            changeFileExent(i, b)
        
            

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

        if (f == "Words/Files.txt"):
            raise Error_Handler.CriticalFileErasedError
            Error_Handler.HandleRestore(Error_Handler.CriticalFileErasedError, 5)
        else:
            Error_Handler.Terminate("File \"" + f + "\" Not Found", Error_Handler.FileNotFoundError, 2)

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
        Error_Handler.Terminate("File \"" + f + "\" Cannot be Read", IOError)

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

def isEmpty(f):
    FileNotFound(f)
    # open file in read mode
    with open(f, 'r') as read_obj:
        s = read_obj.read()
        s = s.strip()
        s = s.strip(" ")
    if (len(s) == 0):
            read_obj.close()
            return True

    read_obj.close()
    return False

def Remove(file):
        FileNotFound("Words/" + file)
        if (file == "Sample.txt" or file == "Files.txt"):
                print("The File Cannot Be Deleted. (not without crashing anyway)")
                return False

        if os.path.exists(("Words/" + file)):
                os.remove(("Words/" + file))
                print("File Deleted")

                #Update the files file
                L = Read("Words/Files.txt")
                name = file.split(".")
                L.remove(name[0])
                Write(L, "Words/Files.txt")
                return True

        else:
                print("The File\"" + file +  "\" Cannot be Found in the Current Directory")
                return False
def eraseFile(file):
        FileNotFound("Words/" + file)

        if (file == "Sample.txt" or file == "Files.txt"):
                print("The File Cannot Be Erased. (not without crashing anyway)")
                return False

        if os.path.exists(("Words/" + file)):
                with open (("Words/" + file), "w") as f:
                        f.write("")
                        print("The File is Now Empty")
                        f.close()
        else:
                print("The File \"" +file+ "\" Cannot Be Found")

#Cleans up every file (not optimized for files that are unchanged)
def totalClean():
     Data = Read("Words/Files.txt")
     for file in Data:
         d = Read("Words/" + file + ".txt")
         Write(cleanUp(d), "Words/" + file + ".txt")
         
    
#Ensures there is a file for every listed term in this file
def fileVerification():
    Data = Read("Words/Files.txt")

    for file in Data:
        if (not os.path.exists(("Words/" + file + ".txt"))):
            Data.remove(file)
            Write(cleanUp(Data), "Words/Files.txt")
    

def arrayContains(L, target):
        try:
                L.index(target) #if it can be found, no exception
                return True
        except ValueError:
                return False

def main(w):
        Write(cleanUp(Read(w)), w)

if (__name__ == "__main__"):
        main("Words/Sample.txt")


