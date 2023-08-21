# Introduction:

- Object Oriented Programming is a way of programming that uses classes and objects.
- The object is related to real-word entities such as book, house, pencil, etc
- The oops concept focuses on writing the reusable code. It is a widespread technique to solve the problem by creating objects.

## OOPs Concepts in Python

- Class
- Objects
- Methods
- Inheritance
- Polymorphism
- Encapsulation
- Data Abstraction

# Need for creating classes:

- Lets say you want to track the number of students in a college who have different name and gender
- For that you can create a list where first element will be students name and second will be his/her section.

```py
student1 = [name, gender]
```

- Like this there are 1000 students and they also have some other properties like section,stream,etc.

```py
students = [(name,gender, stream,...), (name,gender, stream,...), (name,gender, stream,...)........]
          #  student1                      student2                      student3 ...............student 10000
```

- Now how to track them???
- This way lacks organization
- Here is the need of classes

# Creating class and its object:

- created by keyword class followed by class name
- Class definition Syntax:

```py
class ClassName:
   # Statement-1
   .
   .
   .
   # Statement-N
```

- Example:

```py
class Student:
    name = "Ravi"
    gender = "Male"

```

- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

```py
class Student:
    name = "Ravi"
    gender = "Male"

print(Student.name)  # Ravi
print(Student.gender) # Male
```

> Creating Objects:

- Objects are created using class constructor
- Syntax: Object Definition

```py
obj = ClassName()
print(obj.atrr)
```

- create an object of class student

```py
class Student:
    name = "Ravi"
    gender = "Male"

obj1 = Student()
print(obj1.name)  # Ravi
print(obj1.gender) # Male
```

# Now Lets see the Definition of classes :

- Class is a collection of objects.
- A class contains user-defined blueprints or the prototype from which the objects are being created.
- It is a logical entity that contains some specific attributes(properties) and methods(functions).
- Classes helps in bundling data and functionality together.
- A class acts as a user-defined data structure that encapsulates both data members (attributes) and member functions (methods). By creating an instance of a class, you can access and utilize these data members and member functions.
- a class is a user-defined data type that contains both the data itself and the methods that may be used to manipulate it. In a sense, classes serve as a template to create objects. They provide the characteristics and operations that the objects will employ.
- Suppose a class is a prototype of a building. A building contains all the details about the floor, rooms, doors, windows, etc. we can make as many buildings as we want, based on these details. Hence, the building can be seen as a class, and we can create as many objects of this class.
- change this replacing with receipie and dish
- Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

- creating an Empty Class:

```py
class Student:
    pass
```

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

    def get_value(self):
        """This method returns the value stored in the object."""
        return self.value

# Accessing the class docstring
print(MyClass.__doc__)

```

# Objects:

- An Object is an instance of a Class.
- A class is like a blueprint while an instance is a copy of the class with actual values
- It’s not an idea anymore, it’s an actual student, like a student of section A who’s seven years old. You can have many students to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required
- The object is an entity that has a state(variables) and behavior(member function) associated with it.
- It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
- Everything in Python is an object, and almost everything has attributes and methods.
- Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
- More specifically, any single integer or any single string is an object.
- The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on.

- So An object consists of:
- 1. State: Represented by the attributes of an object. It also reflects the properties of an object
- 2. Behavior: Represented by the methods of an object. It also reflects the response of an object to other objects.
- 3. Identity: It gives a unique name to an object and enables one object to interact with other objects.
- To understand the state, behavior, and identity let us take the example of the class Student (explained above).
- 1. The identity can be considered as the name of the student.
- 2. State or Attributes can be considered as the section, age, or height of the student.
- 3. The behavior can be considered as to whether the studying is studying or playing

- <img src="./obj1.png" style="width: 500px;"/>

## Declaring Class Objects (Also called instantiating a class):

- When an object of a class is created, the class is said to be instantiated. All the instances share the attributes and the behavior of the class. But the values of those attributes, i.e. the state are unique for each object. A single class may have any number of instances
- <img src="./obj2.png" style="width: 500px;" />

- Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.

```py
class Student:

    # class Attributes
    name = "Ravi"
    gender = "Male"

    # A sample method
    def fun(self):
        print("My name is ", self.name)
        print("My gender is ", self.gender)


# Driver code
# Object instantiation
Ravi = Student()

