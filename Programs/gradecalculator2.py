categories = {}
while True:
    if cat1 != "stop":
        cat1 = str(input("What is your first category? "))
        catk1 = int(input("What percentage is it of your grade? "))
        categories[cat1] = catk1
    else:
        break
for i in categories:
    print (i, "-", categories[i])