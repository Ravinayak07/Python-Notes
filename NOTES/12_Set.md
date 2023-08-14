# SETS:

- written with curly braces

```py
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

> PROPERTIES:

```
- Unordered
- Unchangeable (but can add and remove items)
- unindexed
- Doesnot allow duplicates
```

- Unoredred: Items doesnot appear in a spcified manner. Every time appear in a different way:

```
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

- Unchangeable means: inidividual items can't be changed but removed or added
- unindexed

```py
fruits = {"apple", "banana", "cherry"}
print(fruits[0])
```

- duplicates not allowed:

```py
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'banana', 'apple', 'cherry'}
```

```py
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) # {True, 2, 'banana', 'cherry', 'apple'}

```

- The values True and 1 are considered the same value in sets, and are treated as duplicates:

# Length:

```py
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
```

# Items can be of different data types;

```py
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
```

```py
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))
```

```
{'banana', 'apple', 'cherry'}
<class 'set'>
```

- Mixed data type:

```py
set1 = {"abc", 34, True, 40, "male"}

print(set1)

```

# The set() Constructor

- It is also possible to use the set() constructor to make a set.

```py
thisset = set({"apple", "banana", "cherry"})
print(thisset)
```

- both brackets can be used

```py
thisset = set(("apple", "banana", "cherry"))
print(thisset)
```

# ACCESS ITEMS:

- You cannot access items in a set by referring to an index or a key.
- we can loop and ask

```py
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

```py
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

# ADD ITEMS:

- .add() method:

```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```

- ERROR: Takes only one argument:

```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange","kanw")

print(thisset)

```

# HOW TO ADD TWO SETS:

- update() method:

```py
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

```

# HOW TO ADD TUPLE OR LIST TO A SET:

- using update() function:

```py
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

```

- what will be result?? set

# HOW TO REMOVE SET ITEMS:

- remove() method

```py
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

```

- Note: If the item to remove does not exist, remove() will raise an error.

> discrad() method:

```py
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

```

Note: If the item to remove does not exist, discard() will NOT raise an error.

## pop() method:

- You can also use the pop() method to remove an item
- but this method will remove a random item, so you cannot be sure what item that gets removed.
- The return value of the pop() method is the removed item.

> Question: create a set and remove any item using pop function:

```py
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal
```

- Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

## EMPTY THE SET:

- using clear

```py
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

```

## DELETE THE SET:

```py
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
```

# JOIN SETS:

> 1. Method1: union()

- returns a new set containing all items from both sets

```py
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

```

> 2 . update() method

- that inserts all the items from one set into another:

```py
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
```

- Note: Both union() and update() will exclude any duplicate items.

# HOW TO STORE THE COMMON ITEMS FROM TWO SETS:

- The intersection() method will return a new set, that only contains the items that are present in both sets.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
```

- The intersection_update() method will keep only the items that are present in both sets.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

```

## KEEP ALL ITEMS EXCEPT THE DUPLICATES:

- The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
```

- The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

```py
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
```
