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

# Tuples:

- used to store multiple items in a single variable.
- created using round brackets
- EX:

```py
myTuple = ("red", "blue", "green");
print(myTuple) #('red', 'blue', 'green')
```

- Tuple items are ordered, unchangeable , can have duplicates

# Dictionary

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

# FUNCTIONS:

- Block of code
- Runs when called
- Data passed into functions are parameters:
- Created with **def** keyword.

```py
def greet():
    print("Hello World!")

greet()  #function call
```

> Arguments(or args):

- Data can be passed into functions as arguments
- Specified after fun name inside ().
- multiple arguments are separated by comma
- EX:

```py
def greet(name):
    print("Hello "+name);

greet("Ravi")
```

> Parameters(param) or Arguments:

- Both are same actually
- paramter is the variable inside () in fun defination
- Argument is the value sent during fun call
- Ex:

```py
def greet(firstName, lastName):
    print("Hello! My Name is "+firstName+ " "+lastName);

greet("Ravi", "Nayak")

# firstName,lastName : parameters
# "Ravi", "Nayak" : arguments
```

- Error:

```py
def greet(firstName. lastName):
    print(firstName+ " " +lastName);
greet("ravi");

# TypeError: greet() missing 1 required positional argument: 'lastName'
```

> Arbitary Arguments(\*args):

- If no. of argumenrts is unknown, add \* before parameter

```py
def myBrothers(*names):
    print("Youngest is: "+names[2])
myBrothers("Sibu", "Liku", "Sinu")

# Youngest is: Sinu
```

> KeyWord Arguments:

- Arguments can be sent in key-value pairs
- In this way, order of arguments does not matter.

```py
def myBrothers(bro2, bro1, bro3):
    print("Eldest: "+bro1)
myBrother(bro1="Sibu", bro2="")
```

# FOR LOOP

-

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

```

# WHILE LOOP:

```py
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
