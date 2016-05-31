# -*- coding: utf-8-*-
import re
import pycurl
from StringIO import StringIO


#mark1
new_word = "SEND TEXT"

message = "sending text"

WORDS = [(new_word), "YES", "NO"]

PRIORITY = 4

def yes(text):
    return bool(re.search(r'\b(yes)\b', text, re.IGNORECASE))

def no(text):
    return bool(re.search(r'\b(no)\b', text, re.IGNORECASE))


def handle(text, mic, profile):

    def getnum():
        global num        
        mic.say("what number should i send it to?")
        num = mic.activeListen()
        mic.say("did you say %s?" %num)
        reply1 = mic.activeListen()
        if no(reply1):
            getnum()
        if yes(reply1):
            return

        

    def getmsg():
        global msg
        mic.say("what is your message?")
        msg = mic.activeListen()
        mic.say("did you say %s?" %msg)
        reply2 = mic.activeListen()
        if no(reply2):
            getmsg()
        if yes(reply2):
            return
        
    getnum()    
    getmsg()

    mic.say(message)

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://textbelt.com/text')
    c.setopt(c.POSTFIELDS, 'number=%s&message=%s' %(num, msg))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    if "true" in body:
        mic.say("text sent successfully")
    if "false" in body:
        mic.say("text failed to send")
    if "quota" in body:
        mic.say("too many texts sent to that number, wait 2 minutes")
    if "number" in body:
        mic.say("Invalid phone number")    



  



    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
