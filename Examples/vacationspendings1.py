print ("""
Welcome!""")

class Vacation(object):
    def __init__(self, rent, days, car, spending):
        self.rent = rent
        self.days = days
        self.car = car
        self.spending = spending
    def totalspendings(self):
        total = (int(self.rent) * (int(self.days)-1)) + (int(self.car) * int(self.days) + int(self.spending))
        print ("Your total is $" + str(total))

vacationspendings = Vacation(input("What is your nightly hotel rent? "), input("How many days total is your vacation? "), input("How much is your car per day if you're renting one? "), input("How much extra will you need? "))
vacationspendings.totalspendings()