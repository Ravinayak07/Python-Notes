# Tuples:

- used to store multiple items in a single variable.
- created using round brackets
- EX:

```py
season = ("summer","rainy","winter","spring","Autumn")
print(season)  #('summer', 'rainy', 'winter', 'spring', 'Autumn')
```

- Tuple items are ordered, unchangeable , can have duplicates
- Tuple Items are indexed. So it can be accessed using indexes.

```
- Ordered means tuple items have a defined order that will not change
- Unchangeable means tuple items cannot be added or removed after it has been created.
- Duplicates means can have items with same value.
```

```py
season = ("summer","rainy","winter","spring","summer")
print(season)  #('summer', 'rainy', 'winter', 'spring', 'Autumn')
```

> Tuple Length:

```py
seasons = ('summer', 'rainy', 'winter', 'spring', 'summer')
print(len(seasons)) #5
```

> How to create tuplw with one Item:

- Need to add comma after the item otherwise python will not recognise it as a tuple

```py
season = ("summer",)
print(type(season)) # <class 'tuple'>

# Not a tuple
season = ("summer")
print(type(season)) # <class 'str'>

```

> Tuples can have items of any data types

- tuples are defined as objects with the data type 'tuple':

```py
colors = ("red","blue","green")
numbers = (1,2,3,4,5)
decision = (True, False, False)

print(type(colors)) # <class 'tuple'>
print(type(numbers))  # <class 'tuple'>
print(type(decision))  # <class 'tuple'>
```

- It can also have mixed data types:

```py
tuple = ("red",12,"blue",8.9,True)
print(tuple) # ('red', 12, 'blue', 8.9, True)
print(type(tuple)) # <class 'tuple'>
```

> Also can create tuple using tuple() Constructor

```py
seasons = tuple(("summer","rainy","winter","Autumn"))
print(seasons)
```

> ACCESS TUPLES:

- by refering the index number.

```py
seasons = tuple(("summer","rainy","winter","Autumn"))
print(seasons[2]) # winter
```

> Negative Indexing:

```py
seasons = tuple(("summer","rainy","winter","Autumn"))
print(seasons[-2]) #winter
```

- Range of Negative indexes. Starting index included. Ending index excluded

```py
seasons = ("summer","rainy","winter","Autumn")
print(seasons[-3:-1])  # ('rainy', 'winter')
```

> Check If Item Exists in Tuple:

```py
seasons = ("summer","rainy","winter","Autumn")
if "summer" in seasons:
  print("YES")
```

> Changing Tuple Values:

- Since Tuples are unchangeable, we cannot add or remove items
- But we can convert tuple into list,change list and then convert back to tuple.

```py
cities = ("Delhi","Mumbai","Pune")
list1 = list(cities)
liat1[1] = "Chennai"
cities = tuple(list1)

print(cities)  # ('Delhi', 'Chennai', 'Pune')
```

- Since tuples are immutable, they don't have built-in append() function
- There are other ways to add item to tuple:

```py
# By converting to list
cities = ("Delhi","Mumbai","Pune")
list1 = list(cities)
liat1.append("Chennai")
cities = tuple(list1)

print(cities)  # ('Delhi', 'Mumbai', 'Pune', 'Chennai')
```

- We can add tuples to tuples. So creating a tuple of one item and then adding to another tuple

```py
# By adding tuple to a tuple:
cities = ("Delhi","Mumbai","Pune")
new = ("Bhubaneswar",)
cities += new
print(cities) #('Delhi', 'Mumbai', 'Pune', 'Bhubaneswar')

```

> Remove Items

- To remove items, we can convert the tuple to list and then remove items and convert back to tuple

```py
cities = ("Delhi","Mumbai","Pune","Bhubaneswar")
print(cities) # ('Delhi', 'Mumbai', 'Pune', 'Bhubaneswar')
cities = list(cities)
cities.remove("Pune")
cities = tuple(cities)
print(cities) # ('Delhi', 'Mumbai', 'Bhubaneswar')

```

- We can delete tuple completely

```py
cities = ("Delhi","Mumbai","Pune","Bhubaneswar")
del cities
print(cities) #Error
```

> Packing and Unpacking a tuple

- Packing means assigning values to a tuple variable

```py
fruits = ("apple", "banana", "mango")

print(fruits)
```

- Unpacking means extracting values back into variables.

```py
fruits = ("apple", "banana", "mango")
print(fruits)

(x,y,z) = fruits

print(x)
print(y)
print(z)
```

