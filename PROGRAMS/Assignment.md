## 1. Python Program for nth multiple of a number in Fibonacci Series

```
Given two integers n and k. Find position the nth multiple of K in the Fibonacci series.
Examples:

Input: k = 2, n = 3
Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

Input: k = 4, n = 5
Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which appears at position 30.
```

```
For example, if you have k = 2 and n = 3, you need to find the third number in the Fibonacci series that is a multiple of 2. In this case, the Fibonacci series starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on. The third multiple of 2 in this series is 34, and it appears at the 9th position
```

```py
n = 3
k = 2

a = 0
b = 1
position = 1
count = 0

while True:
    c = a + b
    a = b
    b = c

    if c % k == 0:
        count += 1
        if count == n:
            break

    position += 1

print(position+1)


```

## 2. Sort the values of first list using second list in Python

```
Given two lists, sort the values of one list using the second list.

Examples:

Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
           list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]

Input : list1 = [“g”, “e”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “e”, “k”, “s”]
            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘g’, ‘k’, ‘r’, ‘e’, ‘e’, ‘g’, ‘s’, ‘f’, ‘o’]

```

```py
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

unique = list(set(list2))
unique.sort()
new = []
for i in unique:
    for j in range(0, len(list2)):
        if(list2[j] == i):
            new.append(list1[j])
print(new)
```

## 3. Maximum and Minimum K elements in Tuple

```
Input : test_tup = (3, 7, 1, 18, 9), k = 2
Output : (3, 1, 9, 18)

Input : test_tup = (3, 7, 1), k=1
Output : (1, 7)
```

```py
myTuple = (3, 7, 1, 18, 9)


print(myTuple)


K = int(input("Enter the k: "))

myList = list(myTuple)
myList = sorted(myList)
new = tuple(myList[:K] + myList[-K:])

print(str(new))


```

## 4. program to find N largest elements from a list:

```
Given a list of integers, the task is to find N largest elements assuming size of list is greater than or equal to N.

Input : [4, 5, 1, 2, 9]
        N = 2
Output :  [9, 5]

Input : [81, 52, 45, 10, 3, 2, 96]
        N = 3
Output : [81, 96, 52]
```

```py
myList=[]
num = int(input("Enter no. of items: "))
for i in range(num):
    item = int(input("Enter ELement: "))
    myList.append(item)

N = int(input("Value of N: "))
myList.sort()
print(myList[-N:])

```

## 5. Remove multiple elements from a list in Python

```
Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition.

Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]
```

## 6. Program to Count Number of Lowercase Characters , uppercase characters and spaces in a String:

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

## 7. Program to find Permutation of a given string using inbuilt function

```
A permutation, also called an “arrangement number” or “order”, is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation. Examples:

Input :  str = 'ABC'
Output : ABC
         ACB
         BAC
         BCA
         CAB
         CBA
```

```py
myStr= 'ABC'
permutations = [[]]
for a in myStr:
    new = []
    for x in permutations:
        for i in range(len(x) + 1):
            new.append(x[:i] + [a] + x[i:])
            permutations = new

for x in permutations:
    print(''.join(x))
```

## 8. Program to Count the Number of matching characters in a pair of string

```
Given a pair of non-empty strings. Count the number of matching characters in those strings (consider the single count for the character which have duplicates in the strings).

Examples:

Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5
(i.e. matching characters :- b, 1, 2, @, k)
```

```py
# intersection: returns a set that contains the similarity between two or more sets.

def myfun(str1,str2):
    x = (set(str1)).intersection(set(str2))
    return len(x)


myStr1="VISHAV"
myStr2="VANSHIKA"


res=myfun(myStr1.lower(),myStr2.lower())

print(res)

```
