# type() function

- returns the type of variable.

  ```py
  x = 7
  y = "Ravi"
  print(type(x))
  print(type(y))
  ```

  ```
  <class 'int'>
  <class 'str'>
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

- evaluates any values or expressions and returns True or False
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

- Functions can also return boolean values

  ```py
  def checkParam(x,y):
    return x>y
  print(checkParam(10,6)) #True
  ```

> isinstance() function:

- It is built-in function that returns a boolean value
- used to determine if an object has a certain data type or not

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

- Python uses classes to define data types.
- Casting is done using constructor functions like int(), float() and str()

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
