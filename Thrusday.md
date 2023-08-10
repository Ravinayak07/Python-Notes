# Error in Grade Program:

```py
sub1=int(input("First subject: "))
sub2=int(input("Second subject: "))

avg=(sub1+sub2)/2

if avg>=90:
    print("Grade: A")
elif avg>=80 & avg<90:
    print("Grade: B")
else:
    print("Grade: C")
```

```
TypeError: unsupported operand type(s) for &: 'int' and 'float'
```

> SOlution 1: type casting

```py
avg=(sub1+sub2)/2
```

> Solution 2: using logical and , not bitwise &

```py
avg>=80 and avg<90:
```

```
- In python, logical AND(and) and Bitwise AND(&) both are different
- Using & operator between an int and a float is not allowed
- While working with boolean operations, use logical AND(and) , not bitwise AND(and)
- The bitwise AND operator is used to perform a bitwise AND operation between individual bits of corresponding numbers. It operates on integers at the binary level, treating each bit separately.
- The logical AND operator is used to combine two or more boolean expressions and evaluate whether they are all true. It operates on boolean values and returns a boolean result.
```

```
The expression print(5 and 3) will output 3.

In Python, the and operator returns the first "falsy" value it encounters, or the last value if all values are "truthy". In this case, both 5 and 3 are considered "truthy" values, so the and operator returns the last value, which is 3.
```

```
The expression print(5 & 3) will output 1.

In this case, the & operator is performing a bitwise AND operation between the binary representations of 5 (101 in binary) and 3 (011 in binary). The result of the bitwise AND operation is 001 in binary, which is 1 in decimal.
```

```
The expression print(0 and 3) will output 0.

In this case, the first value 0 is considered "falsy" because it is equivalent to False in a boolean context. Therefore, when the and operator is used, it immediately returns the first "falsy" value encountered, which is 0. The second value 3 is not even evaluated in this case.

```

```
he expression print(1 and 0) will output 0.

In this case, both 1 and 0 are considered "truthy" values. However, the and operator returns the last value encountered if both values are "truthy". So, it evaluates both values and returns the second value, which is 0.
```

```
In Python, the & operator is a bitwise AND operator, and it has a higher precedence than comparison operators like >= and <. This means that the expression 2 >= 80 & 2 < 90 is actually being interpreted as (2 >= (80 & 2)) < 90.

Now, let's break down the bitwise AND operation: 80 & 2 is equal to 0. So the expression becomes 2 >= 0 < 90, which is equivalent to True because 2 >= 0 is True, and True is considered as 1 in numerical comparisons.

However, this behavior might not be immediately intuitive, and it's generally recommended to use parentheses to clarify the order of operations and to avoid confusion. If you want to perform logical comparisons, it's better to use the and keyword:

python
Copy code
print(2 >= 80 and 2 < 90)
This will give you the expected and more readable result of False.
```

```
# Leap Year
How to check whether it is a Leap year or not?
To check if a year is a leap year, it should satisfy the following conditions:

The year should be divisible by 4.
If the year is divisible by 100, it should also be divisible by 400.
Examples:
Example 1: Let’s check if the year 2024 is a leap year using these conditions:

Is 2024 divisible by 4? Yes, it is.
Is 2024 divisible by 100? No, it is not.
Therefore, 2024 is a leap year.

Example 2: Let’s take another example to determine if the year 2100 is a leap year or not:

Is 2100 divisible by 4? Yes, it is.
Is 2100 divisible by 100? Yes, it is.
Is 2100 divisible by 400? No, it is not.
Therefore, 2100 is not a leap year.
```

```py
# Python Program to Check Leap Year

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
```

```py
year = int(input("Enter year to be checked: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")
```

# LOOPS

- Python has two loops: for loop and while loop.

## Diff bet While and For loop:

- While loop iterates over a condition
- For loop iterates over a sequence(list,tuple,dictionary,set, string)

## WHILE LOOP:

- Executes the code as long as the condition is true.

```py
i = 0
while i<5:
  print(i)
  i=i+1
```

- If we don't add the updation statement, it will be an infinite loop.

# Control Statements:

- Manages the flow of program by determining which code should be executed next.

> Break :

