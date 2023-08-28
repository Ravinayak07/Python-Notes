# Python Encapsulation:

- Process of wrapping data and the methods within one unit.
- This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
- To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
- A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

- <img src="./encapsulation.png"/>

- The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

- Consider a real-life example of encapsulation, in a company, there are different sections like the :

```
1. accounts section
2. finance section
3. sales section etc.
```

- Now if an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section.
- He will first have to contact some other officer in the sales section and then request him to give the particular data.
- This is what encapsulation is.

## Public Members:

- These are accessible from anywhere, both within the class and outside of it.
- By default, all attributes and methods in a Python class are considered public.

```py
class MyClass:
    def __init__(self):
        self.public_attribute = 10

    def public_method(self):
        return "This is a public method."

obj = MyClass()
print(obj.public_attribute)  # Accessing public attribute
print(obj.public_method())   # Calling public method
```

## Protected members

- indicated by a single underscore prefix.
- Protected attribute or method should not be accessed outside the class or its subclasses, but it doesn't enforce this.
- Although the protected variable can be accessed out of the class as well as in the derived class (can also be modified too in derived class), it is convention to not access the protected out the class body.
- protected members are a way to indicate that certain attributes and methods of a class are intended for internal use within the class and its subclasses.

```py
class Parent:
class Parent:
    def __init__(self):
        self._value = 20 # Protected member

    def _protected_method(self):
        return "This is a protected method."

class Child(Parent):
    def __init__(self):

        super().__init__()

    def access_protected(self):
        print(self._value)
        print(self._protected_method())

    def modify(self):
        self._value = 30  # modifying
        print("After Modification: ", self._value)

obj1 = Parent()

# protected member/methods Can be accessed but should not be done due to convention
print(obj1._value)
print(obj1._protected_method())


obj2 = Child()

# acessing protected member/methods of Parent class from child class.
obj2.access_protected()

# Modifying protected members/methods of Parent class from child class
obj2.modify()
```

```
20
This is a protected method.
20
This is a protected method.
After Modification:  30
```

## Private members:

- Private attributes are defined using double underscores
- private members are class attributes and methods that are intended to be used only within the class they are defined in.
- They are not meant to be accessed or modified directly from outside the class.
- Private members provide a way to encapsulate internal functionality and data, reducing the risk of unintentional interference or modification by external code

```py
class Vehicle:
        name = "Ford"  # public attribute
        __price = "13 lakh"   # private Attribute

print(Vehicle.name) # Ford
print(Vehicle.price) # AttributeError
```

- private members cannot be accessed from the derived class too

```py
class Vehicle:
    def __init__(self):
        self.name = "Ford"
        self.__price = "13 lakh"   # private attribute

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def access(self):
        print(self.name)
        print(self.__price)

obj2 = Car()
obj2.access()
```

- However private members and methods can be indirectly accessed using name mangling.
- It's generally not recommended to do so, as it goes against the principle of encapsulation.

```py
class MyClass:
    def __init__(self):
        self.public_attribute = 10
        self._protected_attribute = 20
        self.__private_attribute = 30

    def __private_method(self):
        return "This is a private method."

obj = MyClass()

print(obj.public_attribute)                 # Accessing public attribute
print(obj._protected_attribute)             # Accessing protected attribute (not recommended)
#print(obj.__private_attribute)            # This would cause an AttributeError
# print(obj.__private_method())            # This would cause an AttributeError

# However, we can still access the private attribute:
print(obj._MyClass__private_attribute)
print(obj._MyClass__private_method())
```

- Remember that private members in Python are not meant for strict access control but rather as a convention to indicate that certain members are intended for internal use within the class. It's a good practice to respect the intended access level of these members to maintain code integrity and clarity.

## DATA ABSTRACTION:

- Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden.
- It allows you to create a clear distinction between the interface (how an object is used) and the implementation (how an object works internally). This separation enhances modularity, reduces complexity, and makes the code easier to maintain.
- Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.
- In Python, data abstraction is achieved through the use of abstract classes.

> ABSTRACT CLASSES:

- A class that consists of one or more abstract method is called the abstract class.
- Abstract methods do not contain their implementation.
- Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass.
- Abstraction is a key principle that allows you to define the structure and behavior of a class without providing a complete implementation
- Python doesn't provide the abstract class itself.
- We need to import the abc module, which provides the base for defining Abstract Base classes (ABC).
- The ABC works by decorating methods of the base class as abstract.
- We use the @abstractmethod decorator to define an abstract method
- If we don't provide the definition to the method, it automatically becomes the abstract method. Let's understand the following example
- Syntax:

