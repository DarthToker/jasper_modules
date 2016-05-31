# -*- coding: utf-8-*-
import re


WORDS = ["REPEAT"]

PRIORITY = 4

def quit(text):
    return bool(re.search(r'\b(quit)\b', text, re.IGNORECASE))

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

    #mic.say("what do you want me to say")
    exit = False
    while not exit:
        stuff = mic.activeListen()
        if is_exit(stuff):
            break
        mic.say(stuff)
    mic.say("stopping repeat")


def is_exit(text):
    return bool(re.search(r"(exit|quit|stop)", text, re.IGNORECASE))

        
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\brepeat\b', text, re.IGNORECASE))
