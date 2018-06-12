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
def square(base, exponent):
    solution = base ** exponent
    print (("%d to the power of %d is equal to %d") % (base, exponent, solution))
square(5, 2)

#functions to other functions
def cube(number):
  return (number ** 3)
def by_three(number):
  if (number % 3 == 0):
    return cube(number)
  else:
    return False