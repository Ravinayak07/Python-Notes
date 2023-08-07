"""The area of pentagon formula is Area=(5/2)*s*a
      or Area=(sqrt(5*(5+2*sqrt(5)*side**2))/4)
   where s=side of pentagon
         a=apothem length(length from the centre of the pentagon to the mid point of one of
         its side
"""
from math import sqrt
side=(int(input("Enter the side of pentagon:- ")))
a=(int(input("Enter the apothem length of pentagon:- ")))
Area=(sqrt(5*(5+2*sqrt(5)*side**2))/4)
print("{0:.2f}".format(Area))
Area=(5/2)*side*a
print(Area)