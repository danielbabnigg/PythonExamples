#basic function
def breakfast():
    """Lists breakfast foods"""
    print ("Eggs, bacon, toast")
breakfast()

#calling functions
def square(n):
    squared = (n ** 2)
    print ("%d squared is %d" % (n, squared))
    return squared
square(6)

#functions with multiple parameters
def square1(base, exponent):
    solution = base ** exponent
    print (("%d to the power of %d is equal to %d") % (base, exponent, solution))
square1(5, 2)

#functions to other functions
def cube(number):
  return (number ** 3)
def by_three(number):
  if (number % 3 == 0):
    return cube(number)
  else:
    return False

#functions with more complicated math
def biggest_number(*args):
  print (max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#functions with elif
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
print (shut_down("no"))

#example with if and or
def distance_from_zero1(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"
print (distance_from_zero(-5.234))

#functions and lists
def function(x):
    x[0] = x[0] + 2
    return x
y = [1, 2, 3, 4, 5]
print (function(y))

names = ["Daniel", "Gyorgy", "Ana", "Lenka"]
def join_names(words):
    result = ""
    for word in words:
        result += word
    return result
print (join_names(names))

#functions used to join lists
list1 = [1, 2, 3, 4]
list2 = [2, 7, 3, 5, 8, 7]
def join_lists(x, y):
    return (x + y)
print (join_lists(list1, list2))

list3 = [[1, 2, 3], [4, 5, 6]]
def flatten(lists):
    end = []
    for numbers in lists:
        for number in numbers:
            end.append(number)
    return end
print (flatten(list3))