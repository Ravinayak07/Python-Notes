# PYTHON STRINGS:

```py
# Both are same:
print('Ravi')
print("Ravi")

x = "Ravi"
print(x)
```

- Assign multiline strings using triple quotes:

```py
x = """My name is Ravi,
I am from bhubaneswar, Odisha
"""
print(x)
```

- Or three single quotes

```py
x = '''My name is Ravi,
I am from bhubaneswar, Odisha
'''
print(x)
```

```
My name is Ravi,
I am from bhubaneswar, Odisha
```

## Strings are Arrays of Characters

- python doesnot has character data type
- A single character is a string of length 1

```py
x = "Silicon"
print(x[2]) #l
```

## Looping a string:

```py
collegeName = "Silicon"

for x in collegeName:
    print(x)
```

```
S
i
l
i
c
o
n
```

## String Length:

```py
collegeName = "Silicon"
print(len(collegeName)) # 7
```

## Check String:

```py
msg = "I am very proficient in Python Programming Language"

print("very" in msg) # True
# using if

if "very" in msg:
    print("Present")
```

## Check if Not:

```py
msg = "I am very proficient in Python Programming Language"

print("very" not in msg) # False
# using if

if "very" not in msg:
    print("Absent")
else:
    print("Present")
```

## String Slicing:

- used to return a range of characters
- Starting index included
- Ending index not included

```py
x = "Silicon institute"
print(x[2:5])   # lic
```

```py
# will start from 0 index or first character
b = "Hello, World!"
print(b[:5]) # Hello
```

```py
# All the way to the end:
b = "Hello, World!"
print(b[2:])  # llo, World!
```

```py
# Negative Indexing:
b = "Hello, World!"
print(b[-5:-2]) # orl
```

## Modify Strings:

- python has a set of built-in methods to modify strings:

> upper() : returns string in uppercase

```py
a = "Hello, World!"
print(a.upper())  # HELLO, WORLD!
```

> lower() : returns string in lowercase

```py
a = "Hello, World!"
print(a.lower())  # hello, world!
```

> strip(): removes whitespace from begining or end

```py
a = " Hello, World! "
print(a.strip()) #Hello, World!
```

> replace() : replaces a string with another string:

```py
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!
```

> split(): returns a list where the text between the specified separator becomes the list items:

```py
a = "Hello, World!"
b = a.split(",")
print(b) # returns ['Hello', ' World!']
```

## String Concatenation:

```py
a = "Hello"
b = "World"
c = a +" " + b
print(c)  # Hello World
```

## String formatting:

- we cannot combine strings and numbers using + operator

```py
age = 36
txt = "My name is John, I am " + age
print(txt)  # Error
```

- But it can be done using format() method

> format() method:

- used to format selected parts of string
- takes unlimited number of arguments, and are placed into the respective placeholders {}.
- Ex:

```py
age = 23
msg = "My age is {}"
print(msg.format(age)) # My age is 23
```

```py
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

```

- Add paramters inside {} to convert values in case of decimals

```py
price = 99
msg = "The price of this product is  {:.3f}"
print(msg.format(price)) #The price of this product is  99.000
```

- Multiple Values:

```py
name = "Ravi"
age = 22
year = 2023
msg = "My name is {}. I am {} years old. I graduated in the year {}"
print(msg.format(name,age,year))
```

```
My name is Ravi. I am 22 years old. I graduated in the year 2023
```

- Index Numbers can be used inside {} for correct placeing of values

```py
name = "Ravi"
age = 22
year = 2023
msg = "My name is {0}. I am {1} years old. I graduated in the year {2}"
print(msg.format(name,age,year))
```

```
My name is Ravi. I am 22 years old. I graduated in the year 2023
```

```py
age = 23
name = "Ravi"
msg = "My name is {1}. {1} is {0} years old."
print(msg.format(age, name)) # My name is Ravi. Ravi is 23 years old.

```

```py
price = 199
product = "Medicine"
msg = "The price of this {0} is  {1:.3f}"
print(msg.format(product, price)) #The price of this Medicine is  199.000
```

- We can't copmbine both ways of formatting. It will generate Error

```py
price = 199
product = "Medicine"
msg = "The price of this {0} is  {:.3f}"
print(msg.format(product, price))
```

> Named Indexes:

- names can be added inside {}
- Also need to pass the names in parameter values

```py
msg = "The Capital of {state} is {city}"
print(msg.format(city="Bhubaneswar",state="Odisha"))
```

```
The Capital of Odisha is Bhubaneswar
```

# PROGRAMS:

## Program to Remove Odd Indexed Characters in a string:

```
Means printing only even indexed characters
```

```py
def removeIndex(x):
    newString = ""
    for i in range(len(x)):
        if i % 2 == 0:
            newString = newString + x[i]
    return newString

myString = input("Enter string : ")
print(removeIndex(myString))
```

## Program to Remove the nth Index Character from a Non-Empty String

```py
def remove(myString, n):
      first = myString[:n]
      last = myString[n+1:]
      return first + last

myString = input("Enter string : ")
n=int(input("Enter the index of the character to remove:"))
print(remove(myString, n))
```

## Program to Replace Every Blank Space with underScore in a String:

```py
myString = input("Enter string : ")

myString=myString.replace(' ','_')

print("New string:", myString)
```

## Program to Replace All Occurrences of a character with $ in a String.

```py
myString = input("Enter string : ")
myChar = input("Enter character to replace : ")

myString=myString.replace(myChar.lower(),'$')
myString=myString.replace(myChar.upper(),'$')

print("New string:", myString)
```

# methods:

- replace
