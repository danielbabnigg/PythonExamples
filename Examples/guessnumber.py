#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

from random import randint

n = randint(1, 99)
guess = int(input("What is your guess? "))

while n != guess:
    if n > guess:
        print ("Too low!")
        guess = int(input("What is your guess? "))
    if n < guess:
        print ("Too high!")
        guess = int(input("What is your guess? "))
else:
    print ("You guessed it!")