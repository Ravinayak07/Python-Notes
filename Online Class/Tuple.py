# Tuples:

# properties of a tuple:
# 1. ordered
# 2. Unchangeable
# 3. Allow Duplicates

# [] : list
# () : tuples

season = ("summers","rainy","winter","spring")
print(season)

# how to access each item of a tuple
print(season[2])

# calculate the length of a tuple?
length = len(season)
print(length)

# print the type of a tuple

print(type(season))

numbers = (1,2,3,4,5)
print(type(numbers))

decision = (True, False, True)
print(type(decision))

mixed  = ("ravi",1,True,1)
print(type(mixed))  #output

# How to create a tuple of one item ??
season = ("summers",)
print(type(season))


# Another way of creating a tuple using tuple() constructor.
              #      0        1       2        3
season2 = tuple(("summers","rainy","winter","spring"))
              #     -4       -3      -2       -1
print(season2)

# Negative Indexing in Tuple

# print 2nd item of season2 using negative indexing:
print(season2[-3])

# for printing range of items:
# print 2nd item to 3rd item using negative indexing:
print(season2[-1:-4:-1])

# create a tuple and print its items using loop.
season2 = tuple(("summers","rainy","winter","spring"))
for i in season2:
    print(i)

print("-------------------")
# do the same thing using range() function:
for i in range(len(season2)):
    print(season2[i])

# Check whether a item is present in the tuple or not ??
item = "summers"

if item in season2:
    print("Present")
else:
    print("Not present")


# Tuples are unchangeable:
# How to change items?? add or remove ??

# convert first into list...then change items and then convert back to tuple

# create a tuple of string values and update the 2nd item:
cities = ("Delhi","Mumbai","Pune")
print(cities)
mylist = list(cities)
mylist[1] = "Bhubaneswar"
cities = tuple(mylist)
print(cities)

# How to append in tuple ???
cities = ("Delhi","Mumbai","Pune")
print(cities)
mylist = list(cities)
mylist.append("Bhubaneswar")
cities = tuple(mylist)
print(cities)

# By using + operator:
newTuple = ("Chennai",)
cities = cities + newTuple
print(cities)

# How to remove items from tuple???
cities = ("Delhi","Bhubaneswar","Mumbai","Pune")
print(cities)
mylist = list(cities)
mylist.remove("Bhubaneswar")
cities = tuple(mylist)
print(cities)

# how to remove all items from a list ???
# del keyword:
 # ()


# print empty tuple

cities = ("Delhi","Bhubaneswar","Mumbai","Pune") # packing 
print(cities)
mylist = list(cities)
mylist.clear()
cities = tuple(mylist)
print(cities)


# Packing a Tuple?
# means asiigning values to a tuple
cities = ("Delhi","Bhubaneswar","Mumbai","Pune") # packing
print(cities)

# Unpacking a tuple ??
# means extracting the values back into variables
cities = ("Delhi","Bhubaneswar","Mumbai","Pune")
(x,y,z,a) = cities
print(x)
print(y)
print(z)
print(a)

# In unpacking , no.of variables = no. of values in tuple

# In case, if there less no. of variables than the values
progLang = ("Java","CPP","Python","Javascript")
(x,y,*z) = progLang
print(x) # java
print(y) # CPP
print(*z) # Python","Javascript"

progLang = ("Java","CPP","Python","Javascript","swift","kotlin")
(x,*y,z,a) = progLang
print(x) 
print(y) 
print(z)
print(a)

# Join Tuples:
numbers = (1,2,3,4,5)
letters = ('a','b','c','d')
newTuple = numbers+letters
print(newTuple)

# How to multiple the content of a tuple

progLang = ("Java", "CPP")
progLang = progLang * 0
print(progLang)
#output : ("Java", "CPP","Java", "CPP")


# Tuple Methods:

# index() : first occurance of specified item
progLang = ("Java", "CPP","Python","Java")
print(progLang.index("Java")) # 0

# print(progLang.index("javascript")) # Error

# SORTING A TUPLE:
# since tuples are immutable, we cannot directly sort the elements like we did in list

myTuple = (4,8,1,0,5,6,5)
print(myTuple)
mylist = list(myTuple)
mylist.sort()
myTuple = tuple(mylist)
print(myTuple)
print("-----------------")
# Without converting into list ???
# sorted() function:
# built-in used to sort a tuple
# sorts by default in ascending order and returns a new sorted sequence

myTuple = (4,8,1,0,5,6,5)
print(myTuple)
newTuple = tuple(sorted(myTuple))
print(newTuple)

"""
## Diff between sort() and sorted() function:

# sort():
- mutable sequqnces
- modifies original list without creating a new one
- has no return value because it sorts and updates directly

# sorted():
- can be usedwith any iterables(list, tuple,etc)
- doesnot modify the original sequnece
- returns a new sorted list
"""
fruits = ["Apple","Orange","Mango"]
print(fruits)
fruits.sort()# None
print(fruits)
"""

fruits = ["Apple","Orange","Mango"]
print(fruits)
print(sorted(fruits))
print(fruits)
"""
print("-----------------")
fruits = ["Apple","Orange","Mango"]
print(fruits)
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(fruits)



