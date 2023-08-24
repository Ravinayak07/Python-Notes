# INHERITANCE:

> Syntax:

```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

> composition rather than inheritance:

- In the below example, the Car class is not explicitly inheriting from the Vehicle class, but it's using a property (name) of the Vehicle class. This is a form of composition, where one class is composed of or uses another class as a component.
- This code doesn't involve explicit inheritance, but it shows how one class (Car) can use attributes from another class (Vehicle) through composition.

```py
class Vehicle:
    # class attribute
    name = "Mercedes"

class Car(Vehicle):
    def drive(self):
        return "I am driving "+Vehicle.name

car = Car()

print(car.drive()) # I am driving Vehicle
```

> Modifying the above code to involve inheritance between the Car class and the Vehicle

```py
class Vehicle:
    name = "Mercedes"

class Car(Vehicle):
    def drive(self):
        return "I am driving " + self.name

car = Car()

print(car.drive())
```

- The Vehicle class has a class attribute name set to "Mercedes".
- The Car class inherits from the Vehicle class and directly uses the name attribute within its drive() method.
- The drive() method of the Car class is called on the instance, and it uses the inherited name attribute from the Vehicle class to generate the output.
- This approach involves inheritance without using an **init** method and directly accesses the attributes from the parent class within the child class methods.
- The above code is simmilar to this in a way:

```py
class Vehicle:
    name = "Mercedes"

class Car(Vehicle):
    name = "Mercedes"
    def drive(self):
        return "I am driving " + self.name

car = Car()

print(car.drive())
```

- The local attribute takes precedence over the inherited attribute and overrides it:

```py
class Vehicle:
    name = "Mercedes"

class Car(Vehicle):
    name = "BMW"
    def drive(self):
        return "I am driving " + self.name

car = Car()

print(car.drive())
```

> Using init method:

```py
class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    def drive(self):
        return "I am driving "+self.name

car = Car("Mercedes")
print(car.drive())
```

- In the above code, The Vehicle class now has an **init** constructor that takes a name parameter and assigns it to the instance's name attribute.
- The Car class inherits from the Vehicle class, meaning it inherits the name attribute and constructor from the parent class.
- When you call the drive() method on the car instance, it uses the name attribute from the inherited Vehicle class to create the output "I am driving Mercedes".
- This way, you're using inheritance to share properties and methods between the parent Vehicle class and the child Car class.

> Proper Example of Inheritance

```py
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")

class Child(Parent):
    def introduce(self):
        print(f"My name is {self.name} and I'm the child.")

obj = Child()

obj.greet()       # Inherited from Parent class
obj.introduce()   # Defined in Child class
```

```
TypeError: Parent.__init__() missing 1 required positional argument: 'name'
```

- The Error is because when you create an instance of the Child class, it inherits the **init**() constructor from the Parent class. The **init**() constructor of the parent class requires a name argument, but you didn't provide it when creating the instance of the Child class.
- So the corrected code is:

```py
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")

class Child(Parent):
    def introduce(self):
        print(f"My name is {self.name} and I'm the child.")

obj = Child("Ravi")

obj.greet()       # Inherited from Parent class
obj.introduce()   # Defined in Child class
```

```
Hello, I am Ravi.
My name is Ravi and I'm the child.
```

## How to call Constructor of Parent class from child class.

> 1 . Using parentclass.**init**:

```py
class Person():

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

obj = Employee('Rahul', 1234, 50000, "Developer")

# calling a function of the class Person using its instance
obj.display1()
obj.display2()
```

> 5 . Error if we try to access the attributes of a parent class without invoking its **init**().

- If you forget to invoke the **init**() of the parent class then its instance variables would not be available to the child class.
- The following code produces an error for the same reason.

```py
class Person():

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


    def display2(self):
        print("Salary : ",self.salary)
        print("id number:",self.post)

obj = Employee('Rahul', 1234, 50000, "Developer")

# calling a function of the class Person using its instance
obj.display1()
obj.display2()
```

```
Name :  Rahul
id number: 1234
Salary :  20000
```

- While class A defines an **init** method that initializes the name attribute, class B overrides the **init** method without calling the parent class's **init** method.
- As a result, the name attribute is not being initialized in class B.

> Now what is The super() Function:

- The super() function is a built-in function that returns the objects that represent the parent class.
- It allows you to access methods and attributes of the parent class from the child class.

- You can call the constructor of the parent class from the child class using the super() function
- When you use super().**init**(), you are essentially calling the constructor of the parent class
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

```py
class Person():

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
        super().__init__(name, idnumber)

    def display2(self):
        print("Salary : ",self.salary)
        print("id number:",self.post)

