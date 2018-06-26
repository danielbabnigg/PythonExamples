#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

inputoperation = input("Your equation? ")
inputoperation = "".join(inputoperation.split())
inputoperation += "e"
list = []
num = ""
for i in inputoperation:
    try:
        i = int(i)
        num += str(i)
    except ValueError:
        list.append(int(num))
        list.append(i)
        num = ""
list.remove("e")

index = 0
answer = 0
for i in list:
    if index == 0:
        answer = i
    if i == "+":
        answer += int(list[index + 1])
    if i == "-":
        answer -= int(list[index + 1])
    if i == "*":
        answer *= int(list[index + 1])
    if i == "/":
        answer /= int(list[index + 1])
    index += 1

print ("The answer is " + str(round(answer, 2)))