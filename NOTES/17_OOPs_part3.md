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
