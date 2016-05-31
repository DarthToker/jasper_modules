# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
#mark1


new_word = "CPU TEMPERATURE" 
WORDS = ("%s" %new_word)

PRIORITY = 4

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    t = os.popen('vcgencmd measure_temp').readline()
    temp = t.replace("temp=","").replace("'C\n","")
    message = ("cpu temperature is %s degrees celsius." %temp)

    mic.say("%s" %message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
