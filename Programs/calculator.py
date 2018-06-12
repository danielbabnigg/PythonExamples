operation = (input("Which operation? "))
num1 = (input("First number? "))
num2 = (input("Second number? "))

if (operation == "addition" or operation == "add"):
    answer = (int(num1) + int(num2))
elif (operation == "subtraction" or operation == "subtract"):
    answer = (int(num1) - int(num2))
elif (operation == "multiplication" or operation == "multiply"):
    answer = (int(num1) * int(num2))
elif (operation == "division" or operation == "divide"):
    answer = (int(num1) / int(num2))
else:
    print ("Invalid Operation")
print ("Your answer is %d" % (answer))