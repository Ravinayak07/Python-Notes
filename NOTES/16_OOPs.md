# Introduction:

- Object Oriented Programming is a way of programming that uses classes and objects
- It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
- The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data

## OOPs Concepts in Python

- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

# Class:

- Class is a collection of object
- A class contains user-defined the blueprints or the prototype from which the objects are being created.
- It is a logical entity that contains some attributes and methods.
- Classes helps in bundling data and functionality together.
- Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.
- The class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class.
- A class is like a blueprint for an object.

> Need for creating classes:

- lets say you want to track the number of students in a college that have different name and age.
- For that you can create a list where first element will be students name and second will be his/her age.
- Like this there are 100 students and they also have some other properties like section,etc.
- Now how to track them???
- This way lacks organization
- Here is the need of classes

> class:

- created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
- Class definition Syntax:

```py
class ClassName:
   # Statement-1
   .
   .
   .
   # Statement-N
```

- creating an Empty Class:

```py
class Student:
    pass
```

```py
class Student:
    gender = "Male"
```

- Syntax: Object Definition

```
obj = ClassName()
print(obj.atrr)
```

# Objects:

- An Object is an instance of a Class
- A class is like a blueprint while an instance is a copy of the class with actual values
- It’s not an idea anymore, it’s an actual student, like a student of section A who’s seven years old. You can have many students to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required
- The object is an entity that has a state and behavior associated with it.
- It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
- Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
- More specifically, any single integer or any single string is an object.
- The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on.
- An object consists of:

```
State: It is represented by the attributes of an object. It also reflects the properties of an object

Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.

Identity: It gives a unique name to an object and enables one object to interact with other objects.
```

<img src="./obj1.png"/>
```
To understand the state, behavior, and identity let us take the example of the class Student (explained above).

The identity can be considered as the name of the student.

State or Attributes can be considered as the section, age, or height of the student.

The behavior can be considered as to whether the dog is studying or playing

````

- create an object of class student

```py
obj = Student()
````

> Declaring Claas Objects (Also called instantiating a class):

- When an object of a class is created, the class is said to be instantiated. All the instances share the attributes and the behavior of the class. But the values of those attributes, i.e. the state are unique for each object. A single class may have any number of instances
  <img src="./obj2.png"/>

- Example of Python Class and object
- Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.

```py
# Python3 program to
# demonstrate instantiating
# a class
class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
```

```
mammal
I'm a mammal
I'm a dog
```

- In the above example, an object is created which is basically a dog named Rodger. This class only has two class attributes that tell us that Rodger is a dog and a mammal.
- In this example, we are creating a Dog class and we have created two class variables attr1 and attr2. We have created a method named fun() which returns the string “I’m a, {attr1}” and I’m a, {attr2}. We have created an object of the Dog class and we are printing at the attr1 of the object. Finally, we are calling the fun()

# The Python Self:

- Self represents the instance of the class.
- By using the “self” we can access the attributes and methods of the class in Python.
- It binds the attributes with the given arguments.
- The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.
- Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
- If we have a method that takes no arguments, then we still have to have one argument.
- This is similar to this pointer in C++ and this reference in Java.

```
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
```

```py
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
```

```
Hello my name is John and I work in GeeksForGeeks.
```

- The Self Parameter does not call it to be Self, You can use any other name instead of it. Here we change the self to the word someone and the output will be the same.

```py
class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company

    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
```

```
Hello my name is John and I work in GeeksForGeeks.
```

- In this example, we are creating a GFG class and we have created the name, and company instance variables in the constructor. We have created a method named say_hi() which returns the string “Hello my name is ” + {name} +” and I work in “+{company}+”.”.We have created a person class object and we passing the name John and Company GeeksForGeeks to the instance variable. Finally, we are calling the show() of the class.

## What is the use of self in Python?

- When working with classes in Python, the term “self” refers to the instance of the class that is currently being used
- It is customary to use “self” as the first parameter in instance methods of a class.
- Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter.
- This enables you to modify the object’s properties and execute tasks unique to that particular instance.

```py
class mynumber:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj1 = mynumber(17)
obj1.print_value()
```

```
17
```

## Python Class self Constructor

- When working with classes, it’s important to understand that in Python, a class constructor is a special method named **init** that gets called when you create an instance (object) of a class.
- This method is used to initialize the attributes of the object
- Keep in mind that the self parameter in the constructor refers to the instance being created and allows you to access and set its attributes.
- By following these guidelines, you can create powerful and efficient classes in Python.

```py
class Subject:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


obj = Subject('Maths', 'Science')
print(obj.attr1)
print(obj.attr2)
```

