import sys
from datetime import datetime

print ("""
Welcome!""")
print ("Please start off by entering your cateogires and their corresponding percentages.")

categories = {}
grades = {}
sum = 0

print ("")
while sum <= 100:
    if sum == 100:
        print ("")
        for i in categories:
            print (i, "-", categories[i])
        break
    else:
        categoryentry = str(input("Category? "))
        categoryentryp = float(input("Percentage of grade? "))
        categories[categoryentry] = categoryentryp
        sum += categoryentryp
else:
    print ("Invalid percentages!")
    sys.exit(0)

print("")
print ("Enter your percentage grades for each cateogry one by one, then type 'next' if you wish to go to the next cateogry.")
for key in categories:
    print ("")
    gradeentry = (input("What is a grade in %s? " % (key)))
    list1 = []
    grades[key] = list1
    list1.append(gradeentry)
    while gradeentry != "next":
        gradeentry = (input("What is a grade in %s? " % (key)))
        list1.append(gradeentry)
    else:
        list1.remove("next")
print ("")
for key in grades:
    printlistgrades = ""
    for i in grades[key]:
        printlistgrades += str(i) + ", "
    printlistgrades = printlistgrades[:-2]
    print (key, "-", printlistgrades)

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

print ("Your average is", str(average) + "%")

now = datetime.now()
currentdate = ("%02d/%02d/%04d" % (now.month, now.day, now.year))
currenttime = ("%02d:%02d" % (now.hour, now.minute))
with open("gradereport.txt", "x") as file:
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
    file.write("Your letter grade is " + str(aoran) + " " + str(gradeletter) + ", " + str(gradestring))
print ("")
print ("Your full grade report has been saved to this directory under gradereport.txt")