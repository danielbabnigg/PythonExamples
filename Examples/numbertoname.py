def numtoname(num):
    num = str(num)
    numstring = ""
    for i in num:
        if i == 0:
            numstring += "zero "
        elif i == 1:
            numstring += "one "
        elif i == 2:
            numstring += "two "
        elif i == 3:
            numstring += "three "
        elif i == 4:
            numstring += "four "
        elif i == 5:
            numstring += "five "
        elif i == 6:
            numstring += "six "
        elif i == 7:
            numstring += "seven "
        elif i == 8:
            numstring += "eight "
        elif i == 9:
            numstring += "nine "
    print (numstring)

numtoname(1007)