- can stop the loop even if the condition is true

```py
i=0
while i<5:
  print(i)
  if i==4:
    break
  i = i+1
```

```
0
1
2
3
4
```

> Continue

- can stop the current iteration and continue with the next.
- Question: Write a while loop that prints from 1 to 5 except 3:

```py
# Wrong Code
i = 1
while i < 5:
  if i == 3:
    continue
  print(i)
  i = i + 1

# it will print 1, 2 and after that it will go to infinite loop
```

- Right code

```py
i=0
while i<5:
  i = i+1
  if i==3:
    continue
  print(i)
```

## FOR LOOP

- iterates over a sequence(list, tuple, dictionary, set, string)
- Ex: Create a list and print its items using for loop:

```py
colors= ["red", "blue", "green"]
for x in colors:
  print(x)
```

- Ex: Create a string and print its characters using for loop in one line.

```py
collegeName = "Silicon Institute"
for x in collegeName:
  print(x, end="")
```

- Ex: Create a list and print its items using for loop and skip the any one item

```py
colors = ["red","blue","green"]
for x in colors:
  if x=="red":
    continue
  print(x)
```

- Ex: Create a list and demonstrate the working of for loop using break

```py
colors = ["red","blue","green"]
for x in colors:
  if x == "blue":
    break
  print(x)
```

> range() function:

- helps to loop for a speceified number of times
- it returns a sequence of numbers starting from 0(by default), increments by 1(by default) till reaches at a specified number
- Ex: range(6) means values from 0 to 5.
- Question: print first 10 whole numbers using for loop and range() function

```py
for x in range(10):
  print(x)  # 0 to 9
```

- Starting value can be specified by adding parameter:

```py
for x in range(3, 10):
  print(x)  # 3 to 9
```

- Range() fun increments bydefault by 1
- Increment value can be specified by adding third parameter

```py
for x in range(2,10,3):
  print(x)
```

```
2
5
8
```

> Else in For Loop:

- executes when the loop is finished

```py
for x in range(10):
  print(x)
else:
  print("Loop Over")
```

- If break is used else will not work:

```py
for x in range(10):
  if x==5:
    break
  print(x)
else:
  print("Loop over")
```

> pass in For loop:

- for loops can't be empty:

```py
# error:
for x in range(6):
```

- So we can use pass here

```py
for x in range(6):
  pass
```

- Ex to delay:

```py
for x in range(100000000):
    pass
else:
    print("Loop over")
```

## Do while loop

- In c

```c
do {
  //Code
} while(condition);
```

- In Python?
- Python doesnot has do while to reduce complexity
- The same functionality of do while can be achieved through
  'while' and 'break'
- In C:

```c
int num = 10;
do {
  printf("%d",num);
  num = num-1;
} while(num<=0);
```

- In Python:

```py
num = 10
while True:
  print(num)
  num=num-1
  if num<=0:
    break;
```

# LOOPS PROGRAM

# Print All Even Numbers in a Range

```py
lowRange = int(input("Enter the lower limit :"))
highRange =int(input("Enter the higher limit :"))

for i in range(lowRange,highRange):
    if(i%2==0):
        print(i)
```

# Program to print the table of a given number:

```py
num = int(input("Enter the number :"))
for i in range(1,11):
    print(num , "x" ,i,"=",num * i)
```

# Find the reverse of a Number

```py
num = int(input("Enter the number : "))
revNum=0
while(num>0):
    digit=num % 10
    revNum = revNum*10 + digit
    num =int(num/10) #or num = num//10 (Floor divison)

print("Reverse : ", revNum)
```

# Exam: Check If a Number is Palindrome

- A number is a palindrome if its reverse is equal to the number itself.
- EX: 121, 454, 888, etc.

```py
num = int(input("Enter the number : "))
temp=num
revNum=0
while(num>0):
    digit=num % 10
    revNum = revNum*10 + digit
    num =int(num/10) #or num = num//10 (Floor divison)
if(temp==revNum):
    print("Palindrome")
else:
    print("Not a Palindrome")
```

# Print all Numbers between 0 and 100 which is not divisible by 2 and but divisible by 3

```py
for i in range(0, 31):
    if(i % 2 !=0 and i % 3 == 0):  # u can use & also.
        print(i)
```

