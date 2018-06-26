#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

#title
print ("Welcome to the Pig Latin Translator!")

#variables
pyg = "ay"

#original word input 
original = (input("Enter a word: "))

#check if word has letters and no numbers, if so then displaying it
if len(original) > 0 and original.isalpha():
  word = (original.lower())
  first = (word[0])
  new_word = (word + first + pyg)
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
  print ("empty")