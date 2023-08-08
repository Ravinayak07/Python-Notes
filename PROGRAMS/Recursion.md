# Check Even or Odd Using Recursion:

```py
num = int(input("Enter th number : "))

def checkEvenOdd(num):
    #base condition
    if(num<2):
        return (n%2 == 0)
    return (checkEvenOdd(num-2))

if checkEvenOdd(num) == True:
    print("Even")
else:
    print("Odd")
```

- The base condition is that the number has to be lesser than 2.
- Otherwise the function is called recursively with the number minus

```py
def is_even(num):
    if num == 0:
        return True
    elif num == 1:
        return False
    else:
        return is_even(num - 2)

# Taking input from the user
num = int(input("Enter a number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

```

# Reverse a Number using Recursion:

```py
def reverse_number(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_number = number // 10
        reversed_number = reverse_number(remaining_number)
        return int(str(last_digit) + str(reversed_number))

number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
```

```py
"""
3. Otherwise, we extract the last digit of the number using the modulus operator % and obtain the remaining number by integer division // by 10.
4. We recursively call the reverse_number function on the remaining number to reverse it.
5. Finally, we concatenate the last digit with the reversed remaining number and convert it back to an integer.
"""
```

# Sum of Digits of a number using Recursion

```py
#user input
num = int(input("Enter a number: "))

#creating a list to store the digit
list=[]

def sumOfDigits(num):
    if num==0:
        return list #return the list if num is 0
    digit = num % 10
    list.append(digit) # adding digits to the list
    sumOfDigits(num//10) # passing num after dividing by 10

sumOfDigits(num) # fun call

print(sum(list)) # sum is a built-in function to add all items of an iterables(list, tuple, etc)
```
