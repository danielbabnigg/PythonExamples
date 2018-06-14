#general format for while
count = 0
while count < 6:
    print ("The current count is", count)
    count = count + 1

num = 1
while num <= 100:
    print (num ** 2)
    num = num + 1

#breaking while loops
from random import randint
random_integer = randint(0, 10)
guesses = 3
while guesses > 0:
    guess = int(input("Your guess: "))
    guesses -= 1
    if guess == random_integer:
        print ("You win!")
        break
else:
    print ("You lose :(")

#using "for" for loops
fruits = []
for i in range(5):
    fruit = input("Tell me your favorite fruits: ")
    fruits.append(fruit)
print (fruits)