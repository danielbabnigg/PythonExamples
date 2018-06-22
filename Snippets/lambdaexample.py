#general lambda statements
a = lambda x, y : x * y
print (a(10, 10))
b = lambda x, y : x - y + 2 * x
print (b(5, 2))

#using lambda to print lists
list1 = [x for x in range(11)]
print (list1)
result1 = filter(lambda x: x % 2 == 0, list1)
print (result1)

list2 = [x ** 3 for x in range(1, 11)]
print (list2)
result2 = filter(lambda x: x % 2 == 0, list2)
print (result2)