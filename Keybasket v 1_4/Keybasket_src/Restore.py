#!/usr/bin/env python3

import shutil
import os
import File
import Error_Handler
'''
This module performs a restore in case critical files are removed or damaged.
The 'Words' directory and its contents are deleted.
A new 'Words' directory is created and filed with backup files.
Run this module to perform a restore
'''


def restore():
    try:
        remove()
        create()
    except Exception:
        Error_Handler.Terminate("A Critical Error Has Occurred. Delete and Reinstall this Application", Error_Handler.RestoreFailureError, 7)

'''
Delete "Words"
'''

def remove():

    path = "Words"

    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))
        return 0
'''
Create new Directory with files
'''

def create():
    #Restores Dir
    path = "Words"
  
    try:  
        os.mkdir(path)  
    except OSError as error:  
        print(error)
        return 0

    #Loads files into dir
    File.changeFileExent("Backup/Sample.bin", False) #to txt

    s = ""
    #get content
    with open ("Backup/Sample.txt", "r") as f:
        s = f.read()
    f.close()

    File.changeFileExent("Backup/Sample.txt", True)  # to bin

    #Restore
    f = open("Words/Sample.txt", "w")
    f.write(s)

    f = open("Words/Files.txt", "w")
    f.write("Sample")
    f.close()

    #Finish up (Conversion)
    File.changeFileExent("Words/Sample.txt", True)  # to bin
    File.changeFileExent("Words/Files.txt", True)  # to bin

        

if (__name__ == "__main__"):
    s = input ("Would you like to restore Keybasket? Files will be deleted. y/n\n")
    if (s.lower() == "y" or s.lower() == "yes"):
        restore()
        print("\nKeybasket has been restored.")
    else:
        print ("\nOkay, Keybasket will not be restored.")
            
        

