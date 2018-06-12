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

#length of lists
bag = ["towel", "phone", "paper"]
print (len(bag))