# Program to Count Number of digits in a Number:

```py
num = int(input("Enter number:"))
count=0
while num>0:
    count=count+1
    num = num//10
print("Total Number of digits : ",count)
```

# Program to print sum of digits of a number

```py
num = int(input("Enter a number: "))
sum=0
while num>0:
    digit = num % 10
    sum = sum + digit
    num = num//10;

print(sum)
```

# Programs to print sum of digits of a number using list

```
1. create an empty list
2. insert all digits into the list
3. Add all list items
```

```py
digitsList = []
num = int(input("Enter a number: "))
while num>0:
    digit = num % 10
    digitsList.append(digit)
    num=num//10
print("Sum: ", sum(digitsList))
```

# Program to print all divisors of a number and also its sum

- Ex: if num = 10, divisrors are 2,5,10. So sum = 18

```py
num = int(input("Enter an integer : "))
print("Divisors are : ")
sum = 0
for i in range(2, num+1):
    if(num % i==0):
        print(i)
        sum = sum+i
print("Sum :", sum)
```

- Using while loop:

```py
num = int(input("Enter an integer : "))
print("Divisors are : ")
sum = 0
i = 2
while i <= num:
    if num % i == 0:
        print(i)
        sum = sum+i
    i += 1
print("Sum :", sum)
```

# Program to print the smallest divisor of a Number

```py
num = int(input("Enter an integer:"))

for i in range(2,num+1):
    if num % i==0:
        print("Smallest divisor is:",i)
        break;
```

# Program to find the largest divisor of a Number except the number

- Largest divisor = number/smallest divisor

```py
num = int(input("Enter an integer:"))

for i in range(2,num+1):
    if num % i==0:
        break;
print("Largest Divisor: ", num//i);
```

# Program to check Prime Number:

```py
num = int(input("Enter a number: "))

count=0

if num == 1:
    print("Not a prime")
else:
    for i in range(1, num+1):
        if (num % i) == 0:
            count=count+1

    if count==2:
        print("Prime")
    else:
        print("Not a Prime")
```

# Program to print all prime Numbers between 1 and 100

```py
for i in range(2,101):
    count=0
    for x in range(1,i+1):
        if i%x == 0:
            count=count+1
    if count==2:
        print(i)
```

# EXAM: Program to check whether a number is perfect Number using function

```
 A perfect Number is a number which is equal to the sum of its divisors
 Some perfect numbers are 6, 28, 496, 8128

 Ex: divisrors of 6 = 1,2,3
     sum = 1+2+3 = 6
     hence perfect number
```

```py
def is_perfect_number(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print("Perfect Number")
else:
    print("Not a perfect number.")
```

# EXAM: Program for Sum of squares of first n natural numbers

```py

def squaresum(n):
	sm = 0
	for i in range(1, n+1):
		sm = sm + (i * i)

	return sm
n = 4
print(squaresum(n))
```

# FUNCTIONS:

- Block of code
- Runs when called
- Data passed into functions are parameters:
- Created with **def** keyword.

```py
def greet():
    print("Hello World!")

greet()  #function call
```

> Arguments(or args):

- Data can be passed into functions as arguments
- Specified after fun name inside ().
- multiple arguments are separated by comma
- EX:

```py
def greet(name):
    print("Hello "+name);

greet("Ravi")
```

> Parameters(param) or Arguments:

- Both are same actually
- paramter is the variable inside () in fun defination
- Argument is the value sent during fun call
- Ex:

```py
def greet(firstName, lastName):
    print("Hello! My Name is "+firstName+ " "+lastName);

greet("Ravi", "Nayak")

# firstName,lastName : parameters
# "Ravi", "Nayak" : arguments
```

- Error:

```py
def greet(firstName. lastName):
    print(firstName+ " " +lastName);
greet("ravi");

# TypeError: greet() missing 1 required positional argument: 'lastName'
```

> Arbitary Arguments(\*args):

- If no. of argumenrts is unknown, add (\*) before parameter name in function def
- In this way, the fun will receive a tuple of arguments and can be accessed using index

```py
def progLanguages(*names):
    print("Now we are learning: "+names[1])
progLangueages("Java", "Python", "CPP")

# Now we are learning: CPP
```

