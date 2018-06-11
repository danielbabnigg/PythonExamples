#title
print ("Welcome to the Pig Latin Translator!")

#original word input 
original = (input("Enter a word: "))

#check if word has letters and no numbers, if so then displaying it
if len(original) > 0 and original.isalpha():
  print (original)
else:
  print ("empty")