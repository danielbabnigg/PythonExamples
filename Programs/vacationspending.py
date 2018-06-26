#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

def hotel_cost(nights):
  return (140 * nights)

def plane_ride_cost(city):
  if (city == "Charlotte"):
    return 183
  elif (city == "Tampa"):
    return 220
  elif (city == "Chicago"):
    return 222
  elif (city == "Los Angeles"):
    return 475

def rental_car_cost(days):
  cost = (days * 40)
  if (days >= 7):
    cost -= 50
  elif (days >= 3):
    cost -= 20
  return cost

city = (input("Where is your destination?: "))
days = (input("How many days are you staying?: "))
spending_money = (input("How much extra do you need?: "))

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print ("Your total is " + str(trip_cost(str(city), int(days), int(spending_money))))