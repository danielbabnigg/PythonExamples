print ("""
Welcome!""")

print ("Please start off by entering your cateogires, type 'stop' if you are done.")

categories = []
numofcat = 1

print ("")
categoryentry = (input("Category? "))
while categoryentry != "stop":
    categoryentry = (input("Category? "))
    categories.append(str(categoryentry))
    numofcat += 1
    if categoryentry == "stop":
        del categories[numofcat]
        break
print (categories)