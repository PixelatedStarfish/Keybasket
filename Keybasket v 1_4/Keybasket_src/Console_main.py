#!/usr/bin/env python3
'''

@author Andrew Vella

This runs an earlier version of the program. However, it no longer functions properly for the sake of running the GUI.
It is here for the sake of complete documentation.
'''

import File
import UI



def startup():

   try:
      File.allFileExChange(False) #False means convert to text, True for convert to bin
   except FileNotFoundError:
      print("v2b_bin: Files cannot be edited unless program is running\n\n")
   
   File.fileVerification()

   print("-Keybasket in Shell-\n\nIf you cannot come up with one more variation of your pet's name and childhood home with a dollar sign, then why would you?")
   print("This program takes a pool of familiar words and stitches them together. Try it out with the sample or create a personal file of your own.")
   print("You can also hash out extra-tough passwords (just keep your keywords short and on hand). Next time you need it, run the keywords through here.")
   print("Give it a try! No web plug-ins or master passwords needed!")
   print("\n-Program Created by Andrew Vella-")

def closeDown():
   File.fileVerification()
   File.totalClean()

   #Rather than asking about what the user wants to do every time or storing a single boolean in a file.
   #I have placed a hard-coded value here. Set to True for bin and False for text
   ConvertToBin = True
   if ConvertToBin:
      File.allFileExChange(True)
      print("Files Converted")

def main():
   f = "Sample.txt"
   UI.menus(f)


if (__name__ == "__main__"):
   startup()
   main()
   closeDown()
   print("-End of Session-")


