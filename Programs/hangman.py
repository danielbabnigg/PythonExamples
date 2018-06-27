#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'

import sys
import time
import random

print ("""
Welcome to hangmen! To start, guess a letter to see if it's in the goal word.\nIf you think you know the answer, then type out the full word.
""")

playagain = True

while playagain == True:
    goalword = random.choice(("animal", "art", "aunt", "artwork", "area", "ant", "all", "apple", "beach", "biggest", "best", "better", "bleed", 
    "bless", "believe", "bell", "boast", "call", "calling", "cause", "cough", "can", "chalk", "close", "cope", "dough", "dark", "dog", "demon", 
    "deadly", "death", "dolphin", "dial", "done", "dilligent", "elephant", "ears", "eyes", "enter", "entry", "ending", "ellipse", "eating", "epic",
    "funny", "fantastic", "fan", "fins", "forts", "full", "fill", "fairy", "great", "gears", "games", "goat", "going", "gaps", "gills", "gobble", 
    "hello", "high", "hill", "hopes", "hooked", "hole", "have", "halves", "hears", "italics", "integer", "ill", "identity", "input", "jungle", 
    "jiggle", "jury", "jumping", "jaws", "key", "kettle", "kiwi", "lower", "lame", "learn", "lean", "looking", "loops", "lull", "learnt", "lambs", 
    "money", "much", "merry", "more", "married", "mapping", "meet", "malls", "month", "none", "nope", "name", "near", "never", "narrow", "now",
    "nod", "operation", "opera", "oars", "oat", "okay", "odd", "person", "perfect", "pear", "please", "papers", "popular", "pairs", "pocket", "poach",
    "query", "queue", "question", "quill", "queer", "right", "rains", "rolls", "ridge", "ropes", "reins", "rake", "radical", "really", "rookie", 
    "smart", "smear", "soap", "sapling", "same", "socks", "smells", "saw", "soaks", "selling", "sunscreen", "socket", "tears", "tall", "top", "tar", 
    "taps", "tackle", "temper", "tip", "thunder", "thing", "there", "their", "the", "that", "thorns", "tanks", "under", "unlikely", "utility",
    "understood", "undefined", "users", "upper", "versus", "volleyball", "vulture", "vacant", "vacation", "vary", "words", "works", "wear", "whenever",
    "where", "walls", "war", "ways", "willingly", "winking", "went", "xylophone", "yes", "yams", "yards", "years", "yelling", "zebra", "zero"))
    gameboard = ["    ...........    ","    ..._____...    ", "    ..|.....|..    ", "    ........|..    ", "    ........|..    ", "    ........|..    ", "    ........|..    ", "    ‾‾‾‾‾‾‾‾‾‾‾    "]
    wrongletters = [" "]
    wrongwords = [" "]
    correctguesses = []
    if len(goalword) == 3:
        letterblanks = "       _ _ _       "
        letterspaces = "       "
        gameboard.append(letterblanks)
    elif len(goalword) == 4:
        letterblanks = "      _ _ _ _      "
        letterspaces = "      "
        gameboard.append(letterblanks)
    elif len(goalword) == 5:
        letterblanks = "     _ _ _ _ _     "
        letterspaces = "     "
        gameboard.append(letterblanks)
    elif len(goalword) == 6:
        letterblanks = "    _ _ _ _ _ _    "
        letterspaces = "    "
        gameboard.append(letterblanks)
    elif len(goalword) == 7:
        letterblanks = "   _ _ _ _ _ _ _   "
        letterspaces = "   "
        gameboard.append(letterblanks)
    elif len(goalword) == 8:
        letterblanks = "  _ _ _ _ _ _ _ _  "
        letterspaces = "  "
        gameboard.append(letterblanks)
    elif len(goalword) == 9:
        letterblanks = " _ _ _ _ _ _ _ _ _ "
        letterspaces = " "
        gameboard.append(letterblanks)
    elif len(goalword) == 10:
        letterblanks = "_ _ _ _ _ _ _ _ _ _"
        letterspaces = ""
        gameboard.append(letterblanks)

    wrongguesses = 0
    def printboard():
        num = 1
        for i in gameboard:
            if i == "    ...........    ":
                print (i, "Wrong: %s" % (wrongguesses))
            elif (len(wrongletters)) > num and (len(wrongwords)) > num:
                print (i, wrongletters[num] + "   " + wrongwords[num])
                num += 1
            elif (len(wrongletters)) > num:
                print (i, wrongletters[num])
                num += 1
            elif (len(wrongwords)) > num:
                print (i, " " + "   " + wrongwords[num])
                num += 1
            else:
                print (i)
                num = num
    printboard()

    while True:
        letterguess = (input("\nYour guess: "))
        letterguess = letterguess.lower()
        letterguess = letterguess.strip()
        letter = 1
        alreadyguessed = False
        try:
            letterguess = int(letterguess)
            print ("\nPlease enter a valid character or word!")
            continue
        except ValueError:
            pass
        specialcharacter = False
        for i in """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~""":
            for a in letterguess:
                if a == i:
                    specialcharacter = True
                    break
        for i in wrongletters:
            if letterguess == i:
                print ("\nYou already guessed that letter!")
                alreadyguessed = True
                break
        for i in wrongwords:
            if letterguess == i:
                print ("\nYou already guessed that word!")
                alreadyguessed = True
                break
        for i in correctguesses:
            if letterguess == i:
                print ("\nYou already guessed that letter!")
                alreadyguessed = True
                break

        while len(letterguess) == 0:
            print ("\nEnter a valid character or word!")
            letterguess = (input("\nYour guess: "))
            if len(letterguess) == 1:
                for i in """0123456789!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~""":
                    for a in letterguess:
                        if a == i:
                            specialcharacter = True
                            break
                for i in wrongletters:
                    if letterguess == i:
                        print ("\nYou already guessed that letter!")
                        alreadyguessed = True
                        continue
                for i in wrongwords:
                    if letterguess == i:
                        print ("\nYou already guessed that word!")
                        alreadyguessed = True
                        continue
                for i in correctguesses:
                    if letterguess == i:
                        print ("\nYou already guessed that letter!")
                        alreadyguessed = True
                        continue
                break
            if len(letterguess) > 1:
                for i in """0123456789!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~""":
                    for a in letterguess:
                        if a == i:
                            specialcharacter = True
                            break
                if letterguess == goalword:
                    print ("\nCongrats, you win!")
                    letterblanksstr = ""
                    for i in goalword:
                        letterblanksstr += (i + " ")
                    letterblanks = letterspaces + letterblanksstr + letterspaces
                    gameboard[8] = letterblanks
                    printboard()
                    break
                else:
                    break

        if alreadyguessed == True:
            continue
        if specialcharacter == True:
            print ("\nPlease enter a valid character or word!")
            continue

        if len(letterguess) > 1:
            if letterguess == goalword:
                print ("\nCongrats, you win!")
                letterblanksstr = ""
                for i in goalword:
                    letterblanksstr += (i + " ")
                letterblanks = letterspaces + letterblanksstr + letterspaces
                gameboard[8] = letterblanks
                printboard()
                break
            else:
                print ("\nIncorrect guess!")
                wrongwords.append(letterguess)
                wrongguesses += 1

        correctletter = False
        for i in goalword:
            if letterguess == i:
                letterblanks = letterblanks.strip()
                letterblanks = letterblanks[:letter - 1] + str(letterguess) + letterblanks[letter:]
                letterblanks = letterspaces + letterblanks + letterspaces
                correctletter = True
            letter += 2
        if correctletter == False:
            if len(letterguess) == 1:
                wrongletters.append(letterguess)
                wrongguesses += 1
            if wrongguesses == 1:
                gameboard[3] = "    .( )....|..    "
            if wrongguesses == 2:
                gameboard[4] = "    ..|.....|..    "
            if wrongguesses == 3:
                gameboard[5] = "    ./......|..    "
            if wrongguesses == 4:
                gameboard[5] = r"    ./.\....|..    "
            if wrongguesses == 5:
                gameboard[4] = "    .-|.....|..    "
            if wrongguesses == 6:
                gameboard[4] = "    .-|-....|..    "
                printboard()
                print ("\nGame over, you lose. The correct word was %s." % (goalword))
                break
        elif correctletter == True:
            correctguesses.append(letterguess)
        gameboard[8] = letterblanks

        donewithword = False
        for i in letterblanks:
            if i == "_":
                donewithword = False
                break
            else:
                donewithword = True
        printboard()
        if donewithword == True:
            print ("\nCongrats, you win!")
            printboard()
            break
    playagainq = (input("\nDo you want to play again? "))
    playagainq = playagainq.lower()
    if playagainq == "y" or playagainq == "y" or playagainq == "y":
        print ("")
        playagain = True
    else:
        print ("\nOkay, see you later!")
        playagain = False