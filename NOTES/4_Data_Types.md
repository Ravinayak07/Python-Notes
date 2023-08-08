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
