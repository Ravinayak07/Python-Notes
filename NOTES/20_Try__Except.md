# ERRORS AND EXCEPTIONS:

- Errors are problems in a program due to which the program will stop the execution. Errors can be two types: Syntax Errors and Runtime errors.
- Syntax errors are caused by the wrong syntax in the code. It leads to the termination of the program.

```py
x = 10
if(x>5)
print("Greater")
```

- Runtime errors occur during the execution of the program and are caused by various factors such as invalid input, division by zero, accessing non-existent elements, etc.
- Now An exception is a specific type of runtime error that occurs when the program encounters a situation it cannot handle or when an unexpected condition arises during execution.

# Different types of Exceptions in python::

- There are several built-in exceptions that can be raised when an error occurs during the execution of a program

> 1 . TypeError:

- This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

```py
total = 10 + "5"  # Adding int and str
```

> 2 . NameError:

- This exception is raised when a variable or function name is not found in the current scope.

```py
prnt(x)
```

> 3 . IndexError:

- This exception is raised when an index is out of range for a list, tuple, or other sequence types.

```py
my_list = [1, 2, 3]
print(my_list[5])  # Index out of range
```

> 4 . KeyError:

- This exception is raised when a key is not found in a dictionary.

```py
my_dict = {"Name": "Silicon"}
print(my_dict["name"])  # Key does not exist in the dictionary
```

> 5 . ValueError:

- This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

```py
int("abc")  # String cannot be converted to an integer
```

> 6 . ZeroDivisionError:

- This exception is raised when an attempt is made to divide a number by zero.

```py
x = 5
y = 0
result = x / y  # Division by zero
```

- These exceptions can be handled using try and except blocks

## Try and Except Statement – Catching Exceptions:

- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause:
- Python stops working when it encounters error or exception.

```py
print(x)

sport = "Cricket"
print("I like to play",sport)
```

```
NameError: name 'x' is not defined
```

- The above code will stop execution and will not execute other statements:
- - These errors or Exceptions can be handled by try statement:

```py
# try block will generate error as x is not defined
# so except block will execute
try:
    print(x)
except:
    print("Error: x is not defined")

sport = "Cricket"
print("I like to play",sport)
```

```
Error: x is not defined
I like to play Cricket
```

- Without try block, program will crash and raise error

## Catching Specific Exception:

- Multiple except blocks can be also defined to specify handlers for different exceptions.

- Example

```py
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Other Error")

sport = "Cricket"
print("I like to play",sport)
```

```
Variable x is not defined
I like to play Cricket
```

- Syntax error:

```py
try:
    x= "Five" + 5
    print(x)
except NameError:
    print("Variable x is not defined")
except TypeError:
    print("can only concatenate str (not 'int') to str")

sport = "Cricket"
print("I like to play",sport)
```

```
can only concatenate str (not 'int') to str
I like to play Cricket
```

## Try with Else Clause:

- Executes only if the try clause does not raise an exception
- Ex:

```py
try:
  x=5
  print(x)
except:
  print("Error")
else:
  print("No Error")
```

```
5
No Error
```

```py
# Function which returns a/b
def myFun(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

myFun(2.0, 3.0)
myFun(3.0, 3.0)
```

```
-5.0
a/b result in 0
```

## Finally Keyword in Python:

- It will always get executed whether try block raises error or not.

```py
# In case of error
try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
  print("Try Except Execution is Finished")

```

```
Variable x is not defined
Try Except Execution is Finished
```

- In case of no error:

```py
try:
    x=5
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
  print("Try Except Execution is Finished")
```

```
5
Try Except Execution is Finished
```

```py
try:
    k = 5//0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
```

```
Can't divide by zero
This is always executed
```

# Raising Exception

- raise keyword is used to throw/raise exception
- Ex:

```py
x = -1

if x < 0:
  raise Exception("Number is below zero")

```

```
Number is below zero
```

- We can define what kind of error to raise, and the text to print to the user.

```py
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
```

```
TypeError: Only integers are allowed
```

# Advantages of Exception Handling::

- Improved program reliability: Prevent program from crashing or producing incorrect results due to unexpected errors or input.
- Simplified error handling: It separates error handling code from the main program logic, making it easier to read and maintain.
- Cleaner code: more readable code.
- Easier debugging: making it easier to debug your code.

# Disadvantages of Exception Handling::

- Performance overhead: Makes the program litte slower
- Increased code complexity: Makes code more complex, especially if you have to handle multiple types of exceptions or implement complex error handling logic.
- Possible security risks: Improperly handled exceptions can potentially reveal sensitive or confidential information
