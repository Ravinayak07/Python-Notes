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

# PROPERTIES OF SELF:

> 1 . Self: Pointer to Current Object

- The self is always pointing to the Current Object. When you create an instance of a class, you’re essentially creating an object with its own set of attributes and methods.

```py
# built-in id() function to print the memory address
class check:
    def __init__(self):
        print("Address of self = ",id(self))

obj = check()
print("Address of class object = ",id(obj))
```

```
Address of self =  140273244381008
Address of class object =  140273244381008
```

## Doc strings:

- In Python, classes can indeed have documentation strings, also known as docstrings.
- A docstring is a string literal that is the first statement in a class, function, module, or method definition. It's used to provide documentation and information about the purpose, usage, and behavior of the class or function.
- The docstring for a class can be accessed using the **doc** attribute of the class object i.e which can be accessed by using class-name.**doc**

```py
class MyClass:
    """
    This is a docstring for the MyClass class.
    It provides information about the class.
    """

    def __init__(self, value):
        self.value = value

# Accessing the class docstring
print(MyClass.__doc__)
```

## Class and Instance Variables

> Class Variables:

- Class variable function independently of any class methods and can be accessed through the use of the class name. Here's an illustration:

```py
class Person:
    count = 0   # This is a class variable

    def __init__(self):
        Person.count += 1   # Accessing the class variable using the name of the class
        print(Person.count)


print(Person.count)
obj = Person()
print(obj.count)
```

> Instance Variables:

- Whereas, instance variables are specific to each instance of a class. They are specified using the self-argument in the **init** method. Here's an illustration:

```py
class Person:
    def __init__(self, name):
        self.name = name    # This is an instance variable

person1 = Person("Ayan")
print(person1.name)

```

```
Ayan
```

- Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class.
  Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

# Two ways of declaring classes:

```py
#  new and modern way, most preferred and widely used
# recommend for python 3
class Car:
    pass
```

```py
# Also correct but old way
# used in python 2
class Car():
    pass
```

# OUTPUT:

```py
# Accessing class attribute using classname
class Car():

    name = "Mercedes"    # class attribute
    def drive(self):
        print("I am driving " + Car.name)

obj = Car()
obj.drive() # I am driving Mercedes
```

```py
# using the self parameter to access the class attribute through the instance.
class Car():

    name = "Mercedes"    # class attribute
    def drive(self):
        print("I am driving " + self.name)

obj = Car()
obj.drive() # I am driving Mercedes

obj2 = Car()
obj2.name = "BMW"
obj2.drive() # I am driving BMW
```

- The self parameter in a method refers to the instance of the class that the method is being called on. When you create an instance of a class, like obj = Car(), that instance is passed as the self parameter to any method you call on that instance.

- In your example, the name variable is defined as a class attribute outside of the drive method, using the Car class itself as its scope. This means that name is shared among all instances of the class, and it can be accessed using either the class name or an instance.

- When the drive method is called on the obj instance, the self parameter in the method receives the instance itself (obj in this case). So, when you use self.name inside the drive method, it refers to the class attribute name of the instance.

- If you were to modify the name attribute for a specific instance, it would not affect the name attribute for other instances or the default name attribute of the class.

- self.name refers to the name attribute of the instance car, which is inherited from the class attribute name. This way, you're using the instance's attribute through the self parameter to access the class attribute, achieving the same result as the original code but with a more object-oriented approach.

# Methods inisde init method:

```py
class MyClass:
    def __init__(self, value):
        self.value = value

        def inner_method():
            return self.value * 2

        self.result = inner_method()

# Create an instance of the class
my_object = MyClass(5)

# Access the result calculated within the inner method
print(my_object.result)  # Output: 10
```

- It is not a recommended practice and might lead to confusion and code complexity.
- In object-oriented programming, methods are typically defined outside the constructor (**init**) to promote better organization, readability, and separation of concerns.

# INHERITANCE:

