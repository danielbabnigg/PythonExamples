print ("""
Welcome, enter your element below.""")
element = (input())

if (element == "Hydrogen" or element == "H"):
    a = "Hydrogen (H)"
    b = "Nonmetal"
    c = "Gas"
    d = "1.008"
elif (element == "Helium" or element == "He"):
    a = "Helium (He)"
    b = "Noble Gas"
    c = "Gas"
    d = "4.0026"
elif (element == "Lithium" or element == "Li"):
    a = "Lithium (Li)"
    b = "Alkali Metal"
    c = "Solid"
    d = "6.94"
elif (element == "Beryllium" or element == "Be"):
    a = "Beryllium (Be)"
    b = "Alkaline Earth Metals"
    c = "Solid"
    d = "9.0122"
elif (element == "Boron" or element == "B"):
    a = "Boron (B)"
    b = "Metalloid"
    c = "Solid"
    d = "10.81"
elif (element == "Carbon" or element == "C"):
    a = "Carbon (C)"
    b = "Nonmetal"
    c = "Solid"
    d = "12.011"
elif (element == "Nitrogen" or element == "N"):
    a = "Nitrogen (N)"
    b = "Nonmetal"
    c = "Gas"
    d = "14.007"
elif (element == "Oxygen" or element == "O"):
    a = "Oxygen (O)"
    b = "Nonmetal"
    c = "Gas"
    d = "15.999"
elif (element == "Fluorine" or element == "F"):
    a = "Flourine (F)"
    b = "Nonmetal"
    c = "Gas"
    d = "18.998"
elif (element == "Neon" or element == "Ne"):
    a = "Neon (Ne)"
    b = "Noble Gas"
    c = "Gas"
    d = "20.180"
else:
    print ("Invalid Element"())

print("""
Element: %s
Type: %s
State of Matter: %s
Atomic Mass: %s""" % (a, b, c, d))