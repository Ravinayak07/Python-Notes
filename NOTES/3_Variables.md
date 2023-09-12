# VARIABLES:

- stores data

> Creating variable:

- There is no command for declaring variable in Python.
- Variables are created when we assign values to them.

  ```py
  x = 7
  y = "Ravi"
  print(7)
  print(Ravi)
  ```

> Variable Naming Rules:

- Must start with a letter or Underscore
- Cannot start with a number
- Keywords can't be used
- variables are case-sensitive
- Ex:

  ```py
  # Valid variable names
  myname = "Ravi"
  myName = "Ravi"
  my_name = "Ravi"
  _myName = "Ravi"
  myName2 = "Nayak"
  MYNAME ="Nayak"
  ```

  ```py
  # Invalid variable name
  5myName = "ravi"
  my-name = "ravi"
  my name="ravi"
  ```

# MultiWord Variable Names:

Four Cases:

> 1 . Camel case

```py
myCollegeName = "LPU"
```

> 2 . Pascal case

```py
MyCollegeName = "LPU"
```

> 3 . Snake Case

```py
my_college_name = "LPU"
```

## Assigning Multiple Values:

> 1 . Many values to many variables

```py
a, b, c = "CPP", "Python", "Java"

print(a)
print(b)
print(c)
```

- Here no.of variables should match no. of values, otherwise error.

> 2 . One value to Multiple Variables:

```py
a = b = c = "Python"

print(a)
print(b)
print(c)
```

## Print Variables

- print() function is used.

  ```py
  myName = "Ravi"
  print(myName)
  ```

- comma is used to separate multiple variables

  ```py
  x = "My College"
  y = "Name"
  z = "is LPU."
  print(x, y, z);
  ```

- Using + operator:

  ```py
  x = "My College"
  y = " Name "
  z = "is LPU."
  print(x+y+z);
  ```

  ```py
  # Error: cannot concatenate int and string
  x = 7
  y = "Ravi"
  print(x + y)
  ```

  ```py
  # correct:
  x = 7
  y = "Ravi"
  print(x, y)
  ```

# Global Variables:

- created outside of a function (i.e in the main body of python code)
- belongs to global scope
- can be used by both inside and outside of a function
- so global variables can be accessed within any scope i.e both local and global

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
print(myName)
```

# Local Variable:

- created inside a fun
- belongs to local scope of that function.
- can only be accessible inside the fun, not outside.
- Ex:

```py
def greet():
    myName = "Ravi"  #Local Variable
    print("Hello "+myName)

greet()
```

- Function inside function:

```py
def greet():
    myName = "Ravi"
    def greetWithName():
      print("Hello "+myName)

    greetWithName()

greet()
```

# Both Global and Local variable having same name

- Can both global and local variable have same name> yes
- But Python will treat them as two separate variables

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

- I want to create a global variable inside the fun (i.e in local scope). Is it possible??

```py
# Error
def greet():
    myName = "Ravi" #Local Vraibale
greet()

print("Hello "+myName)
```

- Here comes the global keyword. It is used to create a global variable in local scope.

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