- Inheritance is the capability of one class to derive or inherit the properties from another class.
- It specifies that the child object acquires all the properties and behaviors of the parent object.
- By using inheritance, we can create a class which uses all the properties and behavior of another class.
- The class that derives properties is called the derived class or child class
- The class from which the properties are being derived is called the base class or parent class.
- It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.
- The benefits of inheritance are:
- 1. It represents real-world relationships well.E.g ??
- 2. It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- 3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

> Syntax:

```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

- Example:

```py
class Vehicle:
    name = "Mercedes"

class Car(Vehicle):
    def drive(self):
        return "I am driving "+Vehicle.name

car = Car()

print(car.drive())
```

> 1 . First Create a Parent or Base Class:

- A parent class is a class whose properties are inherited by the child class.
- Let’s create a parent class called Person which has a Display method to display the person’s information.

```py
class Person(object):

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

# An Object of Parent class (Person)

obj1 = Person("Ravi")
obj1.display()     # Ravi
```

```
Ravi
```

> 2 . Now create a child or derived Class:

- A child class is a class that drives the properties from its parent class.
- Here Employee is another class that is going to inherit the properties of the Person class(base class).

```py
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

emp = Employee("Rahul")  # An Object of Employee

# Calling child class function
print(emp.isEmployee()) # True

# calling parent class function
emp.display() # Rahul
```

> 3 . Inheriting properties of parent class in child class:

- In this example, ‘Person’ is the parent class, and ‘Employee’ is its child class.

```py
class Person(object):

    def __init__(self, name):
        self.name = name

    # To get name
    def display(self):
        print(self.name)

# An Object of Parent class (Person)

obj1 = Person("Ravi")
obj1.display()     # Ravi

# Inherited or Child class
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

emp = Employee("Rahul")  # An Object of Employee

# Calling child class function
print(emp.isEmployee()) # True

# calling parent class function
emp.display() # Rahul

