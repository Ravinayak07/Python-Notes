# Programs:

- Program to print Sum of squares of first n natural numbers

```py
n = int(input("Enter The number: "))

def squareSum(n):
	sum = 0
	for i in range(1, n+1):
		sum = sum + (i * i)

	return sum
print(squareSum(n))
```

- 2 . Program to check whether a number is Strong Number or Not.

```
A Strong number is a special number whose sum of the all digit's factorial should be equal to the number itself.
Ex:
num = 145
1! = 1
4! = 4*3*2*1 = 24
5! = 120
sum = 1+24+120 = 145.

Hence, It is a Strong Number
```

```py

sum=0
num=int(input("Enter a number:"))
temp=num

while(num):
    i=1
    fact=1
    rem=num%10

    while(i<=rem):
        fact=fact*i
        i=i+1

    sum=sum+fact
    num=num//10

if(sum==temp):
    print("Strong number")
else:
    print("Not a strong number")

```

- 3 . Print this Pattern:

```
* * * * *
  * * * *
    * * *
      * *
        *

(Here n=5)
```

```py
n = int(input("Enter the value of n: "))
for x in range(5, 0, -1):
    for y in range(x,5):
        print(" ",end="")
    for z in range(0,x):
        print("*",end="")
    print()
```

- 4 . Print this Pattern

```
* * * * *
 * * * *
  * * *
   * *
    *

(Here n=5)
```

```py
n = int(input("Enter the value of n: "))
for x in range(n, 0, -1):
    for y in range(x,n):
        print(" ",end="")
    for z in range(0,x):
        print("* ",end="")
    print()
```

- 5 . Print this Pattern

```
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

(Here n=5)
```

```py
n = int(input("Enter the value of n: "))
for x in range(n,0,-1):
    for y in range(n,0,-1):
        print(y, end="")
    print()
```

- 6 . Program to find the second Largest Number in a list entered by user

```py
list=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    item=int(input("Enter element:"))
    list.append(item)

print("List: ",list)
list.sort()
print("After sorting: ",list)
print("Second Largest is:",list[num-2])
```

- 7 . Program to Find the Largest Even and Largest Odd Number in a list

```py
list=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    item=int(input("Enter Element: "))
    list.append(item)
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print("Largest Even number:",even[len(even)-1])
print("Largest odd number: ",odd[len(odd)-1])
```

- 8 . Program to check whether a Number is Armstrong or Not.

```
Armstrong Number is a Number such that the sum of the cubes of its digits is equal to the number itself. Armstrong numbers are 0, 1, 153, 370, 371, 407, etc.

Ex:.
153 = 1*1*1 + 5*5*5 + 3*3*3
    = 1 + 125 + 27
    = 153
```

```py

num = int(input("Enter a number: "))

sum = 0

temp = num
while num > 0:
   digit = num % 10
   sum += digit ** 3
   num //= 10

if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")

```

# OUTPUT:

- 1

```py
for i in range(5):
    print(i)
```

```
0
1
2
3
4
```

- 2

```py
for i in range(1,2,3):
    print(i)
```

```
1
```

- 3

```py
for i in range(10, 2, -2):
  print(i, "Hello")
```

```
10 Hello
8 Hello
6 Hello
4 Hello
```

- 4

```py
for i in range(7, -2, -9):
  for j in range(i):
    print(j)
```

```
0
1
2
3
4
5
6
```

- 5

```py
x=1234
while x%10:
  x=x//10
  print(x)
```

```
123
12
1
0
```

- 6

```py
n=30
for i in range(2,n//4):
  if n%i == 0:
    print("thon")
  else:
    print("Bye")
```

```
thon
thon
Bye
thon
thon
```

- 7

```py
for i in [10,20,30]:
  print("Hello", i)
```

```
Hello 10
Hello 20
Hello 30
```

- 8

```py
x = 7
for i in range(x):
  if x==5:
    break
  print("H")
print(x)
```

```
H
H
H
H
H
H
H
7
```

- 9

```py
L = [13, 12, 21, 16, 35, 7, 4]
s=5
s1=3
for i in L:
  if i%4==0:
    s=s+i
    continue
  if i%7==0:
    s1=s1+i
print(s, end="")
print(s1)
```

```
3766
```

- 10

```py
count = 1

def doThis():
  global count

  for i in (1)
```

```
Error
```

- 11

```py
mylist = [5,7,8,1,8]
mylist.sort()
print(mylist)
```

```
[1, 5, 7, 8, 8]
```

- 12

```py
mylist = [5,7,8,1,8]
mylist.sort(reverse=False)
print(mylist)
```

```
[1, 5, 7, 8, 8]
```

- 13

```py
def sorting(num):
  return len(str(num))

numbers = [123, 4567, 89, 12, 34567]
print(numbers)
```

```
[123, 4567, 89, 12, 34567]
```

- 14

```py
fruits = ["apple","orange","mango","banana"]
print(fruits.sort())
print(fruits.sort(reverse=False))
```

```
None
None
```

- 15

```py
fruits = ["apple","orange","mango","banana"]
print(fruits[-4:-1])
print(fruits[-4:])
print(fruits[:4])
```

```
['apple', 'orange', 'mango']
['apple', 'orange', 'mango', 'banana']
['apple', 'orange', 'mango', 'banana']
```

- 16

```py
i = 5
while True:
  if i%0011 == 0:
    break
  print(i)
  i=i+1
```

```
SyntaxError
```

- 17

```py
x=5
while(x<15):
  print(x**2)
  x+=3
```

- 18

```py
for i in range(5):
  for j in range(i):
    print("A", end="")
  print()
```

```
A
AA
AAA
AAAA
```

- 19

```py
num = 7
for i in 7:
  print(num)
```

```
Error
```

- 20

```py
s1 = "silicon Institute"
count=0
for x in s1:
  if x!="i":
    count+=1
print(count)
```

```
14
```
