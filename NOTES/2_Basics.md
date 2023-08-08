# Comments

```py
#This is a single line comment
```

```py
#This is a comment
#written in
#more than just one line
```

- We can use multiline string as comment
- Because python ignores string literals that are not assigned to a variable.

```py
"""
This is a comment
written in
more than just one line
"""
```

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
