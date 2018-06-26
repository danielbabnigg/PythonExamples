#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

print ("Available Operations: add, subtract, multiply, divide, square, power")
operation = (input("Which operation? "))

if (operation == "addition" or operation == "add"):
    num1 = (input("First number? "))
    num2 = (input("Plus what number? "))
    answer = (float(num1) + float(num2))
elif (operation == "subtraction" or operation == "subtract"):
    num1 = (input("First number? "))
    num2 = (input("Minus what number? "))
    answer = (float(num1) - float(num2))
elif (operation == "multiplication" or operation == "multiply"):
    num1 = (input("First number? "))
    num2 = (input("Times what number? "))
    answer = (float(num1) * float(num2))
elif (operation == "division" or operation == "divide"):
    num1 = (input("First number? "))
    num2 = (input("Divided by what number? "))
    answer = (float(num1) / float(num2))
elif (operation == "square"):
    num1 = (input("First number? "))
    answer = (float(num1) ** 2)
elif (operation == "power"):
    num1 = (input("First number? "))
    num2 = (input("To the power of what number? "))
    answer = (float(num1) ** float(num2))
else:
    print ("Invalid Operation")
print ("Your answer is %s" % (answer))