```
Maths
Science
```

# Is self in Python a Keyword?

- No, ‘ self ‘ is not a keyword in Python. Self is just a parameter name used in instance methods to refer to the instance itself.
- In a more clear way you can say that SELF has the following Characteristic-

> Self: Pointer to Current Object

- The self is always pointing to the Current Object. When you create an instance of a class, you’re essentially creating an object with its own set of attributes and methods.

```py
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

> Example: Creating Class with Attributes and Methods:

- This code defines a Python class car representing cars with attributes ‘model’ and ‘color’. The **init** constructor initializes these attributes for each instance. The show method displays model and color, while direct attribute access and method calls demonstrate instance-specific data retrieval.

```py
class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model )
        print("color is", self.color )

# both objects have different self which contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

print("Model for audi is ",audi.model)
print("Colour for ferrari is ",ferrari.color)
```

```
Model is audi a4
color is blue
Model is ferrari 488
color is green
Model for audi is  audi a4
Colour for ferrari is  green
```

> Self in Constructors and Methods:

- Self is the first argument to be passed in Constructor and Instance Method.Self must be provided as a First parameter to the Instance method and constructor. If you don’t provide it, it will cause an error.

```py
# Self is always required as the first argument
class check:
    def __init__():
        print("This is Constructor")

object = check()
print("Worked fine")

# Following Error is produced if Self is not passed as an argument
Traceback (most recent call last):
  File "/home/c736b5fad311dd1eb3cd2e280260e7dd.py", line 6, in <module>
    object = check()
TypeError: __init__() takes 0 positional arguments but 1 was given
```

> Self: Convention, Not Keyword:

- Self is a convention and not a Python keyword. Self is a parameter in Instance Method and the user can use another parameter name in place of it. But it is advisable to use self because it increases the readability of code, and it is also a good programming practice.

```py
class this_is_class:
    def __init__(in_place_of_self):
        print("we have used another "
        "parameter name in place of self")

object = this_is_class()
```

```
we have used another parameter name in place of self
```

# The Python init Method :

- The **init** method is similar to constructors in C++ and Java.

## The Default **init** Constructor in C++ and Java:

- Constructors are used to initializing the object’s state.
- The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created
- Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation.
- Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
- It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
- Ex:

```py
# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()
```

```
Hello, my name is Nikhil
```

- In this example, we are creating a Person class and we have created a name instance variable in the constructor. We have created a method named as say_hi() which returns the string “Hello, my name is {name}”.We have created a person class object and we pass the name Nikhil to the instance variable. Finally, we are calling the say_hi() of the class.
- In the above example, a person name Nikhil is created.
- While creating a person, “Nikhil” is passed as an argument, this argument will be passed to the **init** method to initialize the object.
- The keyword self represents the instance of a class and binds the attributes with the given arguments.
- Similarly, many objects of the Person class can be created by passing different names as arguments.
- Below is the example of init in python with parameters
- Ex of init:

```py
# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')

p1.say_hi()
p2.say_hi()
p3.say_hi()
```

```
Hello, my name is Nikhil
Hello, my name is Abhinav
Hello, my name is Anshul
```

> **str**() method:

- Python has a particular method called **str**(). that is used to define how a class object should be represented as a string. It is often used to give an object a human-readable textual representation, which is helpful for logging, debugging, or showing users object information. When a class object is used to create a string using the built-in functions print() and str(), the **str**() function is automatically used. You can alter how objects of a class are represented in strings by defining the **str**() method.

```py
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."


my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)
```

```
My name is John and I work in GeeksForGeeks.
```

- In this example, We are creating a class named GFG.In the class, we are creating two instance variables name and company. In the **str**() method we are returning the name instance variable and company instance variable. Finally, we are creating the object of GFG class and we are calling the **str**() method.

> **init** with inheritance

- Inheritance is the capability of one class to derive or inherit the properties from some other class. Let’s consider the below example to see how **init** works in inheritance. :

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
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something


obj = B("Something")
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

##

- The **init** method is similar to constructors in C++ and Java.
- It is run as soon as an object of a class is instantiated.
- The method is useful to do any initialization you want to do with your object.
- Now let us define a class and create some objects using the self and **init** method.
- Creating a class and object with class and instance attributes

```py
class Student:

    # class attribute
    attr1 = "Boy"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Ravi = Student("Ravi")
Sinu = Student("Sinu")

