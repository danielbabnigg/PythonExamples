#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

print ("""
Welcome to the grade caluculator!
""")
hwper = float((input("What percentage is Homework? ")))
quper = float((input("What percentage are Quizzes? ")))
teper = float((input("What percentage are Tests? ")))

if hwper + quper + teper == 100:
    print ("")
    hwninp = float((input("How many Homework grades do you have? ")))
    if hwninp == 0:
        print ("")
        quninp = float((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("You have no grades to calculate!")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = float(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = float((float(quinp)+ float(quinp2)) / 2)
            print (str((float(quinp)+ float(quinp2)) / 2) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = float((float(quinp)+ float(quinp2) + float(quinp3)) / 3)
            print (str((float(quinp)+ float(quinp2) + float(quinp3)) / 3) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")
    elif hwninp == 1:
        hwinp = (input("What is your first homework grade? "))
        hwave = float(hwinp)
        print (str(hwinp) + "%")
        print ("")
        quninp = float((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(hwave * (hwper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = float(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = float((float(quinp)+ float(quinp2)) / 2)
            print (str((float(quinp)+ float(quinp2)) / 2) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = float((float(quinp)+ float(quinp2) + float(quinp3)) / 3)
            print (str((float(quinp)+ float(quinp2) + float(quinp3)) / 3) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")
    elif hwninp == 2:
        hwinp = (input("What is your first homework grade? "))
        hwinp2 = (input("What is your second homework grade? "))
        hwave = float((float(hwinp) + float(hwinp2)) / 2)
        print (str((float(hwinp) + float(hwinp2)) / 2) + "%")
        print ("")
        quninp = float((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100))+ (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = float(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = float((float(quinp)+ float(quinp2)) / 2)
            print (str((float(quinp)+ float(quinp2)) / 2) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = float((float(quinp)+ float(quinp2) + float(quinp3)) / 3)
            print (str((float(quinp)+ float(quinp2) + float(quinp3)) / 3) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")
    elif hwninp == 3:
        hwinp = (input("What is your first homework grade? "))
        hwinp2 = (input("What is your second homework grade? "))
        hwinp3 = (input("What is your third homework grade? "))
        hwave = float((float(hwinp) + float(hwinp2) + float(hwinp3)) / 3)
        print (str((float(hwinp) + float(hwinp2) + float(hwinp3)) / 3) + "%")
        print ("")
        quninp = float((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = float(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = float((float(quinp)+ float(quinp2)) / 2)
            print (str((float(quinp)+ float(quinp2)) / 2) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = float((float(quinp)+ float(quinp2) + float(quinp3)) / 3)
            print (str((float(quinp)+ float(quinp2) + float(quinp3)) / 3) + "%")
            print ("")
            teninp = float((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = float(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = float((float(teinp)+ float(teinp2)) / 2)
                print (str((float(teinp)+ float(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = float((float(teinp)+ float(teinp2) + float(teinp3)) / 3)
                print (str((float(teinp)+ float(teinp2) + float(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")
    else:
        print ("Too many grades!")
else:
    print ("Invalid percentages!")