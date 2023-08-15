# program to sort a list of tuples using multiple criteria
"""
INPUT:
list : [("Java",2), ("Python",0"), ("apple",2),("cpp",3)]

OUTPUT: 
"""

listOfTuples = [("java",2), ("python",0), ("apple",2),("cpp",3)]

def customSort(y):
    return y[1], y[0]

def sorting(x):
    return sorted(x, key = customSort)

print(sorting(listOfTuples))