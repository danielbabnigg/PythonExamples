print ("Available Operations: add, subtract, multiply, divide, square, power")
operation = (input("Which operation? "))

if (operation == "addition" or operation == "add"):
    num1 = (input("First number? "))
    num2 = (input("Plus what number? "))
    answer = (int(num1) + int(num2))
elif (operation == "subtraction" or operation == "subtract"):
    num1 = (input("First number? "))
    num2 = (input("Minus what number? "))
    answer = (int(num1) - int(num2))
elif (operation == "multiplication" or operation == "multiply"):
    num1 = (input("First number? "))
    num2 = (input("Times what number? "))
    answer = (int(num1) * int(num2))
elif (operation == "division" or operation == "divide"):
    num1 = (input("First number? "))
    num2 = (input("Divided by what number? "))
    answer = (int(num1) / int(num2))
elif (operation == "square"):
    num1 = (input("First number? "))
    answer = (int(num1) ** 2)
elif (operation == "power"):
    num1 = (input("First number? "))
    num2 = (input("To the power of what number? "))
    answer = (int(num1) ** int(num2))
else:
    print ("Invalid Operation")
print ("Your answer is %s" % (answer))