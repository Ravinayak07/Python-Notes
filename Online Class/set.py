# SETS:
# written using curly braces
# Properties of set:
# 1. Unordered
# 2. Unchangeable
# 3. Doesnot allow duplicates
# 4. unindexed

# 1. Unordered: doesnot appear in a specified order

progLang = {"Java","Python","CPP"}
print(progLang)

# 2. Unchangeable: Individual items can't be changed but we can add or remove items

# 3. Unindexed: we can't access items using index number
 
# print(progLang[0]) # Error

# 4. Duplicates are not allowed.
progLang = {"Java","Python","CPP","Python"}
print(progLang)

# Length: using len()
print(len(progLang))


# Set items can also of different data types:
fruits = {"mango","apple","banana"}
numbers = {1,3,4,5,6}
decision = {True, False, True}
print("Length of Decision: ")
print(len(decision))

print(fruits)
print(numbers)
print(decision)

print(type(fruits))
print(type(numbers))
print(type(decision))

# Set can also store mixed data types:
newSet = {"Mango",10, True, 11}
print(newSet)
print(type(newSet))

set2 = {"Java", "Python", "java", 11, 10, 1, True}
print(set2)
print(len(set2))


# set() Constructor:
mySet = set(("Java","Python","CPP"))
print(mySet)

# ACCESSING ITEMS OF A SET:
# we cannot access items in a set by reffering index
# Loop:

set2 = {"Java", "Python", "java", 11, 10, 1, True}

for x in set2:
    print(x)
    
print( "Java" in set2)


# Set is Unchangeable but we can or remove items of sets

# HOW TO ADD ??

# using  add() method:

set3 = {"Java", "Python", "java", 11, 10, 1, True}
print(set3)
set3.add("CPP")
print(set3)


# update method():
newSet1 = {"Java", "Python", "java"}
newSet2 = {11, 10, 1, True}

newSet1.update(newSet2)

print(newSet1)
print(newSet2)

# HOW TO REMOVE SET ITEMS ?

# remove() function:

newSet1 = {"Java", "Python", "java"}
newSet1.remove("Java")
print(newSet1)

# discard() function:
newSet2 = {"Java", "Python", "java"}
newSet2.discard("CPP") 
print(newSet2)

# pop() method:
# Since sets are unordered and unindexed, pop() method randomly removes any item of the set.

newSet3 = {"CPP", "Python", "java"}
value  = newSet3.pop()

print(newSet3)
print(value)


# HOW TO DETELE THE SET ?

set4 = {"CPP", "Python", "java"}

del set4
# print(set4)

# using clear() function:

set5 = {"CPP", "Python", "java"}
set5.clear()

print(set5)

# JOIN THE SETS:
# using union method:

setLetters = {"r", "a","v","i"}
setNumbers = {1,2,3}

combinedSet = setLetters.union(setNumbers)
print(combinedSet)
print("---------------")
# using update method:

setLetters2 = {"r", "a","v","i",0}
setNumbers2 = {1,2,3}

combinedSet2 = setLetters2.union(setNumbers2)
print(combinedSet2)


# HOW TO STORE THE COMMON ITEMS FROM TWO DIFFERENT SETS:

# using intersection() method:
set5 = {"Java","Python","CPP"}
set6 = {"Java","C","Javascript"}

newIntersectionSet = set5.intersection(set6)

print(newIntersectionSet)

# using intersection_update():

set7 = {"Java","Python","CPP"}
set8 = {"Java","C","Javascript"}

print("Set7 : ",set7)

set7.intersection_update(set8)

print("Set7 : ",set7)

# To Store All items other than the duplicate ones:
# symmetric_difference():
# it returns a new Set that contains the elements that are not present in both sets

set9 = {"apple","Mango","Orange"}
set10 = {"apple", "Java","Python"}

newSet6 = set9.symmetric_difference(set10)

print(newSet6)  # output ???
print("---------------------------")
# Using symmetric_difference_update():

set10 = {"apple","Mango","Orange"}
set11 = {"apple", "Java","Python"}

print(set11)
set10.symmetric_difference_update(set11)
print(set10)













