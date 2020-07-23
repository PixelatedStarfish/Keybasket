#!/usr/bin/env python3

'''
Keybasket source code in python3
@author Andrew Vella

I would like to cite Murach's Python Programming by Joe Murach and Micheal Urban
The textbook was a great start for the GUI. The Hash windows were based on the Future Value Calculator program.

This is the main module for the GUI, including startup and close down procedures

It will run from the shell, but you have to ask it nicely.
That is you have to run python from within "Keybasket_src" or you get ErrCode 7 (Failed Restore)
Automator seems to have a little trouble with _tkinter, it throws an error inside tkinter.

Copyright 2020 Andrew Jones Vella
MIT License
'''

import File
import os
import Controller
import Error_Handler
import Restore

#So for a stand-alone app a setup mode is needed to create the Words directory and populate it
'''
startup() converts files form bin to txt, creates an output file, and marks any empty files.
If a marked file is empty during closedown() it will be deleted.
Various exceptions are handled accordingly.
'''
def startup():
   print("Keybasket v 1.4.2 \nCreated by Andrew Vella\nCopyright 2020\nMIT License\n\n")

   #If a set up is needed
   if not os.path.isdir("Words"):
      Restore.create()

   try:
      File.allFileExChange(False) #False means convert to text, True for convert to bin
   except FileNotFoundError:
      pass

   
   File.fileVerification()

   #make output file
   f = open("Output.txt", "w")

   try:
     r = File.getEmptyFiles()
     return r

   except ValueError:
      raise Error_Handler.FileReferenceError

'''
closedown() deletes files that were marked for deletion, verifies that each file present has a reference in Files.txt, and cleans up each file.
It alphabetizes the contents of each file and removes duplicate info.
It will print a message if there is an exception.
'''
def closeDown(L):

   #Delete all files that were empty at the start and end of the program
   R = File.getEmptyFiles()

   for i in R:
      if File.arrayContains(L, i):
         if (not i == "Sample"):
            File.Remove(i + ".txt")

   os.remove("Output.txt")
   File.fileVerification()
   File.totalClean()
   File.allFileExChange(True)

if (__name__ == "__main__"):

   ListCheck = []
   try:
      ListCheck = startup()

      if (File.isEmpty("Words/Sample.txt") or File.isEmpty("Words/Files.txt")):
         raise Error_Handler.CriticalFileErasedError

      # If something goes wrong

   except Error_Handler.FileReferenceError:
      Error_Handler.HandleRestore(Error_Handler.FileReferenceError, 1)

   except Error_Handler.CriticalFileErasedError:
      Error_Handler.HandleRestore(Error_Handler.CriticalFileErasedError, 3)

   except Error_Handler.CriticalFileNotFoundErrorError:
      Error_Handler.HandleRestore(Error_Handler.CriticalFileErasedError, 4)

   except Exception:
      Error_Handler.HandleRestore(Error_Handler.Error)

   try:
      Controller.main()

   except Exception:
      #raise Error_Handler.OpNotCompleteError
      Error_Handler.Terminate("During the use of the app, an operation by the user could not be completed", Error_Handler.OpNotCompleteError, 5)

   try:
      closeDown(ListCheck)
   except Exception:
      Error_Handler.Terminate("An error has occurred", Error_Handler.CloseDownFailureError, 6)

   finally:
      print("\n\nAll Processes Complete")

