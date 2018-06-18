#calling items in a dictionary
dict1 = {"Hi": 1, "No": 2, "Yes": 3, "Ok": 4}
print (dict1.items())

#callings keys and values from a dictionary
dict2 = {"Animal": 1, "Sheep": 2, "Cow": 3, "Hippo": 4}
print (dict2.keys())
print (dict2.values())

#using for loops to print dictionaries neatly
dict3 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for key in dict3:
    print (key, dict3[key])