# Find the square root of first 100 numbers
# 1)take loop of 100 numbers
# 2) take each number and find square root 
# 3)assign result to a variable & print the value

from math import *

for x in range(1,101):
    print(round(sqrt(x),3))
    # format method
    print("{:.3f}".format(sqrt(x)))
    # f-string
    print(f"{sqrt(x):.3f}")