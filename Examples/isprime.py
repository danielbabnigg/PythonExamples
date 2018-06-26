#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

num = int(input("Number? "))
isprime = True
divisor = 0
for i in range(2, num-1):
    if num % i == 0:
        isprime = False
        divisor = i
        break
    if num % i == 1:
        isprime = True
if isprime == True:
    print (str(num) + " is a prime number!")
else:
    print (str(divisor) + " * " + str(num//divisor) + " equals " + str(num))