# Accessing class attributes
print("Ravi is a {}".format(Ravi.__class__.attr1))
print("Sinu is also a {}".format(Sinu.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Ravi.name))
print("My name is {}".format(Sinu.name))
```

```
Ravi is a Boy
Sinu is also a Boy
My name is Ravi
My name is Sinu
```

> Creating Classes and objects with methods:

- Here, The Student class is defined with two attributes:
- attr1 is a class attribute set to the value “Boy”.
- Class attributes are shared by all instances of the class.
- init is a special method (constructor) that initializes an instance of the Student class. It takes two parameters: self (referring to the instance being created) and name (representing the name of the student).
- The name parameter is used to assign a name attribute to each instance of Student.
- The speak method is defined within the Student class. This method prints a string that includes the name of the student instance.
- The driver code starts by creating two instances of the Student class: Ravi and Sinu. The **init** method is called for each instance to initialize their name attributes with the provided names. The speak method is called in both instances (Ravi.speak() and Sinu.speak()), causing each student to print a statement with its name.

```py
class Student:

    # class attribute
    attr1 = "Boy"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Ravi = Dog("Ravi")
Sinu = Dog("Sinu")

# Accessing class methods
Ravi.speak()
Sinu.speak()
```

```
My name is Ravi
My name is Sinu
```

## Class and Instance Variables

- Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

- Defining instance variables using a constructor:

```py
# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
```

```
Rodger details:
Rodger is a dog
Breed:  Pug
Color:  brown
Buzo details:
Buzo is a dog
Breed:  Bulldog
Color:  black
Accessing class variable using class name
dog
```

- A class named Dog is defined with a class variable animal set to the string “dog”. Class variables are shared by all objects of a class and can be accessed using the class name. Dog class has two instance variables breed and color. Later we are creating two objects of the Dog class and we are printing the value of both objects with a class variable named animal.

> Defining instance variables using the normal method:

```py
# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):

        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
```

```
brown
```

- In this example, We have defined a class named Dog and we have created a class variable animal. We have created an instance variable breed in the constructor. The class Dog consists of two methods setColor and getColor, they are used for creating and initializing an instance variable and retrieving the value of the instance variable. We have made an object of the Dog class and we have set the instance variable value to brown and we are printing the value in the terminal.

# PYTHON INHERITANCE:

- Inheritance is the capability of one class to derive or inherit the properties from another class.
- The class that derives properties is called the derived class or child class
- The class from which the properties are being derived is called the base class or parent class
- The benefits of inheritance are:
- It represents real-world relationships well.
- It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

## Types of Inheritance:

- Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
- Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.
- Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
- Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.

## Example:

- we have created two classes i.e. Person (parent class) and Employee (Child Class).
- The Employee class inherits from the Person class
- We can use the methods of the person class through the employee class as seen in the display function in the above code
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
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

```

```
Rahul
886012
My name is Rahul
IdNumber: 886012
Post: Interns
```

# Inheritance in Python:

- One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.

## Benefits of inheritance are:

- Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class. The benefits of Inheritance in Python are as follows:

```
It represents real-world relationships well.

It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.

It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

Inheritance offers a simple, understandable model structure.

Less development and maintenance expenses result from an inheritance.
```

> Python Inheritance Syntax:

- The syntax of simple inheritance in Python is as follows:

```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

- Creating a Parent Class:

```
A parent class is a class whose properties are inherited by the child class. Let’s create a parent class called Person which has a Display method to display the person’s information.
```

```py
# A Python program to demonstrate inheritance
class Person(object):

  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
```

```
Satyam 102
```

- Creating a Child Class:

```
A child class is a class that drives the properties from its parent class. Here Emp is another class that is going to inherit the properties of the Person class(base class).
```

```py
class Emp(Person):

  def Print(self):
    print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
```

- Example of Inheritance in Python :

```
Let us see an example of simple Python inheritance in which a child class is inheriting the properties of its parent class. In this example, ‘Person’ is the parent class, and ‘Employee’ is its child class.
```

```py
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
```

```
Geek1 False
Geek2 True
```

> What is an object class in Python?:

- Like the Java Object class, in Python (from version 3. x), the object is the root of all classes.

```
In Python 3.x, “class Test(object)” and “class Test” are same.
In Python 2. x, “class Test(object)” creates a class with the object as a parent (called a new-style class), and “class Test” creates an old-style class (without an objecting parent).
```

> Subclassing (Calling constructor of parent class)

- A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class.
- Example: class subclass_name (superclass_name)
- In this example, ‘a’ is the instance created for the class Person. It invokes the **init**() of the referred class. You can see ‘object’ written in the declaration of the class Person. In Python, every class inherits from a built-in basic class called ‘object’. The constructor i.e. the ‘**init**’ function of a class is invoked when we create an object variable or an instance of the class.
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
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
```

