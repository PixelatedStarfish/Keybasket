#!/usr/bin/env python3
import File
import secrets
import math

'''
This is where all the hashing happens for the hahing windows or commands

Keys are sorted hashed, sorted, and hashed.
For the one key hash, key2 is default key.

To make the hash each character in key2 is altered (added) by the first char in key1
This new key is then mutated via the second char in key 1 and so on...
Then all the chars in the sequence are stuck together

The final hash is 72 chars
Keys are sorted so that similar keys do not collide
If the second key is not secure it will be replaced.

'''
def Hash(key1, key2 = "mgR\>gE,o"):
        h1, k = encodeStr(key1, key2)
        h2 = encodeStr(key2, h1)[0]
        h3 = encodeStr(h1, h2)[0]   
        return h3, k

def sortAndReverseString(s):
    L = []
    ss = ""
    for i in s:
        L.append(i)
    L.sort()

    if (s[0] < s[1]):
        L.reverse()

    for i in L:
        ss += i
    return ss

def LenWithNoRepeatChars(s):
    L = []
    for i in s:
        L.append(i)
        q = File.cleanUp(L)
    return len(q)

def encodeStr(key1, antiKey = "ZN?d<f\Y3", sortAndReverse = True, Random = False, n = 81):
    #len of hash = 72

    chars = GeneratePrintableCharacters()


    #no empty keys
    if (len(key1) == 0):
        key1 = "otY)\`)+9"
    if (len(antiKey) == 0 or LenWithNoRepeatChars(antiKey) < 8):
        key2 = genRandomCharsStr(chars, int(math.sqrt(n)))
    else:
        key2 = antiKey

    if (sortAndReverse):
        ss = sortAndReverseString(formatString(key1, int(math.sqrt(n))))
    else:
        ss = formatString(key1, int(math.sqrt(n)))

    if Random:
        c =  genRandomCharsStr(chars, int(math.sqrt(n)))
    else:
        c = formatString(key2, int(math.sqrt(n)))
    L = produceEncryptSeq(ss, c, chars)

    r = ""
    for i in L:
        r += i

    return r, key2

def formatString(s, nn):
    while len(s) < nn:
        s = s + s

    concat = ""

    i = 0

    while i < nn:
        concat += s[i]
        i += 1   #it was i = i + 1, but I would like for the whole stingto to be relavant (Actually 9 chars is enough)

    return concat

def genRandomCharsStr(chars, nn):
    s = ""
    i = 0
    while i < nn:
        s += chars[secrets.randbelow(len(chars) - 1)] #picks a char off the ASCII table that is printable
        i = i + 1
    return s

def produceEncryptSeq(toEncrypt, Key2, chars):
    L = []
    r = Key2
    charArray = []

    for i in r:
        charArray.append(i)

    for c in toEncrypt:
        se = ""
        i = 0
        while i < len(charArray):
            #print(i)
            se += charArray[i]
            q = chr(ord(charArray[i]) + ord(c))

            charArray[i] = chars[((ord(q) + ord(Key2[0])) % (len(chars) - 1))]

            i = i + 1
        L.append(se)
        L[0] = ""


    return L

def GeneratePrintableCharacters(): #Generates all ASCII chars that will appear in the console
    s = ""

    i = 33
    while i < ord('~') + 1:
        if (chr(i).isascii()  and chr(i).isprintable and (not chr(i).isspace())):
            s += chr(i)
        i = i + 1
    return s




def main():
    print(Hash("Sophie"))
    GeneratePrintableCharacters()



if (__name__ == "__main__"):
    main()
#32-126 are valid chars
