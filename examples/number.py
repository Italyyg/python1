# accessing many more math functions via python,not currently in this prgm
from math import *


# You can print whole number, negative number, decimals, as well as simple 
# equations like adding, subtracting, multiplication, and division
print(2.05)

print(3*(4+5))

# ten divided by 3 but return the remainder
print(10 % 3)

# you can also use vatiables to hold your number
my_num = 5
print(my_num)

# Maybe you wat to conver your number into a string
print(str(my_num) + " my favorite number")
# you will get a error if you try and print a number next to a string

# getting absolute values from numbers
mi_num = -5
print(abs(mi_num))

# squaring a number, 3 to the power of 2
print(pow(3,2))

# returns the bigger number
print(max(4,6))
# returns the smallers number
print(min(3,9))

# rounds the number to the closet
print(round(3.7))
print(round(3.4))

# (when imported) this will round to the lowest
print(floor(3.7))

#(when imported) wil round up
print(ceil(3.7))

# (when imported) squareroots a number
print(sqrt(36))