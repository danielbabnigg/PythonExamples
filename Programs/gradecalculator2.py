categories = {}


cat1 = str(input("What is your first category? "))
catk1 = int(input("What percentage is it of your grade? "))
categories[cat1] = catk1

for i in categories:
    print (i, "-", categories[i])