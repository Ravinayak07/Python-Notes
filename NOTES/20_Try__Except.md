# ERRORS AND EXCEPTIONS:

- Errors are problems in a program due to which the program will stop the execution
- Exceptions are raised when some internal events occur which change the normal flow of the program.

# Different types of exceptions in python::

- There are several built-in exceptions that can be raised when an error occurs during the execution of a program

> 1 . SyntaxError:

- syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

> 2 . TypeError:

- This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

> 3 . NameError:

- This exception is raised when a variable or function name is not found in the current scope.

> 4 . IndexError:

- This exception is raised when an index is out of range for a list, tuple, or other sequence types.

> 5 . KeyError:

- This exception is raised when a key is not found in a dictionary.

> 6 . ValueError:

- This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

> 7 . AttributeError:

- This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.

> 8 . IOError:

- This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

> 9 . ZeroDivisionError:

- This exception is raised when an attempt is made to divide a number by zero.

> 10 . ImportError:

- This exception is raised when an import statement fails to find or load a module.

- These are just a few examples of the many types of exceptions that can occur in Python. It’s important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing.

## Difference between Syntax Error and Exceptions:

- Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.

```py
# initialize the amount variable
amount = 10000

# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")
```

- Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

```py
# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)
```

- 1. TypeError: This exception is raised when an operation or function is applied to an object of the wrong type. Here’s an example:

```py
x = 5
y = "hello"
z = x + y  # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- try catch block to resolve it:

```py
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")
```

## Try and Except Statement – Catching Exceptions:

- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause:
- Example: Let us try to access the array element whose index is out of bound and handle the corresponding exception.

```py
# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))

    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))

except:
    print ("An error occurred")
```

```
Second element = 2
An error occurred
```

## Catching Specific Exception:

- A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed. For example, we can add IndexError in the above code. The general syntax for adding specific exceptions are –

```py
try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
```

- Example: Catching specific exceptions in the Python:

```py
# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
    if a < 4:

        # throws ZeroDivisionError for a = 3
        b = a/(a-3)

    # throws NameError if a >= 4
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
```

```
ZeroDivisionError Occurred and Handled
```

- If you comment on the line fun(3), the output will be

```
NameError Occurred and Handled
```

- The output above is so because as soon as python tries to access the value of b, NameError occurs

## Try with Else Clause:

- In Python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception
- Ex:

```py
# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
```

```
-5.0
a/b result in 0
```

## Finally Keyword in Python:

- Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try block or after the try block terminates due to some exception.
- Syntax:

```py
try:
    # Some Code....

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
```

- Examples:

```py
# Python program to demonstrate finally

# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
```

```
Can't divide by zero
This is always executed
```

# Raising Exception

- The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).

```py
# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
```

- The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to the raise statement in the last line. So, the output on your command line will look like

```
Traceback (most recent call last):
  File "/home/d6ec14ca595b97bff8d8034bbf212a9f.py", line 5, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
```

# Advantages of Exception Handling::

- Improved program reliability: By handling exceptions properly, you can prevent your program from crashing or producing incorrect results due to unexpected errors or input.
- Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, making it easier to read and maintain your code.
- Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, leading to cleaner and more readable code.
- Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location where the exception occurred, making it easier to debug your code.

# Disadvantages of Exception Handling::

- Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional work to catch and handle the exception.
- Increased code complexity: Exception handling can make your code more complex, especially if you have to handle multiple types of exceptions or implement complex error handling logic.
- Possible security risks: Improperly handled exceptions can potentially reveal sensitive information or create security vulnerabilities in your code, so it’s important to handle exceptions carefully and avoid exposing too much information about your program.
- Overall, the benefits of exception handling in Python outweigh the drawbacks, but it’s important to use it judiciously and carefully in order to maintain code quality and program reliability.

# Try Except:

- **try** block: used to test code for errors
- **except** block: used to handle the error
- **else** block: executes code when there is no error
- **finally** block: executes the code irrespective of the results of try and except blocks

## Excepection Handling:

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

> Multiple except blocks can be also defined.

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

## Else block:

- Executes when there is no Error

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

## finally block:

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

- This can be useful to close files and clean up resources. For Ex:

```py
# Trying to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```

```
Something went wrong when writing to the file
```

## Raise an Exception:

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

## TYPES OF ERRORS:
