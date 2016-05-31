# -*- coding: utf-8-*-
import random
import re
import os


WORDS = ["REBOOT"]

PRIORITY = 3

def handle(text, mic, profile):
    import subprocess
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["rebooting"]

    message = random.choice(messages)

    mic.say(message)
    subprocess.call(["sudo", "reboot"])


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bREBOOT\b', text, re.IGNORECASE))
