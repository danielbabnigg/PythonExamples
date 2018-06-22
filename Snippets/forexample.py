#general for-loop with list
list = [1,2,3,4,5,6,7,8,9]
for number in list:
    print (number ** 2)

#if statements in for-loops
a = [1, 2, 5, 8, 9, 21, 32, 30, 12]
for number in a:
    if number % 2 != 0:
        print (number)
print ("All odd numbers printed")

#more complex loops
total = 0
prices = {
    "bread": 5,
    "apple": 3,
    "roll": 4
}
amount = {
    "bread": 8,
    "apple": 5,
    "roll": 2
}
for food in prices:
    print (food)
    print ("price: %s" % prices[food])
    print ("amount: %s" % amount[food])
    total += (prices[food] * amount[food])
print (total)

#another example with dictionaries
dict1 = {1:2, 2:4, 3:6, 4:8, 5:10}
for i in dict1:
    print (i)
    print (dict1[i])