# Accessing class attributes
# and method through objects
print(Ravi.name)
Ravi.fun()
```

```
Ravi
My name is Ravi
My Gender is Male
```

- In the above example, an object is created which is basically a student named Ravi. This class only has two class attributes that tell us that Ravi is a studnet and male.
- In this example, we are creating a Student class and we have created two class variables name and gender. We have created a method named fun() which returns the string.
- When we define a class, it needs to create an object to allocate the memory:

```py
class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

c1 = car("Toyota", 2016)
c1.display()
```

- In the above example, we have created the class named car, and it has two attributes modelname and year. We have created a c1 object to access the class attribute. The c1 object will allocate memory for these values

# Method:

- The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.

# The Python Self:

- Self represents the instance of the class.( Imagine the class as a recipe, and an instance as a dish made using that recipe.)
- By using the “self” we can access the attributes and methods of the class in Python.
- It binds the attributes with the given arguments.

- In Python, the self parameter is used within instance methods to refer to the instance itself. This parameter is not received automatically; rather, it's passed explicitly when you call an instance method.
- Thats why When we define an instance method in a class, we need to include self as the first parameter. This parameter represents the instance on which the method is being called. It gives us access to the instance's attributes and methods, allowing you to manipulate and interact with the instance's data.
- If we have a method that takes no arguments, then we still have to have one parameter as self.
- This is similar to this pointer in C++ and this reference in Java.

```py
class Student:

    # class Attributes
    name = "Ravi"
    gender = "Male"

    # A sample method
    def fun(self):
        print("My name is ", self.name)
        print("My gender is ", self.gender)


# Driver code
# Object instantiation
Ravi = Student()

# Accessing class attributes
# and method through objects
print(Ravi.name)
Ravi.fun()
```

- The Self Parameter does not call it to be Self, You can use any other name instead of it. Here we change the self to the word someone and the output will be the same.

```py
class Student:

    # class Attributes
    name = "Ravi"
    gender = "Male"

    # A sample method
    def fun(self):
        print("My name is ", self.name)
        print("My gender is ", self.gender)


# Driver code
# Object instantiation
Ravi = Student()

# Accessing class attributes
# and method through objects
print(Ravi.name)
Ravi.fun()
```

> What is the use of self in Python?

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

# Is self in Python a Keyword?

- No, ‘ self ‘ is not a keyword in Python. Self is just a parameter name used in instance methods to refer to the instance itself.
- In a more clear way you can say that SELF has the following Characteristic-

> 1 . Self: Pointer to Current Object

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

> 2 . Example: Creating Class with Attributes and Methods:

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

> 3 . Self in Constructors and Methods:

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

## Python Class self Constructor

- When working with classes, it’s important to understand that in Python, a class constructor is a special method named **init** that gets called when you create an instance (object) of a class.
- This method is used to initialize the attributes of the object
- Keep in mind that the self parameter in the constructor refers to the instance being created and allows you to access and set its attributes.
- By following these guidelines, you can create powerful and efficient classes in Python.

```py
class Student:

    def __init__(self, name, stream):
        self.name = name
        self.stream = stream


Ravi = Student('Ravi', 'CSE')
print(Ravi.name)
print(Ravi.CSE)
```

```
Ravi
CSE
```

# The Python init Method :

- The **init** method is similar to constructors in C++ and Java.
- In order to make an instance of a class in Python, a specific function called **init** is called. Although it is used to set the object's attributes, it is often referred to as a constructor.

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

- All instances of a class exchange class variables. They function independently of any class methods and may be accessed through the use of the class name. Here's an illustration:

```py
class Person:
    count = 0   # This is a class variable

    def __init__(self, name, age):
        self.name = name    # This is an instance variable
        self.age = age
        Person.count += 1   # Accessing the class variable using the name of the class
person1 = Person("Ayan", 25)
person2 = Person("Bobby", 30)
print(Person.count) # 2
```

- Whereas, instance variables are specific to each instance of a class. They are specified using the self-argument in the **init** method. Here's an illustration:

```py
class Person:
    def __init__(self, name, age):
        self.name = name    # This is an instance variable
        self.age = age
person1 = Person("Ayan", 25)
person2 = Person("Bobby", 30)
print(person1.name)
print(person2.age)
```

```
Ayan
30
```

- Class variables are created separately from any class methods and are shared by all class copies. Every instance of a class has its own instance variables, which are specified in the **init** method utilising the self-argument.

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

## ---------------------------------------------------------------------------------------------------------------

# INHERITANCE:

- Inheritance is the capability of one class to derive or inherit the properties from another class.
- It specifies that the child object acquires all the properties and behaviors of the parent object.
- By using inheritance, we can create a class which uses all the properties and behavior of another class.
- The class that derives properties is called the derived class or child class
- The class from which the properties are being derived is called the base class or parent class.
- It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.
- Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class
- The benefits of inheritance are:
- 1. It represents real-world relationships well.
- 2. It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- 3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
- 4. Inheritance offers a simple, understandable model structure.

> Syntax:

```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

