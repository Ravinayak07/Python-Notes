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
or()
```