> KeyWord Arguments:

- Arguments can be sent in key-value pairs
- In this way, order of arguments does not matter.

```py
def progLanguages(lang3, lang1, lang2):
    print("Now we are learning: "+lang2)
progLanguages(lang1="Java", lang2="Python", lang3="CPP")
```

> Key Arguments along with Arbitary arguments

```py
def progLanguages(**names):
    print("Now we are learning: "+names["lang2"])

progLanguages(lang1="Java", lang2="Python", lang3="CPP")
```

> Default Parameter Value

- If we call the function without argument, it uses the default value:

```py
def cities(name = "Delhi"):
    print("My City name is : "+name)

cities("Mumbai")
cities("Pune")
cities()
```

## Collection data Types

- There are 4 built-in data types in Python to store collection of data:
- 1 . Lists: Ordered, Mutable, Allows Duplicate
- 2 . Tuple: Ordered, Unmutable, Allows Duplicate
- 3 . Set: Unordered, Unchangeable(but items can be removed or add), Unindexed, No Duplicate
- 4 . Dictionary: Ordered(in Python version 3.7 but unordered in version 3.6 and earlier ), changeable, No duplicate

# Python Lists:

- used to store multiple items in a variable
- created using square brackets.
- Ex:

```py
iplTeams = ["CSK", "MI", "RCB"];
print(iplTeams);
```

- list items ordered, mutable, can have duplicate values.
- First item of list has index 0.

> Ordered:

- List items have defined order
- Order will not change
- New elements are placed st the end.
- Note: Some list methods changes the order:

> Mutable:

- we can change, add and remove items in a list

> Allow Duplicates:

- List can have duplicate values
- EX:

```py
iplTeams = ["CSK", "MI", "RCB", "CSK"]
print(iplTeams) #['CSK', 'MI', 'RCB', 'CSK']
```

> List Length:

- len() fun is used to find the number of items in a list
- Ex:

```py
colors = ["Yellow", "Blue", "Red"]
print(len(colors)) # 3
```

> Data Types of List Items

- List Items can be of any data type
- Ex:

```py
fruits = ["apple", "orange","Guava"] #string type
numbers = [1,2,4,5] # Integer Type
decision = [True, False, True] # Boolean Type

print(fruits) # ['apple', 'orange', 'Guava']
print(numbers) # [1, 2, 4, 5]
print(decision) # [True, False, True]
```

- List items can be of different data types:
- Ex:

```py
myList = ["Ravi", 22, True, "BBSR"]
print(myList);
```

> type():

- List are defined as objects with the data type list

```py
myList = ["Mercury","Venus", "Earth","Mars"];
print(type(myList));  # <class 'list'>
```

> list() constructor:

- used to create new list
- Ex:

```py
myList = list(("apple", "orange", "Banana"));
print(myList) # ['apple', 'orange', 'Banana']
```

> ACCESS ITEMS:

- Since list are indexed, its items can be accessed using index
- EX:

```py
colors = ["blue","red","Green"]
print(colors[1]) #red
```

- Negative indexing means start from end.
- -1 refers to last item.

```py
colors = ["blue","red","Green"]
print(colors[-2]); #red
```

> Range of Indexes:

- Specify start index(included) and where to end(not included).
- Return value is new list with specified items.
- EX:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[1:4]) # ['blue', 'green', 'yellow']
```

- If start index is not mentioned, range will start from first item

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[:4]); # ['red', 'blue', 'green', 'yellow']
```

- If the end index is not mentioned, range will start go on to the end of the list:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[2:]); #['green', 'yellow', 'orange', 'violet']
```

> Range of Negative Indexes

- EX:

```py
colors = ["red", "blue", "green" , "yellow" ,"orange", "violet"];
print(colors[-4:-1]); #['green', 'yellow', 'orange']
```

> CHheck if Item Exists:

- Use **in** keyword

```py
color = ["red", "blue", "green"]
if "green" in color:
    print("Yes")
```

> Change Item Value:

- Refer Index Value:

```py
# create a list, modify any item value and print the new list

progLang = ["Java","C","CPP"]
print(progLang)

