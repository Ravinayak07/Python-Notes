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

> 4 . Subclassing (Calling constructor of parent class)

- A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class.
- Example: class subclass_name (superclass_name)
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

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
obj = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
obj.display()
```

```
Rahul
886012
```

> 5. Demonstrate error if we forget to invoke **init**() of the parent

- If you forget to invoke the **init**() of the parent class then its instance variables would not be available to the child class.
- The following code produces an error for the same reason.

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
    def __init__(self, n='Rahul'):
        self.name = n

class B(A):
    def __init__(self, roll, n='Rahul'):
        super().__init__(n)  # Call parent class's __init__ method
        self.roll = roll

obj = B(23)
print(obj.name)

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
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
```

```
Rahul 23
Mayank 23
```

> 7 . Adding Properties:

- One of the features that inheritance provides is inheriting the properties of the parent class as well as adding new properties of our own to the child class. Let us see this with an example:

```py
# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)

obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
```

- Here we can see that we added a new property to the child class, i.e., date of birth (dob)

```
Rahul 23
Mayank 23 16-03-2000
```

## Example:

- we have created two classes i.e. Person (parent class) and Employee (Child Class).
- The Employee class inherits from the Person class
- We can use the methods of the person class through the employee class as seen in the display function in the below code
- A child class can also modify the behavior of the parent class as seen through the details() method.

```py
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)

	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Ravi', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

```

```
Ravi
886012
My name is Ravi
IdNumber: 886012
Post: Interns
```

## Types of Inheritance:

- There are 5 different types of inheritance in Python.

> 1 . Single Inheritance:

- When a child class inherits from only one parent class

> 2 . Multilevel Inheritance:

- Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.
- Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

```py
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
```

```
Geek1 23 Noida
```

> 3 . Hierarchical Inheritance:

- Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
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
