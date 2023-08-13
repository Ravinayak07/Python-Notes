## Collection data Types

- There are 4 built-in data types in Python to store collection of data:
- 1 . Lists: Ordered, Mutable, Allows Duplicate
- 2 . Tuple: Ordered, Unmutable, Allows Duplicate
- 3 . Set: Unordered, Unchangeable(but items can be removed or add), Unindexed, No Duplicate
- 4 . Dictionary: Ordered(in Python version 3.7 but unordered in version 3.6 and earlier ), changeable, No duplicate

# Python Lists:

- used to store multiple items in a variable
- created using square brackets.
- Ex:

```py
iplTeams = ["CSK", "MI", "RCB"];
print(iplTeams);
```

- list items ordered, mutable, can have duplicate values.
- First item of list has index 0.

> Ordered:

- List items have defined order
- Order will not change
- New elements are placed st the end.
- Note: Some list methods changes the order:

> Mutable:

- we can change, add and remove items in a list

> Allow Duplicates:

- List can have duplicate values
- EX:

```py
iplTeams = ["CSK", "MI", "RCB", "CSK"]
print(iplTeams) #['CSK', 'MI', 'RCB', 'CSK']
```

> List Length:

- len() fun is used to find the number of items in a list
- Ex:

```py
colors = ["Yellow", "Blue", "Red"]
print(len(colors)) # 3
```

> Data Types of List Items

- List Items can be of any data type
- Ex:

```py
fruits = ["apple", "orange","Guava"] #string type
numbers = [1,2,4,5] # Integer Type
decision = [True, False, True] # Boolean Type

print(fruits) # ['apple', 'orange', 'Guava']
print(numbers) # [1, 2, 4, 5]
print(decision) # [True, False, True]
```

- List items can be of different data types:
- Ex:

```py
myList = ["Ravi", 22, True, "BBSR"]
print(myList);
```

> type():

- List are defined as objects with the data type list

```py
myList = ["Mercury","Venus", "Earth","Mars"];
print(type(myList));  # <class 'list'>
```

> list() constructor:

- used to create new list
- Ex:

```py
myList = list(("apple", "orange", "Banana"));
print(myList) # ['apple', 'orange', 'Banana']
```

> ACCESS ITEMS:

- Since list are indexed, its items can be accessed using index
- EX:

```py
colors = ["blue","red","Green"]
print(colors[1]) #red
```

- Negative indexing means start from end.
- -1 refers to last item.

```py
colors = ["blue","red","Green"]
print(colors[-2]); #red
```

> Range of Indexes:

- Specify start index(included) and where to end(not included).
- Return value is new list with specified items.
- EX:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[1:4]) # ['blue', 'green', 'yellow']
```

- If start index is not mentioned, range will start from first item

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[:4]); # ['red', 'blue', 'green', 'yellow']
```

- If the end index is not mentioned, range will start go on to the end of the list:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[2:]); #['green', 'yellow', 'orange', 'violet']
```

> Range of Negative Indexes

- EX:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[-4:-1]); #['green', 'yellow', 'orange']
```

> CHheck if Item Exists:

- Use **in** keyword

```py
color = ["red", "blue", "green"]
if "green" in color:
    print("Yes")
```

> Change Item Value:

- Refer Index Value:

```py
# create a list, modify any item value and print the new list

progLang = ["Java","C","CPP"]
print(progLang)

# changinng 2nd item:
progLang[1] = "Python"

print(progLang)
```

```
['Java', 'C', 'CPP']
['Java', 'Python', 'CPP']
```

> Changing Item Values within a Range:

- Question: create a of list 5 items and then replace a range of list items between index 2 and 4(not included).
- Ans:

```py
# creating a list of 5 items
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

# inserting items between index 2 and 4
progLang[2:4] = ["HTML","CSS"]

print(progLang)

```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'HTML', 'CSS', 'Javascript', 'Kotlin']
```

- If you insert more than you replace, new items will added and remaining items will be moved.

```py
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

#replacing only 2nd index(3 is not counted) with two items
progLang[2:3] = ["HTML","CSS"]

print(progLang)
```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'HTML', 'CSS', 'CPP', 'Javascript', 'Kotlin']
```

- In this case the length of list changes when no. of items inserted does not match the no. of items replaced.

- Now, inserting less than replace:

```py
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

progLang[3:6] = ["HTML"]

print(progLang)
```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'Python', 'HTML']
```

## Insert List Items:

- How to insert list items without replacing
- using insert() fun:
- It inserts items at the mentioned index.

```
Question: Create a list of 4 items and insert a new item at index 3
```

```py
colors = ["Red", "Blue" ,"Green","Black"]
print(colors)
colors.insert(3, "Orange")
print(colors)
```

```
['Red', 'Blue', 'Green', 'Black']
['Red', 'Blue', 'Green', 'Orange', 'Black']
```

## Append List Items:

- what is append() methods
- to add an item at the end of the list

```py
color = ["red","blue","green"]
print(colors)
colors.append("black")
print(colors)
```

```
['red', 'blue', 'green']
['red', 'blue', 'green', 'black']
```

## Extend List Items:

- what is extend() method used for?
- used to append or add items of another list to the end of current list

```py
colors = ["yellow","purple","green"]
rgb = ["red","blue","green"]
colors.extend(rgb)
print(colors)
```

```
['yellow', 'purple', 'green', 'red', 'blue', 'green']
```

- Extend can append any iterable object(list, tuples, set, dictionaries, etc).

```py
#extending tuple with list
colors = ["yellow","purple","green"]
rgb = ("red","blue","green")
colors.extend(rgb)
print(colors)
```

## Looping Through a List:

> For Loop:

```
 Print all list items using for loop:
