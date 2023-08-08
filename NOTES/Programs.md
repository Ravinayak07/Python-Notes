# Hello World!:

```py
print("Hello World!");
# print() : it is a built-in function display on the screen
```

# ADD TWO NUMBERS:

```py
num1 = 7
num2 = 8

sum = num1+num2;

print(sum)

# Using string formatting:
print("The Sum of %d and %d is %d " % (num1, num2, sum));

# ANother method
print("The sum of "+str(num1)+" and "+str(num2)+" is "+str(sum));

# Format method
print("The Sum of {0} and {1} is {2}".format(num1, num2, sum));

# Using f Strings(python 3.6+):
print(f"The sum of {num1} and {num2} is {sum}");
```

# ADD TWO NUMBERS (TAKE INPUT FROM THE USER):

**input()** : built-in function to take input from the user. It bydefault returns a string

```py
num1 = input("Enter first number: ")  # 7
num2 = input("Enter second number: ") # 8

sum = num1+num2  # 7+8 = 78

print(sum) # 78
```

> convert string input to integer:

- Method1:

```py
num1 = int(input("Enter first number: ")) #7
num2 = int(input("Enter second number: ")) #8

sum = num1+num2; # 7+8
print(sum) #15
```

- Method2:

```py
num1 = input("Enter first number: ")) # 7
num2 = input("Enter second number: ")) # 8

sum = int(num1)+int(num2); # 7+8
print(sum) #15
```

> For float numbers, Convert String input to float

```py
num1 = float(input("Enter first number: "))#9.9
num2 = float(input("ENter second number: ")) #8.9

sum = num1+num2 # 9.9+8.9
print(sum) # 18.8
```

- If we don't convert the numbers into float

```py
num1 = input("Enter first number: "))#4.5
num2 = input("ENter second number: ")) #6.8

sum = num1+num2 # 4.5+6.8
print(sum) # 4.56.8
```

- In one statement

```py
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))
```
