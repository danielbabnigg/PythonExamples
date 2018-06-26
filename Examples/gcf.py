#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

def gcf(num1, num2):
    list1 = []
    list2 = []
    factors = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            list1.append(i)
        else:
            list1 = list1
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            list2.append(i)
        else:
            list2 = list2
    for a in list1:
        for i in list2:
            if a == i:
                factors.append(a)
    if factors == []:
        print ("")
        print ("There is no greatest common factor between %s and %s!" % (num1, num2))
    else:
        factors.reverse()
        print ("")
        print ("The greatest common factor between %s and %s is %s!" % (num1, num2, factors[0]))
gcf(int(input("First number? ")), int(input("Second number? ")))