```
Rahul
886012
```

> Python program to demonstrate error if we forget to invoke **init**() of the parent

- If you forget to invoke the **init**() of the parent class then its instance variables would not be available to the child class. The following code produces an error for the same reason.

```py
class A:
    def __init__(self, n='Rahul'):
        self.name = n

class B(A):
    def __init__(self, roll):
        self.roll = roll

object = B(23)
print(object.name)
```

```
Traceback (most recent call last):
  File "/home/de4570cca20263ac2c4149f435dba22c.py", line 12, in
    print (object.name)
AttributeError: 'B' object has no attribute 'name'
```

> The super() Function:

- The super() function is a built-in function that returns the objects that represent the parent class. It allows to access the parent class’s methods and attributes in the child class.
- Example: super() function with simple Python inheritance:
- In this example, we created the object ‘obj’ of the child class. When we called the constructor of the child class ‘Student’, it initialized the data members to the values passed during the object creation. Then using the super() function, we invoked the constructor of the parent class.

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

> Adding Properties:

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

## Different types of Python Inheritance:

- There are 5 different types of inheritance in Python. They are as follows:
- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above
- Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.
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

- Hierarchical inheritance More than one derived class can be created from a single base.
- Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance

> Private members of the parent class :

- We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class.
- In Python inheritance, we can make an instance variable private by adding double underscores before its name. For example:

```py
# Python program to demonstrate private members
# of the parent class

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

# Python Polymorphism:

- Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.
- This code demonstrates the concept of inheritance and method overriding in Python classes. It shows how subclasses can override methods defined in their parent class to provide specific behavior while still inheriting other methods from the parent class.

```py
class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

```

```
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
```

## Python Encapsulation:

- It describes the idea of wrapping data and the methods that work on data within one unit.
- This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
- To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

- A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
  <img src="./encapsulation.png"/>
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

## DATA ABSTRACTION:

- It hides unnecessary code details from the user. Also, when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
- Data Abstraction in Python can be achieved by creating abstract classes

# What is OOPs?

- In order to understand what is Object oriented Programming. We need to understand what are objects first

# What are objects?

- In order to understand objects..first we need to leran primitive data types first.

# What are primitive data types?

- Variables that store single and simple values
- Stores single piece of data of some kind
- Ex: Byte, Int, Float, Boolean, Double, Char.
- These data types were usefull till one extent.
- But when programs became large and complex, these data types were not that usefull.
- We needed variables to store simmillar types of data together.

## Classes & Objects:

- Class is an Object constructor or blueprint for creating objects
- "class" keyword is used to create class

```py
class Student:
    name = "Ravi"

print(Student)
```

```
<class '__main__.Student'>
```

- Objects are created using class name:

```py
class Student:
    name = "Ravi"

#creating object

obj1 = Student()
print(obj1.name)  # Ravi
```

- To understand the meaning of classes we have to understand the built-in **init**() function.

## The init Function:

```
- All classes have a function called __init__(), which is always executed when the class is being initiated.
- __init__() function is used to assign values to object properties
```

```
- Question: Create a class named Student and use **init**() function to assign values
```

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Student("Ravi", 23)

print(obj1.name) # Ravi
print(obj1.age) # 23
```

- The init function is called automatically every time the class is being used to create a new object.

## str() function:

- controls what should be returned when the class object is represented as string:
- without str function:

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Student("Ravi", 23)

print(obj1)
```

```
<__main__.Student object at 0x2afc51539100>
```

- With str() function:

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

obj1 = Student("Ravi", 23)

print(obj1) # Ravi(23)
```

> The Self parameter:

- self parameter refers to the current instance of the class.
- Used to access class variables.
- It can be named anything but it has to be the first parameter of any function in the class

```py
class Student:
    def __init__(x, name, age):
        x.name = name
        x.age = age

    def intro(xyz):
        print("My name is "+xyz.name)

obj1 = Student("Ravi", 23)

print(obj1.name)  # Ravi
print(obj1.age)  # 23

obj1.intro() # My name is Ravi
```

> Modify object properties

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Student("Ravi", 23)
obj1.age = 22
print(obj1.age) # 22
```

> Delete Object Properties

- using del keyword:

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Student("Ravi", 23)

del obj1.age # Deletes the age property

print(obj1.age)  # AttributeError: 'Student' object has no attribute 'age'

del obj1 # deletes the whole object
```

> The Pass Statement:

- Class definitions cannot be empty:
- To avoid error, use pass statement.

```py
class Student:
    pass
```
