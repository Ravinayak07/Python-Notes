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

# Dictionary

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