- Example:

> 1 . First Create a Parent or Base Class:

- A parent class is a class whose properties are inherited by the child class.
- Let’s create a parent class called Person which has a Display method to display the person’s information.

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
emp = Person("Rahul", 102) # An Object of Person
emp.Display()
```

```
Rahul 102
```

> 2 . Now create a child or derived Class:

- A child class is a class that drives the properties from its parent class.
- Here Employee is another class that is going to inherit the properties of the Person class(base class).

```py
class Employee(Person):

  def Print(self):
    print("Employee class called")

Emp_details = Employee("Ravi", 11908621)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
```

> 3 . Inheriting properties of parent class in child class:

- In this example, ‘Person’ is the parent class, and ‘Employee’ is its child class.

```py
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
emp = Person("Ravi")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Rahuk")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
```

```
Ravi False
Rahul True
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

# POLYMORPHISIM:

- Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape.
- Polymorphism simply means having many forms.
- By polymorphism, we understand that one task can be performed in different ways.
- For example - lets say there is a class Vehicle, and all vehicles run. But they run differently. Here, the "run" behavior is polymorphic in a sense and depends on the vehicle. So, the abstract "vehicle" concept does not actually "run", but specific vehicles (like cars and bikes) have a concrete implementation of the action "speak".
- In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
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

> Example of inbuilt polymorphic functions::

```py
# Python program to demonstrate in-built poly-
# morphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))
```

```
5
3
```

> Examples of user-defined polymorphic functions: :

```py
# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0):
    return x + y+z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))
```

```
5
9
```

## Polymorphism with class methods:

- The below code shows how Python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.

```py
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
```

```
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
```

## Polymorphism with Inheritance (Method OPverriding):

- In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

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

> Polymorphism with a Function and objects: :

- It is also possible to create a function that can take any object, allowing for polymorphism. In this example, let’s create a function called “func()” which will take an object which we will name “obj”. Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. Next, let’s give the function something to do that uses the ‘obj’ object we passed to it. In this case, let’s call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. With those, we can call their action using the same func() function:

```py
def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
```

> Code: Implementing Polymorphism with a Function :

```py
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
```

```
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
```

## Simple example of polymorphism:

> polymorphism in Python using inheritance and method overriding:

```py
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]

# Call the speak method on each object
for animal in animals:
    print(animal.speak())
```

```
Woof!
Meow!
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

## FREECODECAMP (STRORE MANAGEMENT SYSTEM)

- Tracking items that we have in our store using variables

```py
item1 = "Phone"
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

# these variables are instances of different classes
print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))
```

```
<class 'str'>
<class 'int'>
<class 'int'>
<class 'int'>
```

- So in python, each data type is an object that has been instantiated earlier by some class
- In the above example, variable item1 has been instantitaed from a string type of class. Similarly other three variables are instantiated from a int type of class.
- Now it could have been nicer if we could create a data type of our own. It will allow us to write a code that we can reuse in the future easily if needed.
- Now each instance have attributes to describe information related about it.
- Instantiate some objects of a class is same as creating some objects of a class

> Creating class and objects

```py
class Item:
    pass

item = Item()

"""
same as
myStr = str(4)
"""
```

> now creating attributes:

- using dot sign
- Each of the 4 variables are assigned to one instance of the class

```py
class Item:
    pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
```

```
<class '__main__.Item'>
<class 'str'>
<class 'int'>
<class 'int'>
```

> creating methods inside instances

- methods are functions created inside classes
- self is the paramter that python wants us to recieve intentionally
- This is because python passes the object itself as the first argument when you call the methods
- Thats why we are not allowed to create methods that doesnot receive paramters

```py
class Item:
    def calculate_total_price():
        pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item1.calculate_total_price()
```

```
TypeError: Item.calculate_total_price() takes 0 positional arguments but 1 was given
```

- This shows that python tries to pass one argument and you are not receiving it using any paramter.
- Thats why you always have to receive one parameter while creating methods.
- Since it always receive this parameter, we call it self

```py
class Item:
    def calculate_total_price(self):
        pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item1.calculate_total_price()
