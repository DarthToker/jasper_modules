# -*- coding: utf-8-*-
import random
import re
import time

WORDS = ["GOOGLE"]

PRIORITY = 4


def handle(text, mic, profile):
    import subprocess
    global google_s
    
    text1 = text
    new = text1.replace("GOOGLE", "")
    new2 = new.lower()
    mic.say("Googling %s" %new2)
    google_s = subprocess.Popen(["epiphany", "--display=:0", "https://www.google.com/?gws_rd=ssl#q=%s" %new2])
    google_s

    
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bgoogle\b', text, re.IGNORECASE))
