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

# Check If a Number is Palindrome

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

# Program to check prime number

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

# Program to check whether a number is perfect Number using function

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
