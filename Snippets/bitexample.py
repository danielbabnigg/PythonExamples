#basic bit numbers
print (0b1)
print (0b1010)
print (0b11)

#converting number to bit
print (bin(102))
print (bin(14274))

#using int to convert from bit to number
print (int("1001011101", 2))
print (int(bin(5), 2))

#shifts in bitwise operations
shift1 = 0b100
shift2 = 0b1
shift1 = shift1 >> 2
shift2 = shift2 << 3
print (bin(shift1))
print (bin(shift2))

#and operator in bitwise operations
print (bin(0b101010 & 0b111000))

#or operator in bitwise operations
print (bin(0b1 | 0b100))

#xor operator in bitwise operations
print (bin(0b101 ^ 0b111))

#not operator
print (~1)
print (~100)