# changinng 2nd item:
progLang[1] = "Python"

print(progLang)
```

```
['Java', 'C', 'CPP']
['Java', 'Python', 'CPP']
```

> Changing Item Values within a Range:

- Question: create a of list 5 items and then replace a range of list items between index 2 and 4(not included).
- Ans:

```py
# creating a list of 5 items
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

# inserting items between index 2 and 4
progLang[2:4] = ["HTML","CSS"]

print(progLang)

```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'HTML', 'CSS', 'Javascript', 'Kotlin']
```

- If you insert more than you replace, new items will added and remaining items will be moved.

```py
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

#replacing only 2nd index(3 is not counted) with two items
progLang[2:3] = ["HTML","CSS"]

print(progLang)
```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'HTML', 'CSS', 'CPP', 'Javascript', 'Kotlin']
```

- In this case the length of list changes when no. of items inserted does not match the no. of items replaced.

- Now, inserting less than replace:

```py
progLang = ["C","Java","Python","CPP","Javascript","Kotlin"]
print(progLang)

progLang[3:6] = ["HTML"]

print(progLang)
```

```
['C', 'Java', 'Python', 'CPP', 'Javascript', 'Kotlin']
['C', 'Java', 'Python', 'HTML']
```

## Insert List Items:

- How to insert list items without replacing
- using insert() fun:
- It inserts items at the mentioned index.

```
Question: Create a list of 4 items and insert a new item at index 3
```

```py
colors = ["Red", "Blue" ,"Green","Black"]
print(colors)
colors.insert(3, "Orange")
print(colors)
```

```
['Red', 'Blue', 'Green', 'Black']
['Red', 'Blue', 'Green', 'Orange', 'Black']
```

## Append List Items:

- what is append() methods
- to add an item at the end of the list

```py
color = ["red","blue","green"]
print(colors)
colors.append("black")
print(colors)
```

```
['red', 'blue', 'green']
['red', 'blue', 'green', 'black']
```

## Extend List Items:

- what is extend() method used for?
- used to append or add items of another list to the end of current list

```py
colors = ["yellow","purple","green"]
rgb = ["red","blue","green"]
colors.extend(rgb)
print(colors)
```

```
['yellow', 'purple', 'green', 'red', 'blue', 'green']
```

- Extend can append any iterable object(list, tuples, set, dictionaries, etc).

```py
#extending tuple with list
colors = ["yellow","purple","green"]
rgb = ("red","blue","green")
colors.extend(rgb)
print(colors)
```

## Looping Through a List:

> For Loop:

```
 Print all list items using for loop:
```

```py
myList = [1,2,3,4]
for x in myList:
  print(x)
```

```
1
2
3
4
```

```
print  all list items using for loop by refering index number:
```

```py
cities = ["Delhi", "Mumbai", "Pune"]
length = len(cities)
for i in range(length):
  print(cities[i])
```

```
Delhi
Mumbai
Pune
```

> Using While Loop:

```
print all list items using while loop
```

```py
cities = ["Delhi","Mumbai","Pune"]
i = 0
length = len(cities)
while i < length:
  print(cities[i])
  i = i+1
```

# Sorting the Lists:

- sort(): built-in fun to sort list in ascending by default:

```py
#sort alphabetically
colors = ["red", "blue", "green","yellow","orange"]
colors.sort()
print(colors)
```

```py
#sort numerically
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)
```

```py
#Sort in descending
colors = ["red", "blue", "green","yellow","orange"]
colors.sort(reverse=False)
print(colors)
```

```py
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
```

# Copy Lists:

## List Comprehension:

- Process of reducing the syntax during looping through lists
- It helps when we create a new list based on the values of existing list
-
- Ex

```py
cities = ["Delhi","Mumbai","Pune"]
for x in cities:
  print(x)
```

- The above code can be reduced using list comphrension:

```py
cities = ["Delhi","Mumbai","Pune"]
[print(x) for x in cities]
```

# Tuples:

- used to store multiple items in a single variable.
- created using round brackets
- EX:

```py
myTuple = ("red", "blue", "green");
print(myTuple) #('red', 'blue', 'green')
```

- Tuple items are ordered, unchangeable , can have duplicates

# Dictionary

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
