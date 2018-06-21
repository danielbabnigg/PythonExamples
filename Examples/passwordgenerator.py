from random import randint

def passgen(string, num):
    password = ""
    string = string.lower()
    for i in range(0, len(string)):
        randnum = randint(0,50)
        if randnum > 25:
            password += string[i].lower()
        if randnum <= 25:
            password += string[i].upper()
    password += str(num)
    print (password)

passgen(input("What's a word you want in your password? "), input("And how about a number? "))