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