obj = Employee('Rahul', 1234, 50000, "Developer")

# calling a function of the class Person using its instance
obj.display1()
obj.display2()
```

> Why we need to explicitly call Constructor of Parent class from child class

- IWhen a child class inherits from a parent class, it also inherits the parent's **init** method.
- In many cases, you might not need to explicitly call the parent's constructor using super(). The parent class's constructor will be automatically called when you create an instance of the child class. This is known as constructor chaining.
- However, there are situations where you might want to customize the initialization process in the child class while still retaining the behavior of the parent class's constructor. Using super() allows you to achieve this by calling the parent's constructor explicitly while adding any additional initialization specific to the child class.
- Here are some scenarios where calling the parent class's constructor from the child class using super() can be useful:

- 1. Additional Parameters: If the child class requires additional parameters in its constructor, you can use super() to call the parent's constructor with the necessary arguments.

```py
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child_instance = Child("Alice", 25)
print(child_instance.name)
print(child_instance.age)

```

- In this example, the Child class requires an additional parameter (age) in its constructor. By using super().**init**(name), the parent's constructor is called with the name parameter, and the child's constructor adds the age attribute.
- Using parent Name:

```py
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self,name)
        self.age = age

child_instance = Child("Alice", 25)
print(child_instance.name)
print(child_instance.age)
```

- Without:

```py
class Parent:
    def __init__(self, name,age):
        self.name = name
        self.age = age

class Child(Parent):
    pass

child_instance = Child("Alice", 25)
print(child_instance.name)
print(child_instance.age)
```

- 2. Initialization Order: If you need specific attributes to be set in a particular order, calling the parent's constructor ensures that the parent's attributes are initialized before the child's attributes.

```py
class Parent:
    def __init__(self):
        self.attribute = "Parent attribute"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = "Child attribute"

child_instance = Child()
print(child_instance.attribute)       # Accessing parent's attribute
print(child_instance.child_attribute) # Accessing child's attribute

```

```
Parent attribute
Child attribute
```

- Using super().**init**() ensures that the parent's attribute is initialized before the child's attribute

# Types of Inheritance:

- 1 . Single Inheritance: One class inherits from a single base class
- 2 . Multiple Inheritance: One class inherits from multiple base classes
- 3 . Multilevel Inheritance: one class derives from another base class which in turn derives from another class
- 4 . Hierarchical Inheritance: Several classes inherit from a single base class.
- 5 . Hybrid (or Mixed) Inheritance: A combination of multiple and hierarchical inheritance involving multiple base and derived classes

# Multiple Inheritance:

- When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.
  <img src="./multiple.png" style="width: 400px;"/>

> syntax:

```
Syntax:

Class Base1:
       Body of the class

Class Base2:
     Body of the class

Class Derived(Base1, Base2):
     Body of the class
```

```py
# base class 1
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def show_wheels(self):
        print("This vehicle has", self.wheels, "wheels.")

# base class 2
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started. Fuel type:", self.fuel_type)

# child class
class Car(Vehicle, Engine):
    def __init__(self, wheels, fuel_type):
        Vehicle.__init__(self, wheels)
        Engine.__init__(self, fuel_type)

    def drive(self):
        print("Car is moving.")

my_car = Car(4, "Gasoline")
my_car.show_wheels()
my_car.start()
my_car.drive()
```

```
This vehicle has 4 wheels.
Engine started. Fuel type: Gasoline
Car is moving.
```

# Multilevel Inheritance:

- one class derives from another base class which in turn derives from another class
- <img src="./multilevel.png" style="width: 300px;"/>

```py
# Base class
class Grandfather:
    def __init__(self, grandfather):
        self.grandfather= grandfather

# Intermediate class
class Father(Grandfather):
    def __init__(self, father, grandfather):
        self.father = father

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfather)


# Derived class
class Son(Father):
    def __init__(self, son, father, grandfather):
        self.son = son

        # invoking constructor of Father class
        Father.__init__(self, father, grandfather)

    def print_name(self):
        print('Grandfather:', self.grandfather)
        print("Father:", self.father)
        print("Son:", self.son)



s1 = Son('Prince', 'John', 'James')
s1.print_name()
```

```
Grandfather: James
Father: John
Son: Prince
```

> using super() function:

```py
# Base class
class Grandfather:
    def __init__(self, grandfather):
        self.grandfather= grandfather

# Intermediate class
class Father(Grandfather):
    def __init__(self, father, grandfather):
        self.father = father

        # invoking constructor of Grandfather class
        super().__init__(grandfather)


# Derived class
class Son(Father):
    def __init__(self, son, father, grandfather):
        self.son = son

        # invoking constructor of Father class
        super().__init__(father, grandfather)

    def print_name(self):
        print('Grandfather:', self.grandfather)
        print("Father:", self.father)
        print("Son:", self.son)



