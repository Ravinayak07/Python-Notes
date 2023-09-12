# Introduction:

- Python is an interpreted language
- It means that Python code is executed line by line by an interpreter at runtime, rather than being compiled into machine code beforehand.
- When you run a Python script, the Python interpreter reads your code, parses it, and then executes it directly. This makes Python code highly portable, as it can be run on any platform with the appropriate interpreter installed.

# Python Command Line:

- Quickest way to test short amount of python code:
- Open cmd and run this command:
  ```
  C:\Users\ASUS>python
  ```
- Or

  ```
  C:\Users\ASUS>py
  ```

- Wite any python code

  ```
  C:\Users\ASUS>python
  Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec 6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  > > > print("Hello World!")
  > > > Hello World!
  ```

- To quit python command line interface:

  ```
  exit()
  ```

# Comments

```py
# This is a single line comment
```

```py
# This is a
# Multiline
# Comment
```

- We can use multiline string as comment because python ignores string literals that are not assigned to a variable.

```py
"""
This is
a multiline
Comment
"""
```

# Indentation:

- refers to the spaces at the beginning of a code line.
- indicates a block of code.
- EX:

  ```py
  if 10 % 2 == 0:
        print("Even")
  ```

- Error:

  ```py
  if 10 % 2 == 0:
  print("Even")
  ```

- Any number of spaces can be given

  ```py
  if 10 % 2 == 0:
    print("Even")

  if 9 % 2 != 0:
     print("Odd")
  ```

- In a block of code same number of spaces should be used

  ```py
  # IndentationError: unexpected indent

  if 10 % 2 == 0:
   print("Even")
        print("Even)
  ```

  ```py
  # Correct
  if 10 % 2 == 0:
        print("Even")
        print("Even)
  ```
