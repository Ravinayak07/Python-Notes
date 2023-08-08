# If elif else:

```py
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

```

> Short Hand If...Else or Ternary Operator:

- Take two numbers and print which is greatere using ternary

```py
a = 200
b = 33

if a > b: print("a is greater than b")
```

```py
a = 2
b = 330

print("A") if a > b else print("B")
```

```py
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

> AND:

```py
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```

> OR:

-

> Not:

```py
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```

## Nested If:

```py

```

## Pass Statement:

- If statements can't be empty but if you want you can put pass statement t avoid getting error

```py
for i in range(5):
    if i != 3:
        pass
    else:
        print("Found it")
print("Loop finished")

```
