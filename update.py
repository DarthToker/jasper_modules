# -*- coding: utf-8-*-
import random
import re
import os
import subprocess

WORDS = ["UPDATE"]

PRIORITY = 3

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
    messages = ["updating"]

    message = random.choice(messages)

    mic.say(message)
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])

    mic.say("update compleat")

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bupdate\b', text, re.IGNORECASE))
