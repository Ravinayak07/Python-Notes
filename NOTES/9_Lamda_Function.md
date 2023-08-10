# Lamda Function:

- Anonymous function (which no name)
- Created using "lambda" keyword
- It takes any number of arguments but can have only one expression
- Syntax:

```
lambda arguments : expression
```

- Ex:

```py
res = lambda x : x * 10
print(res(5))  # 50

"""
here,
x : argument
x*10 : expression
"""
```

- With multiple arguments

```py
res = lamda x,y : x*y
print(res(10,20))  #200

```

```py
res = lambda x,y,z : x*y*z
print(res(2,3,4))  #24
```

> Using Lamda Function inside another function

```py
def myfunc(n):
    res = lambda x : x*n
    return res

res =
print(myfunc(5)) #None
```
