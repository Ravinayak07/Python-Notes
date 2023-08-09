# Operators:

- Used to perform operations on variables and values.

## Types:

> 1 . Arithmetic:

```
+ , - , * , / , % , **(expoentiation), //(Floor Divison)
```

```py
x = 10
y = 3

print(x % y) # 1
print(x ** y) # 1000
```

> Differnce between / and //

- /(Regular divison):
- returns the result as floating point number
- Means includes the decimal even if it is whole numbers

```py
print(5/2) # 2.5
print(2/2) # 1.0
print(38/10) #  3.8
```

- //(Floor Divison):
- returns the result as integer number(no decimal part)
- returns largest integer which is <= result

```py
print(5//2) #  2
print(2//2) #  1
print(38//10) # 3.8
```

> 2 . Assignment:

```py
x = 5
x += 5 # x = x + 5
print(10)
```

```py
x = 10
x /= 3 # x = 10 /3
print(x) # 3.3333333333333335
```

```py
x = 5
x **= 3
print(x)
```

```py
# Bitwise AND
x = 5
x &= 3
print(x)

""""
5 (x)   =  101
3       =  011
--------------
x &= 3  =  001 (1 in decimal)
""""
```

- Bitwise or

```py
x = 5
x |= 3
print(x) # 7

""""
5 (x)   =  101
3       =  011
--------------
x |= 3  =  111 (7 in decimal)
""""
```

- Bitwise XOR(^) : 1 if bits are different

```py
x = 5
x ^= 3
print(x) # 6
```

```py
"""
5 (x)   =  101
3       =  011
--------------
x ^= 3  =  110 (6 in decimal)
"""
```

> 3 . Comparison Operators:

```
==, != , > , < , >= , <=
```

> 4 . Logical Operators:

```
and(&)
or(|)
not()
```

> 5 . Idenitity operators(is, is not):

- used to compare the objects
- doesnot compare whether they have equal value.
- it compares whether they are actually the same object i.e having same memory location.

```py
x = ["red", "blue"]
y = ["red", "blue"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y) # True
```

```py
x = ["red", "blue"]
y = ["red", "blue"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y) # False
```
