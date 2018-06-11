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