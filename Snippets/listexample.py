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
print box

box.insert(1, "cake")
print box

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
print fish.index("tropical")

#sorting lists
fruit = ["apple", "peach", "pineapple", "grape"]
print (fruit)

#dictionaries
fruit = {"apple" : "red", "peach" : "orange", "pineapple" : "yellow", "grape" : "purple"}

del fruit["apple"]

fruit["peach"] = "light orange"