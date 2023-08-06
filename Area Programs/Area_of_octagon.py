"""The area of octagon formula is Area=2*(1+sqrt(2))*side**2
"""
from math import sqrt
side=(int(input("Enter the side of octagon:- ")))
Area=2*(1+sqrt(2))*side**2
print("{0:.2f}".format(Area))

