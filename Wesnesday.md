# Indentation:

- refers to the spaces at the beginning of a code line.
- indicates a block of code.
- EX:

```py
if 5 > 2:
  print("Five is greater than two!")
```

- Error:

```py
if 5 > 2:
print("Five is greater than two!")
```

- We can give any number of spaces

```py
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")
```

- But you have to use same number of spaces in the same block of code:

```py
#Error
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
```

```py
#Error:
if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")
```

# Global Variables:

- created outside of a function.
- can be used by both inside and outside of a function

```
#Question
Create a function named greet that:
1) Displays: Hello myName
2) Where myName should be a global variable
```

```py
myName = "Ravi" #Global Variable
def greet():
    print("Hello " +myName)

greet()
```

# Local Variable:

- created inside a fun
- can only be accessible inside the fun, not outside,
- Ex:

```py
def greet():
    myName = "Ravi"  #Local Variable
    print("Hello "+myName)

greet()
```

# Both Global and Local variable having same name

- Can both global and local variable have same name> yes

```py
myName = "Ravi" #Global

def greet():
  myName = "Darshan" #Local
  print("Hello " + myName)

greet()

print("Hello " + myName)
```

```
Python is Darshan
Python is Ravi
```

## Problem:

- I want to create a global variable inside the fun. Is it possible??

```py
# Error
def greet():
    myName = "Ravi" #Local Vraibale
greet()

print("Hello "+myName)
```

- Here comes the global keyword. It is used to create a global variable inside a function.

```py
#Error
def greet():
    global myName = "Ravi";

greet()

print("Hello "+myName)
```

- The above is error because In Python, you need to declare it as global within the function before you can assign a new value to it

```py
def greet():
    global myName
    myName = "Ravi"

greet()

print("Hello "+myName)
```

- Also, use the global keyword if you want to change a global variable inside a function.

```py
x = "awesome"

def myfunc():
  x = "fantastic"

myfunc()

print("Python is " + x)
```

```
Python is awesome
```

- But i want output: "Python is fantastic"

```py
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

# BOOLEANS

- Two values: True or False

```py
print(10>20)  # False
print(20==20) # True
print(10<=10) # True
print(5=5) #Syntax error
```

> bool() function:

- evaluates any values and returns True or False
- Almost all values are True if it has content
- Any String is true except empty string
- Any number is True, except 0
- Any list, tuple, set, and dictionary are True, except empty ones.
- Empty values are false: [],(),{},"", 0, None

```py
print(bool("Ravi")) #True
print(bool(15)) # True
print(bool("")) # False (Empty String)
print(bool(0))  # False
print(bool(["red", "green", "blue"])) #False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool(None)) # False
print(bool(False)) # False
```

- Can functions return boolean value: Yes

```
Create a function:
1) takes two paramters
2) if param1 > param2, fun should return True, Otherwise false
```

```py
def checkParam(x,y):
    return x>y

print(checkParam(10,6)) #True
```

> isinstance() function:

- it is built-in function that returns a boolean value
- used to determine if an object has a certain data type

```py
x = 7
print(isinstance(x, int)) # True
```

```py
x = 5.6
print(isinstance(x, float)) # True
```

```py
x = "Ravi"
print(isinstance(x, string)) # Error
```

```py
x = "Ravi"
print(isinstance(x, str)) # True
```

# Operators:

- Used to perform operations on variables and values.

## Types:

> 1 . Arithmetic:

```
+ , - , * , / , % , **(expoentiation), //(Floor Divison)
```

```py
x = 10
y = 3

print(x % y) # 1
print(x ** y) # 1000
```

> Differnce between / and //

- /(Regular divison):
- returns the result as floating point number
- Means includes the decimal even if it is whole numbers

```py
print(5/2) # 2.5
print(2/2) # 1.0
print(38/10) #  3.8
```

- //(Floor Divison):
- returns the result as integer number(no decimal part)
- returns largest integer which is <= result

```py
print(5//2) #  2
print(2//2) #  1
print(38//10) # 3.8
```

> 2 . Assignment:

```py
x = 5
x += 5 # x = x + 5
print(10)
```

```py
x = 10
x /= 3 # x = 10 /3
print(x) # 3.3333333333333335
```

```py
x = 5
x **= 3
print(x)
```

```py
# Bitwise AND
x = 5
x &= 3
print(x)

""""
5 (x)   =  101
3       =  011
--------------
x &= 3  =  001 (1 in decimal)
""""
```

- Bitwise or

```py
x = 5
x |= 3
print(x) # 7

""""
5 (x)   =  101
3       =  011
--------------
x |= 3  =  111 (7 in decimal)
""""
```

- Bitwise XOR(^) : 1 if bits are different

```py
x = 5
x ^= 3
print(x) # 6
```

```py
"""
5 (x)   =  101
3       =  011
--------------
x ^= 3  =  110 (6 in decimal)
"""
```

> 3 . Comparison Operators:

```
==, != , > , < , >= , <=
```

> 4 . Logical Operators:

```
and(&)
or(|)
not()
```

> 5 . Idenitity operators(is, is not):

- used to compare the objects
- doesnot compare whether they have equal value.
- it compares whether they are actually the same object i.e having same memory location.

```py
x = ["red", "blue"]
y = ["red", "blue"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y) # True
```

```py
x = ["red", "blue"]
y = ["red", "blue"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y) # False
```
