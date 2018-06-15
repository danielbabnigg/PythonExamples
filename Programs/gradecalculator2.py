import sys
from collections import defaultdict

categories = {}
grades = {}

sum = 0
while sum <= 100:
    if sum == 100:
        print ("")
        for i in categories:
            print (i, "-", categories[i])
        break
    else:
        cat1 = str(input("What is your category? "))
        catk1 = int(input("What percentage is it of your grade? "))
        categories[cat1] = catk1
        grades[cat1] = [] 
        sum += catk1
else:
    print ("Invalid Percentages! Start over.")
    sys.exit(0)