```

```
Ravi
True
Rahul
```

> 4 . How to call Constructor of Parent class from child class.

- A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class.
- Example: class childclass_name (Parentclass_name)
- In this example, ‘obj’ is the instance created for the class Employee. It invokes the **init**() of the referred class.
- You can see ‘object’ written in the declaration of the class Person. In Python, every class inherits from a built-in basic class called ‘object’. The constructor i.e. the ‘**init**’ function of a class is invoked when we create an object variable or an instance of the class.
- The variables defined within **init**() are called instance variables or objects. Hence, ‘name’ and ‘idnumber’ are the objects of the class Person. Similarly, ‘salary’ and ‘post’ are the objects of the class Employee. Since the class Employee inherits from class Person, ‘name’ and ‘idnumber’ are also the objects of class Employee.

```py
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display1(self):
        print("Name : ",self.name)
        print("id number:",self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def display2(self):
        print("Salary : ",self.salary)
        print("id number:",self.post)

# creation of an object variable or an instance
obj = Employee('Rahul', 1234, 50000, "Developer")

# calling a function of the class Person using its instance
obj.display1()
obj.display2()

```

```
Name :  Rahul
id number: 1234
Salary :  50000
id number: Developer
```

> 5 . Error if we try to access the attributes of a parent class without invoking its **init**().

- If you forget to invoke the **init**() of the parent class then its instance variables would not be available to the child class.
- The following code produces an error for the same reason.

```py

class Person(object):

    salary=20000
    # __init__ is known as the constructor
    def __init__(self, salary=50000):
        self.salary= Salary


    def display1(self):
        print("Salary : ",self.salary)  #Person.Salary also


# child class
class Employee(Person):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber


    def display2(self):
        print("Name : ",self.name)
        print("id number:",self.idnumber)

obj = Employee('Rahul', 1234)


obj.display2()
```

```
Name :  Rahul
id number: 1234
Salary :  20000
```

- When we call the init method:

```py

class Person(object):

    def __init__(self, salary=50000):
        self.salary= salary

    def display1(self):
        print("Salary : ",self.salary)  #Person.Salary also

class Employee(Person):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

        # invoking the __init__ of the parent class
        Person.__init__(self)

    def display2(self):
        print("Name : ",self.name)
        print("id number:",self.idnumber)

obj = Employee('Rahul', 1234)

obj.display2()
obj.display1()
```

```
Name :  Rahul
id number: 1234
Salary :  50000
```

```py
class A:
    def __init__(self, n='Rahul'):
        self.name = n

class B(A):
    def __init__(self, roll):
        self.roll = roll

obj = B(23)
print(obj.name)
```

```
Traceback (most recent call last):
  File "/home/de4570cca20263ac2c4149f435dba22c.py", line 12, in
    print (object.name)
AttributeError: 'B' object has no attribute 'name'
```

- The error you're encountering occurs because the class B does not have an attribute named name.
- While class A defines an **init** method that initializes the name attribute, class B overrides the **init** method without calling the parent class's **init** method.
- As a result, the name attribute is not being initialized in class B.
- To fix this issue, you should call the parent class's **init** method from within the B class's **init** method using the super() function

```py
class A:
    def __init__(self, n):
        self.name = n

class B(A):
    def __init__(self, roll, name):
        super().__init__(name)  # Call parent class's __init__ method
        self.roll = roll

obj = B(23,"Rahul")
print(obj.name)

```

```
Rahul
```

- In this corrected code, when you create an instance of class B, the **init** method of class B calls the **init** method of class A using super().**init**(n), which initializes the name attribute. This way, you won't encounter the "AttributeError" when trying to access obj.name

> 6 . Now what is The super() Function:

- The super() function is a built-in function that returns the objects that represent the parent class.
- It allows to access the parent class’s methods and attributes in the child class.
- Example: super() function with simple Python inheritance:
- In below example, we created the object ‘obj’ of the child class. When we called the constructor of the child class ‘Student’, it initialized the data members to the values passed during the object creation. Then using the super() function, we invoked the constructor of the parent class.

```py
# parent class
class Person():
  def __init__(self, name):
    self.PersonName = name

  def displayPerson(self):
    print("Person Name: ",self.PersonName)

# child class
class Student(Person):
  def __init__(self, name):
    self.StudentName = name

    # inheriting the properties of parent class
    super().__init__("Rahul")

  def displayStudent(self):
    print("Student Name: ", self.StudentName)

obj = Student("Ravi")
obj.displayPerson()
obj.displayStudent()
```

```
Person Name:  Rahul
Student Name:  Ravi
```

# POLYMORPHISIM:

- Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape.
- Polymorphism simply means having many forms.
- By polymorphism, we understand that one task can be performed in different ways.
- For example - lets say there is a class Vehicle, and all vehicles run. But they run differently. Here, the "run" behavior is polymorphic in a sense and depends on the vehicle. So, the abstract "vehicle" concept does not actually "run", but specific vehicles (like cars and bikes) have a concrete implementation of the action "speak".
- In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
- It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

> Example 1: Polymorphism in addition operator(t does not have a single usage.)

```py
# For integer data types, + operator is used to perform arithmetic addition operation.
num1 = 1
num2 = 2
print(num1+num2)

#  for string data types, + operator is used to perform concatenation.
str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)
```

- Here, we can see that a single operator + has been used to carry out different operations for distinct data types. This is one of the most simple occurrences of polymorphism in Python.

> Example 2: in-built polymorphic functions:

- len() function can run with many data types in Python

```py
# len() function is used for a string
print (len("Javatpoint"))

# len() function is used for a list
print (len([110, 210, 130, 321]))
```

```
10
4
```

> Examples 3: user-defined polymorphic functions::

```py
def add(p, q, r = 0):
    return p + q + r

print (add(6, 23))
print (add(22, 31, 544))
```

## Polymorphism with Class Methods:

- We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.
- Polymorphism allows objects of different classes to be treated as objects of a common superclass

```py
class Student1():
    def display(self):
        print("Name : Ravi")

