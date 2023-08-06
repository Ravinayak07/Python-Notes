"""The area of hexagon formula is Area=(3*sqrt(3)*side**2)/2
"""
from math import sqrt
side=(int(input("Enter the side of hexagon:- ")))
Area=(3*sqrt(3)*side**2)/2
print("{0:.2f}".format(Area))
