# VARIABLES:

- stores data

> Creating variable:

- Python has no command for declaring variable
- variable is created when we assign value to it.

```py
x = 7
y = "Ravi"
print(7)
print(Ravi)
```

> Casting:

- to specify the data type of variable:

```py
x = str(7)
y = int(7)
z = float(7)

print(x)
print(y)
print(z)

```

> Get the type:

- by type() function

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

## VARIABLE NAMES:

- Must start with a letter or Underscore
- Cannot start with a number
- case-sensitive
- cannot be any python keywords
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
# In valid variable name
5myName = "ravi"
my-name = "ravi"
my name="ravi"
```

# MultiWord Variable Name:

> Camel case

```py
myCollegeName = "LPU"
```

> Pascal case

```py
MyCollegeName = "LPU"
```

> Snake Case

```py
my_variable_name = "LPU"
```

## ASSIGNING MULTIPLE VALUES:

> Many values to many variables

```py
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

```

- Here no.of variables should match no. of values, otherwise error.

> One value to Multiple Variables:

```py
x = y = z = "Orange"

print(x)
print(y)
print(z)

```

## Output Variables

- print() function is used.

```py
myName = "Ravi"
print(myName)
```

- multiple variables are separated by comma

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
#correct:
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
