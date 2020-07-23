#!/usr/bin/env python3
'''
This module generates usernames and passwords using keywords passed from a file.
There are over 10 different modes. The first 5 are great for usernames.
The rest are great for passwords

'''

import random
import File


def Generate(fName, mode = 1):
    List = File.Read(fName)

    if (mode == 0):
        return List[random.randint(0, len(List) - 1)]
    if (mode == 1):
        return List[random.randint(0, len(List) - 1)] + "_" + str(random.randint(0, len(List)))

    if (mode == 2):
        return concat(List, "")

    if (mode == 3):
        return concat(List, "-")

    if (mode == 4):
        return concat(List, "_")

    if (mode == 5):
        return (Generate(fName, 2) + str(random.randint(0, 1000)))
    if (mode == 6):
        return (Generate(fName, 2) + str(random.randint(0, 1000))).title()
    if (mode == 7):
        return (Generate(fName, 3) + str(random.randint(0, 1000)))
    if (mode == 8):
        return (Generate(fName, 3) + str(random.randint(0, 1000))).title()
    if (mode == 9):
        return (Generate(fName, 4) + str(random.randint(0, 1000)))
    if (mode == 10):
        return (Generate(fName, 4) + str(random.randint(0, 10000))).title()
    if (mode == 11):
        l = ["!", "$", "*", "|", "+", "=", ":", ";", "<", ">", "^"]
        return (Generate(fName, random.randint(2, 4)) + str(random.randint(0, 10000))).title() + l[random.randint(0, len(l) - 1)]
    #if (mode == 12):
     #   pass
        #This is where the "*" could be implemented




def concat(List, c):
        s = ""
        i = 2
        while (i > 0):
            q = random.randint(0, len(List) - 1)
            s += List[q]
            s+= c
            List.pop(q)
            i = i - 1
        return s.lower()

def main(fname):
    i = 50
    while (i > -1):
        #print(Generate(fname, random.randint(1, 11)))
        i = i - 1

if (__name__ == "__main__"):
    main("Words/Sample.txt")
