# PROGRAMS:

## Creating a Class:

```
Define a class named Employee with attributes name, company and id. Initialize these attributes using the __init__ method. Create an object of the class and print the student's details.
```

```py
class Employee:
    def __init__(self, name, company, id):
        self.name = name
        self.company = company
        self.id = id

emp = emp("John", "Amazon", 1234)
print("Name:", emp.name)
print("Company:", emp.company)

```

## Methods and Attributes:

```
Create a class Car with attributes make and model. Include a method called display_info that prints the car's make and model. Create two car objects and call the method on each of them.
```

```py
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Car Make:", self.make)
        print("Car Model:", self.model)

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()
```

## Program to count number of objects in a class:

```py
class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1
s1=Student()
s2=Student()
s3=Student()
print("The number of students:",Student.count)
```

## Instance Variables:

```
Define a class Rectangle with attributes width and height. Implement a method called calculate_area that calculates and returns the area of the rectangle. Create an object, set its dimensions, and print the calculated area.
```

```py
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())

print()
```

## Program to Find the Area and Perimeter of the Circle using classes:

```py
import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))
```

##

```
Create a class BankAccount with attributes account_number and balance. Include methods for depositing and withdrawing money, updating the balance accordingly. Create an object, perform some transactions, and print the final balance.
```

```py
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount("12345", 1000)
print("Initial Balance:", account.balance)
account.deposit(500)
account.withdraw(200)
print("Final Balance:", account.balance)

```

## Basic Calculator:

```
Define a class Calculator with methods for addition, subtraction, multiplication, and division. Use the __init__ method to initialize a starting value. Create an object and perform basic arithmetic operations.
```

```py
class Calculator:
    def __init__(self, value):
        self.result = value

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Cannot divide by zero")

calculator = Calculator(10)
calculator.add(5)
calculator.subtract(3)
calculator.multiply(2)
calculator.divide(4)
print("Result:", calculator.result)

```

## Program to Create a Class which all Basic Calculator Operations according to user's wish:

```py
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
```

## Python program to calculate Compund Interest using classes and objects:

```
- Formula : (P * (1 + r/100)^t) - P
```

```py
class CompoundInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        compound_interest = self.principal * (1 + self.rate / 100) ** self.time - self.principal
        return compound_interest

# Taking user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (years): "))

# Creating an instance of the CompoundInterestCalculator class
calculator = CompoundInterestCalculator(principal, rate, time)

# Calculating and displaying the compound interest
compound_interest = calculator.calculate()
print(f"Compound Interest: {compound_interest:.2f}")

```

## Program to print all prime numbers between an interval using classes and objects:

```py
class PrimeNumberFinder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(self):
        prime_numbers = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                prime_numbers.append(num)
        return prime_numbers

# Taking user input for the interval
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Creating an instance of the PrimeNumberFinder class
prime_finder = PrimeNumberFinder(start, end)

# Finding and printing prime numbers within the interval
prime_numbers = prime_finder.find_primes()
print("Prime numbers between", start, "and", end, "are:", prime_numbers)

```

## Program to Append, Delete and Display Elements of a List using Classes:

```py
class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n)

obj=check()

choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=int(input("Enter number to append: "))
        obj.add(n)
        print("List: ",obj.dis())

    elif choice==2:
        n=int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ",obj.dis())

    elif choice==3:
        print("List: ",obj.dis())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
```
