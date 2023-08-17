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

# Python program to print even length words in a string:

```
Input: s = "i am laxmi"
Output: am
```

```py
# Python code
# To print even length words in string

#input string
n="This is a python language"
#splitting the words in a given string
s=n.split(" ")
for i in s:
#checking the length of words
if len(i)%2==0:
	print(i)

# this code is contributed by gangarajula laxmi

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

# Check Palindrome:

```py
myStr = input("Enter String: ")
if(myStr==myStr[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
```

# program to find the number of occurances of a word without using count() function.

```py
myStr=input("Enter string:")
word=input("Enter word:")
list=[]
count=0
list=myStr.split(" ")
for i in list:
      if(word==i):
            count=count+1
print(count)
```

# Program to check whether a string is symmetrical

```py
myStr = input("Enter the string: ")
half = int(len(string) / 2)


first_str = string[:half]
second_str = string[half:]


# symmetric
if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')
```

## Program to Find All Odd Palindrome Numbers in a Range:

```py
low = int(input("Enter lower limit: "))
upp = int(input("Enter upper limit: "))
numList = []
for x in range(low, upp+1):
    if x % 2 != 0 and str(x) == str(x)[::-1]:
        numList.append(x)
print("The numbers are: ",numList)
```