```

```
No Error
```

- Now pass more parameter to calculate the price

```py
class Item:
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(item1.calculate_total_price(item1.price, item1.quantity)) # 500

# item1 passed as self
# item1.price passed as x
# item1.quantity passesd as y
```

- Multiple instances:

```py
class Item:
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(item1.calculate_total_price(item1.price, item1.quantity)) # 500

class Item:
    def calculate_total_price(self, x, y):
        return x*y

item2 = Item()
item2.name = "Phone"
item2.price = 1000
item2.quantity = 3

print(item2.calculate_total_price(item2.price, item2.quantity)) # 3000
```

> problem1:

- for each item of an instance , we need to hard code in the attribute name. Like:

```py
item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
```

- Here comes a special method named init method which is also called as constructor:
- Now when you create an instance of a class, python automatically executes this method and performs all the actions inside this method.
- for example:

```py
class Item:
    def __init__(self):
        print("init Method Executed")

item1 = Item()
```

```
init Method Executed
```

- This will get execute every time an object(or instance) is created.

```py
class Item:
    def __init__(self):
        print("init Method Executed")

item1 = Item()
item2 = Item()
```

- Now how to avoid hard coding the attributes:
- Since we got to know that every time an instance is created, the init method gets executed.
- We can use this to receive certain parameters , along with self(since it is mandatory)
- For example: lets pass the name attribute

```py
class Item:
    def __init__(self, name):
        print(f"An Instance Created: {name}")

item1 = Item("Phone")
item1.name = "Phone"

item2 = Item("Laptop")
item2.name = "Laptop"
```

```
An Instance Created: Phone
An Instance Created: Laptop
```

- now we can dynamically assign the atrributes inside the init method.

```py
class Item:
    def __init__(self, name):
        self.name = name
        print(f"An Instance Created: {name}")

item1 = Item("Phone")
item2 = Item("Laptop")

print(item1.name)
print(item2.name)
```

```
An Instance Created: Phone
An Instance Created: Laptop
Phone
Laptop
```

- Similarily doing the same for all atributes:

```py
class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone",1000,5)
item2 = Item("Realme",1000,3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
```

```
Phone
Realme
1000
1000
5
3
```

- Default parameters:

```py
class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone",1000)
item2 = Item("Realme",1000)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
```

```
Phone
Realme
1000
1000
0
0
```

- You can add some attributes specially for some instances
- Like: check whether a laptop has numpad or not:

```py
class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone",1000)
item2 = Item("Realme",1000)

item2.has_numpad = False
```

- We aldo don't need to pass x,y. We can use self since we are passing the object iteslf as self parameter:

```py
class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, 2)
item2 = Item("Realme",1000, 3)

print(item1.calculate_total_price()) #2000
print(item2.calculate_total_price()) #3000
```

- See what happens if i pass the price values as string types:

```py
class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone","1000", 2)
item2 = Item("Realme","1000", 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
```

```
10001000
100010001000
```

- Thus, We need to validate the data types of the values that we are passing in.
- There different ways to do this:
- First one is mentioning the type of data that is receiving:

```py
class Item:
    def __init__(self,name: str,price: float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, 2)

# with float mentioned, we can pass int alos
# since default value of quantity is 0, no need to mention
# integer
```

- Adding more validation:
- Suppose letssay we don't want to receive a negative number for price and quantity.
- This cannot acheived by typing.
- For that we will use assert statements
- Its is a statement to check what is happening to your expectations.

```py
class Item:
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, 2)
print(item1.calculate_total_price()) # 2000
```

- now if we pass negative numbers, it will show errors:

```py
class Item:
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, -2)
print(item1.calculate_total_price())
```

```
AssertionError
```

- With assert statements we can add our own exception messages:

```py
class Item:
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, -2)
print(item1.calculate_total_price())
```

```
AssertionError: Quantity -2 is not greater than zero !
```

- Till now what we learnt are instance attributes.
- Now consider a situation that you want to make use of an attribute that is global(i.e used across all instances)
- Those attributes are called class attributes
- Class attribute is an attribute that is going to be belong to the class itself. But you can also access this attribute from the instance level as well
- Ex: creating a class attribute:

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, 2)

# Accessing class atrribute from class level:
print(Item.pay_rate) # 0.8

# Accessing class attributes from instance level:
print(item1.pay_rate) # 0.8
print(item2.pay_rate) # 0.8
```

