# FUNCTIONS:

- Block of code
- Runs when called
- Data passed into functions are parameters:
- Created with **def** keyword.

```py
def greet():
    print("Hello World!")

greet()  #function call
```

> Arguments(or args):

- Data can be passed into functions as arguments
- Specified after fun name inside ().
- multiple arguments are separated by comma
- EX:

```py
def greet(name):
    print("Hello "+name);

greet("Ravi")
```

> Parameters(param) or Arguments:

- Both are same actually
- paramter is the variable inside () in fun defination
- Argument is the value sent during fun call
- Ex:

```py
def greet(firstName, lastName):
    print("Hello! My Name is "+firstName+ " "+lastName);

greet("Ravi", "Nayak")

# firstName,lastName : parameters
# "Ravi", "Nayak" : arguments
```

- Error:

```py
def greet(firstName. lastName):
    print(firstName+ " " +lastName);
greet("ravi");

# TypeError: greet() missing 1 required positional argument: 'lastName'
```

> Arbitary Arguments(\*args):

- If no. of argumenrts is unknown, add (\*) before parameter name in function def
- In this way, the fun will receive a tuple of arguments and can be accessed using index

```py
def progLanguages(*names):
    print("Now we are learning: "+names[1])
progLangueages("Java", "Python", "CPP")

# Now we are learning: CPP
```

> KeyWord Arguments:

- Arguments can be sent in key-value pairs
- In this way, order of arguments does not matter.

```py
def ipl2023(bro2, bro1, bro3):
    print("Eldest: "+bro1)
ipl2023(win="CSK", runner)
```
