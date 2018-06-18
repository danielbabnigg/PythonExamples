#using lambda to print lists
list1 = [x for x in range(11)]
print (filter(lambda x: x % 2 == 0, list1))

list2 = ["hi", "no", "yes"]
print (filter(lambda x: x == "hi", list2))

list3 = [x ** 3 for x in range(1, 101)]
print (filter(lambda x: ((x >= 100) and (x <= 500)), list3))