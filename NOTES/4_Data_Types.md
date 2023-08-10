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

# Casting:

- Since, Python is an object-orientated language, it uses classes to define data types, including its primitive types.
- Casting in done using constructor functions:

```
- int() - constructs an integer number from an integer literal, a float literal or a string literal

- float() - constructs a float number from an integer literal, a float literal or a string literal

str() - constructs a string s
```

- Ex:

```py
print(int(1)) # 1
print(int(2.8)) # 2
print(int("3")) # 3

print(float(1)) # 1.0
print(float(2.8)) # 2.8
print(float("3")) # 3.0
print(float("4.2")) # 4.2

print(str("s1")) # s1
print(str(2)) # 2
print(str(3.0)) # 3.0
```
