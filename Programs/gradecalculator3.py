import sys

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
        categoryentryp = int(input("Percentage of grade? "))
        categories[categoryentry] = categoryentryp
        sum += categoryentryp
else:
    print ("Invalid percentages!")
    sys.exit(0)

for key in categories:
    print ("")
    print ("Enter your grades for each cateogry one by one, then type 'stop' if you wish to go to the next cateogry.")
    gradeentry = (input("What is a grade in %s? " % (key)))
    list1 = []
    grades[key] = list1
    list1.append(gradeentry)
    while gradeentry != "stop":
        gradeentry = (input("What is a grade in %s? " % (key)))
        list1.append(gradeentry)
    else:
        list1.remove("stop")
print ("")
for key in grades:
    print (key, "-", grades[key])

for key in categories:
    print (int(categories[key]))
    for i in grades[key]:
        print (int(i))

print ("Your grade report has been saved to this directory under gradereport.txt")