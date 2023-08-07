"""The area of hexagon formula is Area=(7*side**2*cot(180/7))/7
"""
import sympy
side=(int(input("Enter the side of heptagon:- ")))
Area=(7*side**2*sympy.cot(180/7))/7
print("{0:.2f}".format(Area))

