#simple lists
zoo_animals = ["pangolin", "cassowary", "sloth", "hippo"]

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])

#changing lists
zoo_animals = ["pangolin", "cassowary", "sloth", "hippo"]
zoo_animals[0] = "tiger"

#adding to lists
box = []
box.append("cookies")
print (box)

box.insert(1, "cake")
print (box)

#deleting parts of lists
hi = ["hey", "hi", "hello", "hiya"]
hi.remove("hiya")
print (hi)

#length of lists
bag = ["towel", "phone", "paper"]
print (len(bag))

#portions of lists
letters = ["a", "b", "c", "d", "e"]
slice = letters[0:3]
print (letters)
print (slice)

animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]

#finding index numbers
fish = ["betta", "tropical", "tetra", "guppie"]
print (fish.index("tropical"))

#sorting lists
fruit = ["apple", "peach", "pineapple", "grape"]
print (fruit)

#dictionaries
fruit1 = {"apple" : "red", "peach" : "orange", "pineapple" : "yellow", "grape" : "purple"}

del fruit1["apple"]
print (fruit1)

fruit1["peach"] = "light orange"
print (fruit1)

#creating new lists
odd_cubes = [x ** 3 for x in range(1, 100) if x % 2 == 1]
print (odd_cubes)

#more complicated if's in lists
square_by_three = [x ** 2 for x in range(1, 21) if ((x ** 2) % 3) == 0]
print (square_by_three)

#slicing lists
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (list1[2:7:2])

#defaults in slicing
print (list1[0:2])
print (list1[:6])
print (list1[::2])

#negative steps causing reverse lists
list2 = ["hi", "yes", "ok", "no", "cool"]
backwardslist2 = list2[::-1]
print (backwardslist2)

list3 = [x for x in range(101)]
backwardsbysevens = list3[::-7]
print (backwardsbysevens)

#placing sliced comprehension lists in new lists
list4 = [x for x in range(1,21)]
oddlist4 = list4[::2]
middlelist4 = list4[7:13]
print (list4)
print (oddlist4)
print (middlelist4)