- This might be little confusing:

```
print(item1.pay_rate) # 0.8
print(item2.pay_rate) # 0.8
```

- these two statements will first check for the attribute in the instance level(i.e inside the init method)
- If it doesnot find there, then it will check in class level
- Now there is a built-in magic attribute(**dict**) with which we can see all the attributes that are belonging to that specific object

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Phone",1000, 2)
print(Item.pay_rate) # Print all the attributes of class level
print(item1.pay_rate) # Print all the attributes of instance level
```

```
{'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x7f0ca69a6c00>, 'calculate_total_price': <function Item.calculate_total_price at 0x7f0ca69a6ca0>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
{'name': 'Phone', 'price': 1000, 'quantity': 2}
>
```

- It returns all the attributes in a dictionary form. That why it is named so.

- Adding discount function:

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone",100, 2)
item1.apply_discount()
print(item1.price) #80.0
```

- Now lets say you want to give a different discount of 30% for laptop only. If we change the pay_rate at class level from 0.8 to 0.7 , it will affect all
- So the solution is:

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone",100, 2)
item1.apply_discount()
print(item1.price) #80.0

item2 = Item("Laptop",1000,3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) # 700.0

```

- So here for second item, since we are mentioning pay_rate at instance level, it should take that value and will not check at class level.
- But it still printing 20% discount. This is because inside discount function, we have mentioned Item.pay_rate
- Need to mention self.pay_rate
- Now since self is mentioned, for both the items, it will first check the value of pay_rate at instance level.
  For item1 at instance level, it will not find the value, so it will pull it from class level

- Now consider you have a large shop having more items. Currently in the class, we don't have any resource where we can access all items that we have in our shop.
- currently there is not an approach thet will give us a list with five different elements where each element will represent an instance of a class.
- So for this, we could create a class attribute that could name all:

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append every time an instance is created
        # uaing class object first
        Item.all.append(self)
        # self is the instance that is everytime created

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone",100, 2)
item2 = Item("Laptop",1000,3)
item3 = Item("Earbuds",500,1)

print(Item.all) # will print list of 3 instances
```

```
[<__main__.Item object at 0x7f0189582c50>, <__main__.Item object at 0x7f0189582c90>, <__main__.Item object at 0x7f0189582cd0>]
```

- The output is not too user friendly
- It would be nicer if we could change the way the object is being represented in this list here
- This can be acheived by a magic method called --repr--:
- It stands for representing your objects. There is also another method like this(**str**)

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append every time an instance is created
        # uaing class object first
        Item.all.append(self)
        # self is the instance that is everytime created

    def calculate_total_price(self):
        return self.price*self.quantity

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone",100, 2)
item2 = Item("Laptop",1000,3)
item3 = Item("Earbuds",500,1)

print(Item.all) # will print list of 3 instances
```

```
[Item('Phone','100','2'), Item('Laptop','1000','3'), Item('Earbuds','500','1')]
```

- Lets say we want to print all names of the instances:
- We can do it using a for loop

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0):

        # Run validations to received arguments:
        assert price >= 0, f"Price {price} is not greater than zero !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append every time an instance is created
        # uaing class object first
        Item.all.append(self)
        # self is the instance that is everytime created

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone",100, 2)
item2 = Item("Laptop",1000,3)
item3 = Item("Earbuds",500,1)

print(Item.all) # will print list of 3 instances

for instance in Item.all:
    print(instance.name)
```

```
Phone
Laptop
Earbuds
```

# Notes:

- OOPs helps to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
- How these are real world entities. We will explain it later.
- The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data
-

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

# Differenc between Object-oriented and Procedural Programming:

```
- Object-oriented programming is the problem-solving approach and used where computation is done by using objects.

- Procedural programming uses a list of instructions to do computation step by step
```

```
Object-oriented programming makes the development and maintenance easier.

In procedural programming, It is not easy to maintain the codes when the project becomes lengthy.
```

```
Object-oriented programming simulates the real world entity. So real-world problems can be easily solved through oops.

procedural programming doesn't simulate the real world. It works on step by step instructions divided into small parts called functions.
```

```
Object-oriented programming provides data hiding. So it is more secure than procedural languages. You cannot access private data from anywhere.

Procedural language doesn't provide any proper way for data binding, so it is less secure.
```

```
Example of object-oriented programming languages is C++, Java, .Net, Python, C#, etc.

Example of procedural languages are: C, Fortran, Pascal, VB etc.
```
