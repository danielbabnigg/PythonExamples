import random
from random import randint
import string


def encodetext(string):
    newstring = string[::-1]
    encodedstring = ""
    for i in newstring:
        encodedstring += str(i)
        for a in range(0, randint(1, 5)):
            encodedstring += (random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSUVWXYZ1234567890"))
    print (encodedstring)

encodetext(input("Message? "))