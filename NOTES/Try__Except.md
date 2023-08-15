# Try Except:

- **try** block: used to test code for errors
- **except** block: handles the error
- **else** block: executes code when there is no error
- **finally** block: executes the code irrespective of the results of try and except blocks

## Excepection Handling:

- Python stops working when encounters error or exception
- These errors are handled by try statement:

```py
# try block will generate error as x is not defined
# so except block will execute
try:
    print(x)
except:
    print("Error")
```

- Without try block, program will crash and raise error

```py
print(x)
```

- Multiple except block can be defined.

```py
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
```

```
Variable x is not defined
```

> Else block:

- Executes when there is no Error

```py
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

```
Hello
Nothing went wrong
```

> finally:

- It will always get executed whether try block raises error or not.

```py
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```

```
Something went wrong
The 'try except' is finished
```

- This can be useful to close objects and clean up resources. For Ex:

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

> Raise an Exception:

- raise keyword is used to throw/raise exception
- Ex:

```py
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

```

```
Exception: Sorry, no numbers below zero
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