- In unpacking the number of variables must match the number of values in list

> Using Asterisk(\*):

- If no. of variables < no. of values, we can add \* to the variable name and all the values will be assigned to the variable as a list.

```py
progLang = ("Java","CPP","Python","Javascript","Swift","Kotlin")
(x,y,*z) = progLang
print(x)
print(y)
print(z)
```

```
Java
CPP
['Python', 'Javascript', 'Swift', 'Kotlin']
```

```py
progLang = ("Java","CPP","Python","Javascript","Swift","Kotlin")
(x,*y,z,a) = progLang
print(x)
print(y)
print(z)
print(a)
```

```
Java
['CPP', 'Python', 'Javascript']
Swift
Kotlin
```

## Looping over a Tuple:

- For Loop

```py
progLang = ("Java","CPP","Python","Javascript","Swift","Kotlin")
for x in tuple:
  print(x)
```

- using range function

````py
```py
progLang = ("Java","CPP","Python","Javascript","Swift","Kotlin")

for i in range(len(progLang)):
  print(progLang[i])
````

- While Loop:

```py
progLang = ("Java","CPP","Python","Javascript","Swift","Kotlin")
i=0
while i < len(progLang):
  print(progLang[i])
  i=i+1
```

## JOIN TUPLES:

- Join two or more tuples using + operator

```py
vowels = ('a','e','i','o','u')
prime = (2,3,5,7,11)

newTuple = vowels + prime

print(newTuple)
```

- we can multiple the content of tuple using \*

```py
progLang = ("Java","CPP")
newTuple = progLang * 3
print(newTuple) # 'Java', 'CPP', 'Java', 'CPP', 'Java', 'CPP')
```

```py
progLang = ("Java","CPP")
newTuple = progLang * 0
print(newTuple) # ()
```

## Tuple Methods:

> 1 . count():

- returns the number of times a item occurs in a tuple:

```py
progLang = ("Java","CPP","Python","Java")
x = progLang.count("Java")
print(x)  # 2
```

> 2 . index():

- return the index of first occurance of the specified item
- raises an exception if the value is not found.

```py
progLang = ("Java","CPP","Python","Java")
x = progLang.index("Java")
print(x)  # 2
```

## SORTING A TUPLE:

- Since Tuples are immutable, we cannot directly sort the elements as we did in list
- So there are two methods:

> 1 . Convert to list:

```py
myTuple = (4,8,1,0,4,6,3)
print(myTuple)
mylist = list(myTuple)
mylist.sort()
myTuple = tuple(mylist)
print(myTuple)
```

```
(4, 8, 1, 0, 4, 6, 3)
(0, 1, 3, 4, 4, 6, 8)
```

> 2 . using sorted() function

- It is built-in function to sort a Tuple
- It sorts by default in ascending order and returns a new sorted list.

```py
myTuple = (4,8,1,0,4,6,3)

# returns a new sorted list
print(sorted(myTuple))  #[0, 1, 3, 4, 4, 6, 8]

# original tuple is not changes
print(myTuple)   # (4, 8, 1, 0, 4, 6, 3)

# storing in a alist
mylist = sorted(myTuple)
myTuple = tuple(mylist)
print(myTuple)  # (0, 1, 3, 4, 4, 6, 8)
```

## Diff between sort() and sorted() fun

> sort():

- available for mutable sequence types
- It modifies the original list without creating a new list
- has no return value. It sorts the list and updates it directly

> sorted():

- can be used with any iterables(lists, tuples, strings, etc)
- It doesnot modfifies the original sequence
- returns a new sorted list/sequence

```py
fruits = ["Apple","Orange","Mango"]
print(fruits.sort()) # None
print(sorted(fruits)) # ['Apple', 'Mango', 'Orange']
```

# PROGRAMS:

## Program to create a list of tuples containing first 10 Natural numbers

```
[(1,2),(3,4),(5,6),(7,8),(9,10)]
```

```py
myTuple = ()
mylist = []
for i in range(1,10):
  myTuple = (i,i+1)
  mylist.append(myTuple)
  i=i+2

print(mylist)
```

## Python program to create a list of tuples from a given list where each tuple will have the number and its cube

```
Input list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]
```

```py
num = int(input("Enter the number of elements : "))
myList = []
for i in range(num):
  item = int(input("Enter element : "))
  myList.append(item)

myTuple=()
newList=[]
for i in myList:
  myTuple = (i,i**3)
  newList.append(myTuple)

print(newList)
```
