print ("""
Welcome to the grade caluculator!
""")
hwper = int((input("What percentage is Homework? ")))
quper = int((input("What percentage are Quizzes? ")))
teper = int((input("What percentage are Tests? ")))

if hwper + quper + teper == 100:
    print ("")
    hwninp = int((input("How many Homework grades do you have? ")))
    if hwninp == 0:
        print ("")
        quninp = int((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("You have no grades to calculate!")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str(teave * (teper/100)) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = int(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = int((int(quinp)+ int(quinp2)) / 2)
            print (str((int(quinp)+ int(quinp2)) / 2) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = int((int(quinp)+ int(quinp2) + int(quinp3)) / 3)
            print (str((int(quinp)+ int(quinp2) + int(quinp3)) / 3) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(quave * (quper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")














    elif hwninp == 1:
        hwinp = (input("What is your first homework grade? "))
        hwave = int(hwinp)
        print (str(hwinp) + "%")
        print ("")
        quninp = int((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str(hwave * (hwper/100)) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = int(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = int((int(quinp)+ int(quinp2)) / 2)
            print (str((int(quinp)+ int(quinp2)) / 2) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = int((int(quinp)+ int(quinp2) + int(quinp3)) / 3)
            print (str((int(quinp)+ int(quinp2) + int(quinp3)) / 3) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        else:
            print ("Too many grades!")
    elif hwninp == 2:
        hwinp = (input("What is your first homework grade? "))
        hwinp2 = (input("What is your second homework grade? "))
        hwave = int((int(hwinp) + int(hwinp2)) / 2)
        print (str((int(hwinp) + int(hwinp2)) / 2) + "%")
        print ("")
        quninp = int((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = int(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = int((int(quinp)+ int(quinp2)) / 2)
            print (str((int(quinp)+ int(quinp2)) / 2) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = int((int(quinp)+ int(quinp2) + int(quinp3)) / 3)
            print (str((int(quinp)+ int(quinp2) + int(quinp3)) / 3) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
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
        hwave = int((int(hwinp) + int(hwinp2) + int(hwinp3)) / 3)
        print (str((int(hwinp) + int(hwinp2) + int(hwinp3)) / 3) + "%")
        print ("")
        quninp = int((input("How many Quiz grades do you have? ")))
        if quninp == 0:
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 1:
            quinp = (input("What is your first quiz grade? "))
            quave = int(quinp)
            print (str(quinp) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 2:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quave = int((int(quinp)+ int(quinp2)) / 2)
            print (str((int(quinp)+ int(quinp2)) / 2) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            else:
                print ("Too many grades!")
        elif quninp == 3:
            quinp = (input("What is your first quiz grade? "))
            quinp2 = (input("What is your second quiz grade? "))
            quinp3 = (input("What is your third quiz grade? "))
            quave = int((int(quinp)+ int(quinp2) + int(quinp3)) / 3)
            print (str((int(quinp)+ int(quinp2) + int(quinp3)) / 3) + "%")
            print ("")
            teninp = int((input("How many Test grades do you have? ")))
            if teninp == 0:
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 1:
                teinp = (input("What is your first test grade? "))
                teave = int(teinp)
                print (str(teinp) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 2:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teave = int((int(teinp)+ int(teinp2)) / 2)
                print (str((int(teinp)+ int(teinp2)) / 2) + "%")
                print ("")
                print ("Average: " + str((hwave * (hwper/100)) + (quave * (quper/100)) + (teave * (teper/100))) + "%")
            elif teninp == 3:
                teinp = (input("What is your first test grade? "))
                teinp2 = (input("What is your second test grade? "))
                teinp3 = (input("What is your third test grade? "))
                teave = int((int(teinp)+ int(teinp2) + int(teinp3)) / 3)
                print (str((int(teinp)+ int(teinp2) + int(teinp3)) / 3) + "%")
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