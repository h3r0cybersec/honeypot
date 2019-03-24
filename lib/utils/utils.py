#!/usr/bin/env python3
"""
    Author : Cavallo Luigi
    Description : This file include utilities used in all the project
"""

from termcolor import colored
import os
from multiprocessing import Process

def message(message, sym="[*]", color="cyan"):
    """
        Stampa in console un messaggio colorato
        @param message: Message to print 
        @param sym: type of message these are the
                    standard:
                    [*] => notification
                    [#] => warning 
                    [!] => error 
        @param color: color of the message in console
                      these are the standard:
                      cyan   => for notifications 
                      yellow => for warnings 
                      red    => for errors
    """
    print(colored("%s %s" %(sym, message), color))

def is_root():
    """
        Verify if user that execute the script is root or not
    """
    if os.getuid() is 0:
        return True
    return False

def create_new_process():
    pass


if __name__ == "__main__":
    message("sono un messaggio di prova")