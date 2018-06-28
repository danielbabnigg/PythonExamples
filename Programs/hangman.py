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
    goalword = random.choice(("aardvark", "account", "add", "addition", "addiction", "adult", "adventure", "afro", "aged", "again", "aid", "aims", 
    "always", "albino", "and", "aunt", "ant", "apes", "apply", "aqueous", "artwork", "armies", "around", "arrows", "asterisk", "ate", "aurora", 
    "available", "avoid", "awe", "axis", "barefoot", "barely", "barista", "barns", "bars", "babies", "bakery", "best", "bet", "bends", "bears", 
    "beans", "been", "below", "bees", "bells", "biggest", "bills", "bias", "bisque", "biology", "bin", "bleeding", "bloated", "black", "bless",
    "body", "boar", "boulder", "boards", "bowling", "bows", "brown", "browse", "bronze", "bread", "building", "bulls", "buds", "call", "calling", 
    "cause", "can", "cars", "cannon", "cake", "cells", "chill", "charred", "cherry", "cheese", "chokes", "chalk", "circle", "close", "clean",
    "clasps", "clears", "closely", "cope", "coarse", "cotton", "cross", "crows", "crops", "crane", "crawfish", "curry", "cubes", "cyan", "dark",
    "dares", "date", "days", "deadly", "delicious", "decrease", "deer", "defined", "diligent", "dill", "dial", "document", "dolphin", "dread",
    "drown", "drawing", "drain", "droids", "droplets", "dual", "dull", "duckling", "ears", "eat", "ecology", "education", "efficient", "eggs",
    "ego", "elephant", "elk", "enter", "enough", "enable", "epic", "equal", "equality", "error", "erosion", "escalate", "every", "extra", "eyes",
    "far", "fairy", "fair", "factual", "fast", "fears", "ferry", "feel", "fill", "figs", "float", "flee", "flawless", "floor", "foggy", "for",
    "free", "frail", "from", "future", "funny", "fumes", "full", "fuss", "games", "gaps", "gas", "get", "gears", "gel", "geography", "ghost",
    "gills", "girls", "glory", "glamorous", "glean", "glossy", "gnome", "gnarly", "gore", "goats", "goes", "grape", "grasp", "halves", "have",
    "hall", "heading", "heads", "heroes", "heaps", "hearing", "hills", "hit", "hopes", "hoax", "hoses", "horses", "hook", "holes", "hug", "hyena",
    "icy", "ideal", "idol", "identity", "ill", "imagine", "image", "integer", "inner", "input", "instantly", "instant", "italics", "ivy", "jars",
    "jaws", "jade", "jets", "jingle", "jolly", "jungle", "jury", "jumping", "juices", "just", "kettle", "keys", "kiss", "kind", "kiwi", "knowing",
    "knack", "knot", "lame", "lambs", "lastly", "ladder", "leaves", "leading", "lead", "learning", "leap", "lesson", "light", "liability", "lies",
    "lists", "lick", "loop", "load", "loose", "logs", "luster", "made", "malls", "married", "mapping", "mass", "maybe", "message", "messy", "met",
    "meat", "meal", "melon", "meaning", "men", "milk", "missing", "mill", "middle", "minute", "microphone", "more", "money", "mossy", "module",
    "mopping", "much", "muddy", "must", "muffle", "mugs", "mystery", "name", "narrow", "navy", "never", "neptune", "near", "needs", "nine", "nope",
    "none", "nods", "oats", "oars", "oasis", "object", "odd", "off", "often", "ogre", "omelette", "opera", "operation", "opposite", "oppose",
    "opening", "ores", "oxen", "patience", "papers", "pairs", "pages", "passing", "peach", "pears", "perfect", "peel", "pills", "pies", "picture",
    "pipeline", "pidgin", "picking", "please", "plus", "plots", "plans", "poach", "positive", "pools", "possible", "prey", "proper", "prance",
    "previous", "punch", "puff", "pull", "python", "queue", "query", "questions", "quest", "quill", "rains", "rapping", "raspberry", "radical",
    "really", "real", "resolution", "reef", "reputation", "rhino", "right", "ridge", "risky", "rookie", "roaring", "roses", "rooftop", "rugs",
    "ruins", "rusty", "sand", "safe", "sadly", "safari", "sapling", "screen", "scary", "scope", "self", "sealing", "second", "segment", "seven",
    "should", "showing", "single", "sister", "sick", "slowly", "slate", "smear", "smart", "smoke", "snakes", "snowing", "soon", "soaps", "soft",
    "solidify", "soccer", "spring", "spare", "space", "spikes", "sport", "state", "stars", "stop", "stage", "stall", "staff", "steep", "stack",
    "summer", "sunscreen", "sustain", "supper", "swear", "tall", "talking", "tails", "tapping", "tavern", "take", "tanning", "tears", "tea",
    "thing", "thank", "thorns", "thesis", "tinker", "tip", "total", "toads", "totally", "toss", "topping", "toes", "tore", "tollway", "toast",
    "treasure", "treat", "trees", "troops", "track", "trash", "trains", "tubs", "tunnel", "tuck", "twins", "tweet", "under", "unlikely", "unable",
    "undefined", "unprepared", "units", "upper", "upset", "upload", "users", "usual", "useless", "utility", "vacation", "vacant", "valley",
    "vans", "vaccum", "vary", "versus", "vessel", "verbs", "villain", "visable", "viking", "video", "visual", "vulture", "walls", "wars", "waffle",
    "wake", "waves", "well", "wear", "weapon", "west", "while", "whales", "willing", "winking", "wick", "words", "works", "worse", "wool", "write",
    "xylophone", "yams", "yards", "yelling", "yellow", "years", "yoyo", "zebra", "zero"))
    
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
    if playagainq == "yes" or playagainq == "ye" or playagainq == "y":
        print ("")
        playagain = True
    else:
        print ("\nOkay, see you later!")
        playagain = False