```

```py
myList = [1,2,3,4]
for x in myList:
  print(x)
```

```
1
2
3
4
```

```
print  all list items using for loop by refering index number:
```

```py
cities = ["Delhi", "Mumbai", "Pune"]
length = len(cities)
for i in range(length):
  print(cities[i])
```

```
Delhi
Mumbai
Pune
```

> Using While Loop:

```
print all list items using while loop
```

```py
cities = ["Delhi","Mumbai","Pune"]
i = 0
length = len(cities)
while i < length:
  print(cities[i])
  i = i+1
```

# Sorting the Lists:

- sort(): built-in fun to sort list in ascending by default:

```py
#sorts alphabetically
colors = ["red", "blue", "green","yellow","orange"]
colors.sort()
print(colors)
```

```py
#sorts numerically
thislist = [80, 10, 30, 50, 60]
thislist.sort()
print(thislist)
```

- For Sorting in descending, use the keyword argument **reverse = True**

```py
#Sort in descending
colors = ["red", "blue", "green","yellow","orange"]
colors.sort(reverse=True)
print(colors) # ['yellow', 'red', 'orange', 'green', 'blue']
```

```py
#Sort in descending
thislist = [80, 10, 30, 50, 60]
thislist.sort(reverse = True)
print(thislist)
```

- if keyword argument is **reverse=False**, it will sort in ascending

```py
thislist = [80, 10, 30, 50, 60]
thislist.sort(reverse = True)
print(thislist)
```

## Customizing sort function

- by using keyword argument **key = function**
- Ex: sort the list based on the remainder when divided by 3.

```py
def customSort(num):
  return num%3

numbers = [10, 17, 12, 3, 21, 14]
numbers.sort(key=customSort)
print(numbers) # [12, 3, 21, 10, 17, 14]
```

```
numbers   = [10, 17, 12, 3, 21, 14]
remiander =   1   2   0  0   0   2

Now we need to sort according to the remainder,
Those numbers which have same remainder will maintain the given order

so output will be = [12 , 3, 21, 10, 17, 14]
                      0   0   0   1   2   2
```

- Question: Sort a list of names based on the lengths of the names

```py
def sortNames(names):
  return len(names)

names = ["Alice", "Bob", "David", "Charlie"]
names.sort(key=sortNames)
print(names) #['Bob', 'Alice', 'David', 'Charlie']
```

> Case Insensitive Sort:

- sort() method is case sensitive. Means all capital letters sorted before lowercase letters.
- Ex:

```py
thislist = ["apple", "Banana", "Orange", "mango"]
thislist.sort()
print(thislist) # ['Banana', 'Orange', 'apple', 'mango']

```

- To have case-insensitive sort function, we can use str.lower as key function

```py
thislist = ["apple", "Banana", "Orange", "mango"]

thislist.sort(key = str.lower)

print(thislist) #['apple', 'Banana', 'mango', 'Orange']

```

> reverse() Method:

- reverses the current sorting order.

```py
fruits = ["apple", "Banana", "Orange", "mango"]

print("Normal Sorting: ",fruits)

fruits.reverse()

print("With Reverse: ", fruits)
```

```
Normal Sort :  ['apple', 'Banana', 'Orange', 'mango']
With Reverse : ['mango', 'Orange', 'Banana', 'apple']
```

# Copy Lists:

- we cannot copy a list by assigning to another list because it will create a new refernce that points to the same list.
- Any modification will affect both the list
- When we say that two variables, list1 and list2, are referring to the same object in Python, it means that both variables are pointing to the exact same location in memory where the object is stored

```py
list1 = [1,2,3,4]
list2 = list1

list1.append(5)
print("List 1: ",list1)
print("List 2: ",list2)
```

```
List 1:  [1, 2, 3, 4, 5]
List 2:  [1, 2, 3, 4, 5]
```

## TWO WAYS TO COPY LISTS:

> 1. copy():

- built-in list method:

```py
list1 = [1,2,3,4,5]
list2 = list1.copy()
list1.append(6)
print(list1) # [1, 2, 3, 4, 5, 6]
print(list2) # [1, 2, 3, 4, 5]
```

> 2. list():

- another built-in method

```py
fruits = ["mango","banana","apple","orange"]
newlist = list(fruits)
print(newlist)
```

# JOIN(or Concatenate) LISTS:

- Three ways to do :

## 1. Using + Operator:

```py
letters = ["a","b","c","d"]
numbers = [1,2,3,4]

newList = letters + numbers
print(newList)  # ['a', 'b', 'c', 'd', 1, 2, 3, 4]
```

## 2. append() fun:

- appending all elements from one list to another.

```py
letters = ["a","b","c","d"]
numbers = [1,2,3,4]

for x in numbers:
  letters.append(x)

print(letters) # ['a', 'b', 'c', 'd', 1, 2, 3, 4]
```

## 3. extend() fun:

```py
letters = ["a","b","c","d"]
numbers = [1,2,3,4]

letters.extend(numbers)
print(letters)  #['a', 'b', 'c', 'd', 1, 2, 3, 4]
```

## List Comprehension:

- Process of reducing the syntax during looping through lists
- It helps when we create a new list based on the values of existing list
-
- Ex

```py
cities = ["Delhi","Mumbai","Pune"]
for x in cities:
  print(x)
```

- The above code can be reduced using list comphrension:

```py
cities = ["Delhi","Mumbai","Pune"]
[print(x) for x in cities]
```
