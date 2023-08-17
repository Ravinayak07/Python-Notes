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
print(x[-1]) #l
```

## String Length:

```py
collegeName = "Silicon"
print(len(collegeName)) # 7
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

```py
collegeName = "Silicon"

for i in range(len(collegeName)):
    print(collegeName[i])
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
print(x[0:0])   # No ouput
print(x[0:1])   # S
```

```py
# will start from 0 index or first character
x = "Silicon institute"
print(x[:7])
print(x[:0])   # Empty String
print(x[:1])
```

```
Silicon

S
```

```py
x = "Silicon institute"
print(x[:7])
print(x[:0], end="")
print(x[:1])
```

```
Silicon
S
```

```py
# All the way to the end:
x = "Silicon institute"
print(x[0:]) # Silicon institute
print(x[-1:]) # e

```

- Negative Indexing

```py
# Negative Indexing:
x = "Silicon"
print(x[-7:-3]) # Sili
print(x[-1:-5]) # Empty
print(x[-1:-5:-1]) # noci
print(x[-1:-8:-2]) # nclS
print(x[1:8:2]) # iio
```

## Modify Strings:

- python has a set of built-in methods to modify strings:

> upper() : returns a new string in uppercase

```py
x = "Silicon"
res = x.upper()
print(type(res))
print(res)
print(x.upper())
print(x)

"""
<class 'str'>
SILICON
SILICON
Silicon
"""
```

> lower() : returns a new string in lowercase

```py
x = "Silicon"
print(x.lower())  # silicon

```

> strip(): returns a new string after removing whitespace from begining or end

```py
x = "  Silicon  "
res = x.strip()
print(res)
print(type(res))
print(x.strip())
print(len(res))
print(len(x))
```

```
Silicon
<class 'str'>
Silicon
7
11
```

> replace() : replaces a string with another string:

```py
x = "Silicon"
res = x.replace("i","e")
print(res)
print(x)
```

```
Selecon
Silicon
```

> split(): returns a list where the text between the specified separator becomes the list items:

```py
x = "Silicon, Institute"
res = x.split(",")
print(res)

y = "Silicon @ Institute"
res2 = y.split("@")
print(res2)

z = "Silicon, Institute"
res3 = z.split(":")
print(res3)
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

# String Methods:

- All string methods return new values. They do not change the original string.

> 1 . capitalize():

- Converts the first character to upper case

```py
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

```

> 2 . casefold(): Converts string into lower case

```py
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

```

> 3 . center() Returns a centered string

- center align the string, using a specified character (space is default) as the fill character.

```py
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"

x = txt.center(20)

print(x)
```

```py
txt = "banana"

x = txt.center(20, "O")

print(x)
```

> 4 . count() : Returns the number of times a specified value occurs in a string

```py
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
```

```py
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)

```

# PROGRAMS:

## Program to Calculate the Length of a String Without using Library Functions:

```py
myStr = input("Enter a string: ")
count=0
for i in myStr:
      count=count+1
print(count)
```

## Program to calculate the number of vowels in a string:

```py
myStr = input("Enter String: ")
count=0
vowels = "aeiou"
for i in myStr:
    if i.lower() in vowels:
        count=count+1

print(count)
```

## Program to calculate number of digits in a string:

```py
myStr = input("Enter String: ")
count=0
for i in myStr:
    if i.isdigit():
        count=count+1
print(count)
```

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

# Program tro reverse a string:

```py
# Using Slicing

myStr = input("Enter a string: ")
print("Reverse of the string is: ")
print(myStr[::-1])
```

```py
# Using loop
def reverseString(myStr):
    newStr = ""
    for i in myStr:
        newStr = i + newStr
    return newStr

myStr = input("Enter a string: ")
print(reverseString(myStr))
```

## Program to Count the Number of Words and Characters in a String:

```py
myStr = input("Enter a string: ")
count = 0
word = 0
flag = False  # Set flag to False initially

for i in myStr:
    count = count + 1
    if i == ' ':
        if not flag:  # Check if previous character was not a space
            word = word + 1
            flag = True
    else:
        flag = False

# Check if the last character was not a space
if myStr[-1] != ' ':
    word = word + 1

print("Characters:", count)
print("Words:", word)
```

## Program to Count Number of Lowercase Characters , uppercase characters and spaces in a String:

```py
myStr = input("Enter String: ")
low=0
up=0
space=0
for i in myStr:
    if i.islower():
        low=low+1
    elif i.isupper():
        up = up+1
    elif i==" ":
        space=space+1

print("Lowercase Characters: ",low)
print("Uppercase Characters: ",up)
print("Spaces: ",space)
```

# methods:

- replace
- islower()
- isupper()