```py
from abc import ABC
class ClassName(ABC):

# ABC : Abstract Base Class
```

- Example:

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area of shape: {shape.area()}")

```

- The Shape class is an abstract base class (ABC) that defines an abstract methods. It serves as a template for different shapes, ensuring that any child class inheriting from it must provide an implementation for the area method.

- Concrete Subclasses: The Circle and Rectangle classes inherit from the Shape class and provide concrete implementations for the area method. Each subclass calculates the area of the respective shape (circle or rectangle) based on its attributes.

- When you call the area method on each shape instance, the appropriate implementation from the respective subclass is executed, and you get the correct area calculation.
- In this example, abstraction is achieved by defining an abstract base class with an abstract method (Shape with area). Concrete subclasses (Circle and Rectangle) then inherit from the base class and provide specific implementations for the abstract method. This ensures a consistent interface while allowing flexibility in implementation details for different shapes.

> Points to remember

- An Abstract class can contain the both method normal and abstract method.
- An Abstract cannot be instantiated; we cannot create objects for the abstract class.

# WHAT is DSA:

- Stands for Data Strutures and Algorithms
- Data Structures means the way to organize data in main memory or RAM
- Algorithm is the sequqnce of steps to solve a problem

# WHY DSA:

- Makes us a better software developer
- When we solve a programming problem and if the problem requires to storage the data in the memory so that you can process the data.
- So to store the data there can be different ways. So different data structures teach us how do we efficiently store the data in the memory so that we can process the data faster and we can do the required operations fatser. Thats all data structures is about
- And algorithm is the sequence of steps to follow while solving the problem
- when you have a programming or business problem, there can be multiple ways to solve it
- For example there are meny meny algorithms to sort a sequence of data and these different algorithms can require different times of CPUs or different number of CPU cycles. And if you write an efficient code you can save a lot of CPU cycles. Hence you make a software better
- For example you are writing a software that takes sorted data from a web page from user and then gives you the results according to the search queries given by the input
- Andd if your code is inefficient it will take a lot of time to respond for slightly larger quieries
- So hence we learn DSA to write effiecient code that works faster and saves hardware cost, CPU cycles and makes the user experinece better.
- ALso helps to get a tech job
- Also helps in competitive coding(a sport)
- so DSA is pre requisite for a World class coder
- DSA is the core of hriring software developer. it is the fundamentals

# ROADMAP:

- First learn a programming language
- 4 most popular language people use to learn DSA or do competitive programming
- C++
- Java
- Python
- Javascript

# Best , Average and Worst Case

- Consider the below example:

```py
# program to find sum of elements of a list

mylist = [1,2,3,4]
n = len(mylist)
def getSum(mylist, n):

    sum = 0    # c2 (executes only once)

    for i in range(n):
        sum=sum+mylist[i]  # nc1 (becoz it executes linear number of times)

    return sum # c2 (executes only once)

# Time Taken: nc1 + c2
# order of growth = n i.e linear
```

- consider another example:

```py
mylist = [1,2,3,4]
n = len(mylist)
def getSum(mylist, n):

    if n%2 == 0:   # even sized list
        return 0

    sum = 0    # c2 (executes only once)

    for i in range(n):
        sum=sum+mylist[i]  # nc1 (becoz it executes linear number of times)

    return sum # c2 (executes only once)

```

- here we cannot make a general statement that the order of growth is linear or constant because it depends on the type of input i.e even or odd
- If user input is even sized array, it will take constant time
- If user input is odd sized array, it will take linear time
- Thats why divide algorithms into three cases: Best, Average and worst

> Best Case:

- Best Case: minimum number of growth of an algorithm

```
Best case = constant i.e when the user provides even sized list
```

- Best case is bogus.Not used that much

> Average Case:

- Average case = Time taken by all the inputs / Number of inputs
- Most of the time we don't know how many inputs user will provide. In those cases we take assumptions.
- So in this code we assume that user provides half of the time even input and half of the time odd input
- Half of the time = linear when user provides odd sized array
- Half of th time = constant when user provides even sized array.
- so time taken = ((c1n + c2) + c3) / 2 = c1n/2 + c2/2 + c3/2
- Ignore the lower order terms and constant. time taken = n i.e linear
- So avg case requires us to make certain assumptions in the input or in ideal situation, requires to know the exact input.
- So avg case is not typically considered

> Worst case:

- We find the input size for which the fun will take maximum time or order of growth
- In this case if the user provides odd sized list, it will take maximum time
- so worst case: linear
