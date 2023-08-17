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

# Introduction:

- Python is an object-oriented Language

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