s1 = Son('Prince', 'John', 'James')
s1.print_name()
```

# Hierarchical Inheritance:

- When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance
- <img src="./hirarchical.png" style="width: 400px;"/>

```py
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)

class Rectangle(Shape):
    def __init__(self, color):
        super().__init__(color)

circle = Circle("red")
print("Circle: ",circle.get_color())


rectangle = Rectangle("blue")
print("Rectangle: ",rectangle.get_color())
```

```
Circle:  red
Rectangle:  blue
```

## Hybrid Inheritance:

- It combination of different types of inheritances
- <img src="./hybrid.png" style="height: 200px;"/>
- <img src="./hybrid2.png" style="height: 200px;"/>

```py
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()
```

- In the given code, the following types of inheritance are used:
- Single Inheritance: The base class School is inherited by the subclasses Student1 and Student2. This is a form of single inheritance where each subclass inherits from a single parent class.
- Multiple Inheritance: The class Student3 inherits from both Student1 and School classes. This is an example of multiple inheritance where a class inherits from more than one parent class.
- Multilevel Inheritance: The class Student3 is derived from the class Student1, which in turn is derived from the class School. This forms a chain of inheritance, resulting in multilevel inheritance.

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

## Python Encapsulation:

- It describes the idea of wrapping data and the methods that work on data within one unit.
- This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
- To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

- A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
  <img src="./encapsulation.png"/>
- The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

- Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc. The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of all the sales. Now there may arise a situation when due to some reason an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section. He will first have to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section
- In the above example, we have created the c variable as the private attribute. We cannot even access this attribute directly and can’t even change its value.

```py
# Python program to
# demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

```

```
GeeksforGeeks
```

> Protected members

- Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “\_”.
- Although the protected variable can be accessed out of the class as well as in the derived class (modified too in derived class), it is customary(convention not a rule) to not access the protected out the class body.
- Note: The **init** method is a constructor and runs as soon as an object of a class is instantiated.

```py
# Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):

        # Protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
```

```
Calling protected member of base class:  2
Calling modified protected member outside class:  3
Accessing protected member of obj1:  3
Accessing protected member of obj2:  2
```

> Private members:

- Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
- However, to define a private member prefix the member name with double underscore “\_\_”.
- Note: Python’s private and protected members can be accessed outside the class through python name mangling.

```py
# Python program to
# demonstrate private members

# Creating a Base class


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class
```

```
GeeksforGeeks
```

```
Traceback (most recent call last):
  File "/home/f4905b43bfcf29567e360c709d3c52bd.py", line 25, in <module>
    print(obj1.c)
AttributeError: 'Base' object has no attribute 'c'

Traceback (most recent call last):
  File "/home/4d97a4efe3ea68e55f48f1e7c7ed39cf.py", line 27, in <module>
    obj2 = Derived()
  File "/home/4d97a4efe3ea68e55f48f1e7c7ed39cf.py", line 20, in __init__
    print(self.__c)
AttributeError: 'Derived' object has no attribute '_Derived__c'
```

## DATA ABSTRACTION:

- It hides unnecessary code details from the user. Also, when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
- Data Abstraction in Python can be achieved by creating abstract classes
- Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because data abstraction is achieved through encapsulation.
- Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.

## Data Hiding and Object Printing:

> Data hiding:

- In Python, we use double underscore (Or \_\_) before the attributes name and those attributes will not be directly visible outside.

```py
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)

# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
print (myObject.__hiddenVariable)
```

```
2
7
Traceback (most recent call last):
  File "filename.py", line 13, in
    print (myObject.__hiddenVariable)
AttributeError: MyClass instance has
no attribute '__hiddenVariable'
```

- In the above program, we tried to access a hidden variable outside the class using an object and it threw an exception.
- We can access the value of a hidden attribute by a tricky syntax:

```py
# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 10

# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)
```

```
10
```

- Private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names

> Printing Objects:

- Printing objects give us information about objects we are working with. In C++, we can do this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class. In Java, we use toString() method.
  In python, this can be achieved by using **repr** or **str** methods.

```py
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s," \
              "b is %s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()
```

```
From str method of Test: a is 1234,b is 5678
[Test a:1234 b:5678]
```

> Important Points about Printing:

- If no **str** method is defined, print t (or print str(t)) uses **repr**.

```py
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
print(t)
```

```
Test a:1234 b:5678
```

> If no **repr** method is defined then the default is used:

```py
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Driver Code
t = Test(1234, 5678)
print(t)
```

```
<__main__.Test instance at 0x7fa079da6710>
```