class Student2():
    def display(self):
        print("Name : Darshan")

obj1 = Student1()
obj2 = Student2()
for obj in (obj1, obj2):
    obj.display()
```

- However, notice that we have not created a common superclass or linked the classes together in any way. Even then, we can pack these two different objects into a tuple and iterate through it using a common animal variable. It is possible due to polymorphism.
- This ability to treat different classes with a common interface (in this case, the display() method) is an example of polymorphism

## Polymorphism with Inheritance (Method Overriding):

- In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class(i.e the methods of the parent class are passed to the child class). However, it is possible to modify a method in a child class which it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

```py
class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def drive(self):
        print("Bike is riding")

# Create instances of the child classes
car = Car()
bike = Bike()

# Call the overridden methods
car.drive()  # Output: "Car is driving"
bike.drive()  # Output: "Bike is riding"
```

- In the above example: We have a Parent class Vehicle with a method drive().
- We have two child classes, Car and Bike, both inheriting from the parent class, Vehicle.
- Each child class overrides the drive() method to provide a specific message for the type of vehicle.
- When we create instances of the child classes and call the drive() method, the overridden methods in the child classes are used to indicate how each type of vehicle moves.
- This demonstrates method overriding by allowing the child classes to provide their own implementation of the drive() method based on their specific characteristics.

## Polymorphism with a Function and objects: :

- It is also possible to create a function that can take any object. This allows for polymorphism.
- In this example, let’s create a function called “func()” which will take an object which we will name “obj”.
- Next, let’s give the function something to do with the ‘obj’ object that we passed to it.
- In this case, let’s call the two methods, capital(), language(), each of which is defined in the two classes ‘India’ and ‘USA’.
- Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already.
- With those, we can call their actions using the same func() function:

```py
def func(obj):
    obj.capital()
    obj.language()

objIndia = India()
objUsa = USA()

func(objIndia)
func(objUsa)
```

> Code: Implementing Polymorphism with a Function :

```py
class India():
    def capital(self):
        print("Capital of India: New Delhi")

    def language(self):
        print("Lang of India: Hindi")

class USA():
    def capital(self):
        print("Capital of USA: Washington DC")

    def language(self):
        print("Lang of USA: Engliah")


def func(obj):
    obj.capital()
    obj.language()

objIndia = India()
objUsa = USA()

func(objIndia)
func(objUsa)
```

## Programs on Polymorphisim:

- Create a Parent class Animal with a method make_sound(). Create child classes Dog and Cat that override the make_sound() method to print different sounds. Demonstrate polymorphism by creating instances of both child classes and calling their make_sound() methods

```py
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Tiger(Animal):
    def make_sound(self):
        print("Roar!")

dog = Dog()
tiger = Tiger()

dog.make_sound()  # Output: Bark
tiger.make_sound()  # Output: Roar

```

- Design a payment system using polymorphism. Create a base class Payment with a method process_payment(). Implement subclasses CreditCardPayment and PayPalPayment with their own implementations of process_payment(). Demonstrate polymorphism by processing payments using different payment methods.

```py
class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processed credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processed PayPal payment of ${amount}")

credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.process_payment(100)  # Output: Processed credit card payment of $100
paypal.process_payment(50)        # Output: Processed PayPal payment of $50

```

- Develop a vehicle rental system using polymorphism. Create a base class Vehicle with methods like get_rental_price() and display_info(). Implement subclasses Car and Bike with their own implementations of these methods. Demonstrate polymorphism by calculating rental prices and displaying information for both vehicle types.

```py
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_rental_price(self):
        pass

    def display_info(self):
        print(f"{self.make} {self.model}")

class Car(Vehicle):
    def get_rental_price(self):
        return 50  # Sample rental price calculation

class Bike(Vehicle):
    def get_rental_price(self):
        return 20  # Sample rental price calculation

car = Car("Toyota", "Camry")
bike = Bike("Honda", "CBR")

