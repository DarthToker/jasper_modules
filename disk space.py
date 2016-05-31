# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
#mark1


new_word = "DISK SPACE" 
WORDS = ("%s" %new_word)

PRIORITY = 4

def handle(text, mic, profile):
    

    def getdiskspace():
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])
    w = getdiskspace()
    w1 = w[3]
    w2 = w[2].replace("M","")



    message = ("your disk is %s full and has %s megabytes left" %(w1, w2))

               
               


    mic.say("%s" %message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
