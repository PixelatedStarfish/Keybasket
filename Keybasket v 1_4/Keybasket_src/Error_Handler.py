#!/usr/bin/env python3

import tkinter as tkin
from tkinter import messagebox
import Restore
import traceback
import sys

class Error(Exception):
    message = ""
    def __init__(self):
        super().__init__(self.message)


class FileReferenceError(Error):
    def __init__(self, file = "Words/Files.txt", message = "Missing reference for file. (ErrCode 1)"):
        self.message = message + "\n" + file



class FileNotFoundError(Error):
    def __init__(self, file = "Words/Sample.txt", message = "File Not Found. (ErrCode 2)"):
        self.message = message + "\n" + file



class CriticalFileErasedError(Error):
    def __init__(self, file = "Words/Sample.txt", message="Critical Files Erased. (ErrCode 3)"):
        self.message = message + "\n" + file

class CriticalFileNotFoundError(Error):
    def __init__(self, file = "Words/Sample.txt", message="Critical Files Deleted. (ErrCode 4)"):
        self.message = message + "\n" + file


class OpNotCompleteError(Error):
    def __init__(self, message="The Operation Could not be Completed. (ErrCode 5)"):
        self.message = message

class CloseDownFailureError(Error):
    def __init__(self, message="Close down procedure failure. Restart the application to resolve it. (Errcode 6)"):
        self.message = message

class RestoreFailureError(Error):
    def __init__(self, message="Restore Failure; The Application has been tampered with. The restore file has been compromised. (ErrCode 7)"):
        self.message = message





'''
Indicates a failure.
'''
def failureBox(strr):
    root = tkin.Tk()

    root.geometry("0x0")
    msg = messagebox.showerror("Error", strr)

'''
asks yes or no for a restore
'''

def YesNo(strr):
    root = tkin.Tk()

    #root.option_add('*Dialog.msg.font', 'Calibri 20')
    root.geometry("0x0")
    return messagebox.askyesno("Restore Required", strr)

'''
get message for error code i, from 0 to 5

An Error Occurred. (ErrCode 0)
Missing reference for file. (ErrCode 1)
File Not Found. (ErrCode 2)
Critical Files Erased. (ErrCode 3)
Critical File Not Found. (ErrCode 4)
An Operation Could Not Be Completed. (ErrCode 5)
Close down procedure failure. Restart the application to resolve it. (Errcode 6)
Restore Failure; The Application has been tampered with. The restore file has been compromised. (ErrCode 7)

@param i
@return a string Errcode
'''

def ErrorCode(i):
    ErrCode = ""
    if (i == 1):
        ErrCode = "Missing reference for file. (ErrCode 1)"
        return ErrCode

    if (i == 2):
        ErrCode = "File Not Found. (ErrCode 2)"
        return ErrCode

    if (i == 3):
        ErrCode = "Critical Files Erased. (ErrCode 3)"
        return ErrCode

    if (i == 4):
        ErrCode = "Critical File Not Found. (ErrCode 4)"
        return ErrCode

    if (i == 5):
        ErrCode = "An Operation Could Not Be Completed. (ErrCode 5)"
        return ErrCode

    if (i == 6):
        ErrCode = "Close down procedure failure. Restart the application to resolve it. (Errcode 6)"
        return ErrCode

    if (i == 7):
        ErrCode = "Restore Failure; The Application has been tampered with. The restore file has been compromised. (ErrCode 7)"
        return ErrCode

    else:
        ErrCode = "An Error Occurred. (ErrCode 0)"

    return ErrCode
'''
As the name implies, it calls Restore.restore to handle restores, then it pops up the Terminate message
@param e the error. Default is generic error
@param i the error code. Default is 0 for a generic error
'''

def HandleRestore(e = Error, i = 0):
   if (YesNo("The Application has failed and needs to be restored. During restoration, files will be deleted. Would you like to restore?")):
      Restore.restore()

      Terminate("Restore successful, please restart the application", e, i)

   else:
      Terminate("The application will need to be restored. ", e, i)

'''
Produces a window with a message to describe an error. Then, terminates the program.
@param message the error message
@param e the error. Default is generic error
@param i the error code. Default is 0 for a generic error
'''

def Terminate(message, e = Error, i = 0):

    s = message + "\n\n" + ErrorCode(i)

    if (i == 0 or i > 4):

        #If the exception is generic or not defined, then it's time to show the traceback
        print("Debug Information (Stack Trace):\n\n" + traceback.format_exc())

    failureBox(s)
    sys.exit(1)