car.display_info()       # Output: Toyota Camry
print(car.get_rental_price())  # Output: 50
bike.display_info()      # Output: Honda CBR
print(bike.get_rental_price()) # Output: 20

```

- Create a Parent class Shape with an abstract method calculate_area(). Implement child classes Rectangle and Circle that calculate and return their respective areas. Show polymorphism by calling the calculate_area() method on instances of both child classes.

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(rectangle.calculate_area())  # Output: 15
print(circle.calculate_area())     # Output: 50.24

```

## Types of Inheritance:

- There are 5 different types of inheritance in Python.

> 1 . Single Inheritance:

- When a child class inherits from only one parent class

> 2 . Multilevel Inheritance:

- Multi-level inheritance enables a derived class to inherit properties from an parent class which in turn inherits properties from his parent class.
- Its like child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

```py
class Parent(object):

    def __init__(self, name):
        self.name = name

    def displayName(self):
        return self.name


class Child(Parent):

    def __init__(self, name, age):

        self.age = age

        Parent.__init__(self, name)


    def displayAge(self):
        return self.age


class GrandChild(Child):

    def __init__(self, name, age, city):

        self.city = city

        Child.__init__(self, name, age)


    def displayCity(self):
        return self.city


obj = GrandChild("Ravi", 21, "BBSR")
print(obj.displayName())
print(obj.displayAge())
print(obj.displayCity())

```

```
Ravi
21
BBSR
```

- uisng superfun:

```py
class Parent(object):

    def __init__(self, name):
        self.name = name

    def displayName(self):
        return self.name


class Child(Parent):

    def __init__(self, name, age):

        self.age = age

        super().__init__(name)


    def displayAge(self):
        return self.age


class GrandChild(Child):

    def __init__(self, name, age, city):

        self.city = city

        super().__init__(name, age)


    def displayCity(self):
        return self.city


obj = GrandChild("Ravi", 21, "BBSR")
print(obj.displayName())
print(obj.displayAge())
print(obj.displayCity())

```

> 3 . Hierarchical Inheritance:

- More than one derived class can be created from a single base.

> 4 . Multiple Inheritance:

- When a child class inherits from multiple parent classes.
- Unlike Java, python shows multiple inheritances.:

```py
# Python example to show the working of multiple
# inheritance

class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
```

```
Base1
Base2
Derived
Geek1 Geek2
```

> 5 . Hybrid inheritance:

- This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance

## Private members of the parent class :

- We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class.
- In Python inheritance, we can make an instance variable private by adding double underscores before its name. For example:

```py
# Python program to demonstrate private members of the parent class

class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

object1 = D()

# produces an error as d is private instance variable
print(object1.c)
print(object1.__d)
```

- Here we can see that when we tried to print the variable ‘c’, its value 21 is printed on the console. Whereas when we tried to print ‘d’, it generated the error. This is because the variable ‘d’ is made private by using the underscores. It is not available to the child class ‘D’ and hence the error.

```
21
  File "/home/993bb61c3e76cda5bb67bd9ea05956a1.py", line 16, in
    print (object1.d)
AttributeError: type object 'D' has no attribute 'd'
```

## **init** with inheritance

- Let’s consider the below example to see how **init** works in inheritance. :

```py
# Python program to
# demonstrate init with
# inheritance

class A(object):
    def __init__(self, something):
        print("A init called", something)
        self.something = something


class B(A):
    def __init__(self, something):

        # Calling init of parent class
        A.__init__(self, something)
        print("B init called". something)
        self.something = something


obj = B("Ravi")
```

```
A init called
B init called
```

- So, the parent class constructor is called first. But in Python, it is not compulsory that the parent class constructor will always be called first. The order in which the **init** method is called for a parent or a child class can be modified. This can simply be done by calling the parent class constructor after the body of the child class constructor.

```py
# Python program to
# demonstrate init with
# inheritance

class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        print("B init called")
        self.something = something
        # Calling init of parent class
        A.__init__(self, something)


obj = B("Something")
```

```
B init called
A init called
```
