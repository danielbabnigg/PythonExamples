#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

print ("")
inputoperation = input("Your equation? ")
inputoperation1 = "".join(inputoperation.split())

newstring = ""
for i in inputoperation1:
    i = i.replace("x", "*")
    i = i.replace("÷", "/")
    i = i.replace("^", "**")
    i = i.replace("=", "")
    i = i.replace("?", "")
    newstring += i

print ("")
print (inputoperation, "is", round((eval(newstring)), 2))