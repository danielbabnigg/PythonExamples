#basic classes
class Food(object):
    def __init__(self, color):
        self.color = color
orange = Food("Orange")
print (orange.color)

class Animals(object):
    healthy = "yes"
    def __init__(self, name, age, color, is_good):
        self.name = name
        self.age = age
        self.color = color
        self.is_good = is_good
    def description(self):
        print (self.name)
        print (self.age)
hippo = Animals("Bruce", 5, "Orange", True)
print (hippo.name, hippo.age, hippo.color, hippo.is_good)
hippo.description()
print (hippo.healthy)

#overriding from other classes
class Employee(object):
    def __init__(self, name):
        self.name = name
        print (name)
    def wage(self, hours):
        self.hours = hours
        return (hours * 20)
class Intern(Employee):
    def wage(self, hours):
        self.hours = hours
        return (hours * 9)
person = Employee("db")
print (person.wage(20))
person2 = Intern("ab")
print (person2.wage(20))

#retreiving from overwritten classes
class Person(object):
    def __init__(self, name):
        self.name = name
        print (name)
    def wage(self, age):
        self.age = age
        return ((age * 10) + 10000)
class Student(Person):
    def wage(self, age):
        self.age = age
        return ((age * 2) + 5000)
    def workingwage(self, age):
        return super(Student, self).wage(age)
hi = Student("hi")
print (hi.wage(20))
print (hi.workingwage(20))

#classes with if-statments
class Square(object):
    def __init__(self, angle1, angle2, angle3, angle4):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.angle4 = angle4
    def checkangles(self):
        if ((self.angle1 + self.angle2 + self.angle3 + self.angle4) == 360):
            return True
        else:
            return False
square1 = Square(90, 90, 90, 90)
print (square1.checkangles())

#another example
class Fruit(object):
    freshness = "ripe"
    def __init__(self, type, color, shape):
        self.type = type
        self.color = color
        self.shape = shape
    def display(self):
        print ("This is a %s, %s %s." % (self.shape, self.color, self.type))
    def fruitwaits(self):
        self.freshness = "rotten"
class Preservatives(Fruit):
    def fruitwaits(self):
        self.freshness = "not flavorful"
my_fruit = Fruit("peach", "orange", "circular")
my_fruit.display()
my_fruit.fruitwaits()
print (my_fruit.freshness)
new_fruit = Preservatives("grape", "purple", "small")
new_fruit.display()
new_fruit.fruitwaits()
print (new_fruit.freshness)