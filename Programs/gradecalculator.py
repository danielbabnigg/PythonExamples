#importing datetime, time, and operator
from datetime import datetime
import time
import operator

print ("""
Welcome!""")
print ("Please start off by entering your categories and their corresponding percentages.")

#creating empty lists to store categories and grades
categories = {}
grades = {}
sum = 0

#asks for category and corresponding percentage, then stops if the percentages add up to 100, storing them in the categories dictionary
print ("")
while True:
    if round(sum, 0) == 100:
        categories = sorted(categories.items(), key=operator.itemgetter(1), reverse = True)
        categories = dict(categories)
        print ("")
        for i in categories:
            print (i, "-", categories[i])
        break
    elif sum > 100:
        print ("Invalid percentages, start over!")
        categories.clear()
        sum = 0
        continue
    else:
        categoryentry = str(input("Category? "))
        if not categoryentry.strip():
            print ("Please enter a valid category!")
            continue
        while True:
            try:
                categoryentryp = float(input("Percentage of total grade? "))
                break
            except ValueError:
                print ("Please enter a valid percentage!")
        categoryentry = categoryentry.strip()
        categoryentryp = round(categoryentryp, 2)
        categories[categoryentry] = categoryentryp
        sum += categoryentryp

time.sleep(1)

#asks for grades in each category, stores in the grades dictionary as lists
print("")
print ("Enter your percentage grades for each cateogry one by one, then type 'next' if you wish to go to the next cateogry.")
for key in categories:
    print ("")
    while True:
        try:
            gradeentry = (input("What is a grade in %s? " % (key)))
            if gradeentry != "next":
                gradeentry = float(gradeentry)
                break
            elif gradeentry == "next":
                print ("Please enter at least one grade!")
        except ValueError:
            print ("Enter a valid grade!")
    list1 = []
    grades[key] = list1
    list1.append(gradeentry)
    while gradeentry != "next":
        while True:
            try:
                gradeentry = (input("What is a grade in %s? " % (key)))
                if gradeentry != "next":
                    gradeentry = float(gradeentry)
                    break
                elif gradeentry == "next":
                    break
            except ValueError:
                print ("Enter a valid grade!")
        list1.append(gradeentry)
    else:
        list1.remove("next")
    list1.sort(reverse = True)
print ("")
for key in grades:
    printlistgrades = ""
    for i in grades[key]:
        printlistgrades += str(i) + ", "
    printlistgrades = printlistgrades[:-2]
    print (key, "-", printlistgrades)

#calculates then prints the overall average of the numbers
average = float(0)
for key in categories:
    gradesincat = float(0)
    numofgradesinsec = float(0)
    for i in grades[key]:
        gradesincat += float(i)
        numofgradesinsec += 1
    gradesincat = float(gradesincat)
    gradesincat = (float(gradesincat) / float(numofgradesinsec))
    gradesincat *= float(categories[key])
    average += float(gradesincat)
average = float(average * 0.01)
average = round(average, 2)
print ("")

time.sleep(1)

print ("Your average is", str(average) + "%")

time.sleep(1)

#creates .txt file with report, including all data above
now = datetime.now()
currentdate = ("%02d/%02d/%04d" % (now.month, now.day, now.year))
currenttime = ("%02d:%02d" % (now.hour, now.minute))
with open("gradereport.txt", "w+") as file:
    file.write("Your grade report as of " + str(currentdate) + " at " + str(currenttime) + "\n\n")
    file.write("Categories: " + "\n")
    for i in categories:
        file.write(str(i) + " - " + str(categories[i]) + "% of total grade" + "\n")
    file.write("\n")
    file.write("Grades: " + "\n")
    for key in grades:
        printlistgrades = ""
        for i in grades[key]:
            printlistgrades += str(i) + ", "
        printlistgrades = printlistgrades[:-2]
        file.write(str(key) + " - " + str(printlistgrades) + "\n")
    file.write("\n")
    file.write("Averages:" + "\n")
    for key in categories:
        gradesincat = float(0)
        numofgradesinsec = float(0)
        for i in grades[key]:
            gradesincat += float(i)
            numofgradesinsec += 1
        gradesincat = float(gradesincat)
        gradesincat = (float(gradesincat) / float(numofgradesinsec))
        gradesincat = round(gradesincat, 2)
        file.write(str(key) + " - " + str(gradesincat) + "%" + "\n")
    file.write("\n")
    file.write("Your overall average is " + str(average) + "%")
    file.write("\n")
    if average >= 97:
        aoran = "an"
        gradeletter = "A+"
        gradestring = "excellent job!"
    elif average >= 93:
        aoran = "an"
        gradeletter = "A"
        gradestring = "excellent job!"
    elif average >= 90:
        aoran = "an"
        gradeletter = "A-"
        gradestring = "great job!"
    elif average >= 87:
        aoran = "a"
        gradeletter = "B+"
        gradestring = "great job!"
    elif average >= 83:
        aoran = "a"
        gradeletter = "B"
        gradestring = "good job!"
    elif average >= 80:
        aoran = "a"
        gradeletter = "B-"
        gradestring = "good job!"
    elif average >= 77:
        aoran = "a"
        gradeletter = "C+"
        gradestring = "not bad!"
    elif average >= 73:
        aoran = "a"
        gradeletter = "C"
        gradestring = "not bad!"
    elif average >= 70:
        aoran = "a"
        gradeletter = "C-"
        gradestring = "you're almost there!"
    elif average >= 67:
        aoran = "a"
        gradeletter = "D+"
        gradestring = "you're almost there!"
    elif average >= 63:
        aoran = "a"
        gradeletter = "D"
        gradestring = "you could've done better!"
    elif average >= 60:
        aoran = "a"
        gradeletter = "D-"
        gradestring = "you could've done better!"
    else:
        aoran = "a"
        gradeletter = "F"
        gradestring = "study harder next time!"
    file.write("You got the letter grade of " + str(aoran) + " " + str(gradeletter) + ", " + str(gradestring))

print ("")
print ("A full grade report has been saved to this directory under gradereport.txt")