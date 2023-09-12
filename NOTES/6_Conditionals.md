## If elif else:

- ```py
  a = 20
  if a > 0:
  print("Positive")
  elif a < 0:
  print("Negative")
  else:
  print("Zero")
  ```

## Ternary Operator(i.e Short Hand If...Else):

- ```py
      a = 20
      if a > 0: print("Positive")
  ```

  ```py
  a = 10
  b = 20
  print("A") if a > b else print("B")
  ```

  ```py
  a = 10
  print("Positive") if a > 0 else print("Zero") if a == 0 else print("Negative")
  ```

## Nested If:

- ```py
  num = 15
  if num >= 0:
  	if num == 0:
  		print("Zero")
  	else:
  		print("Positive number")
  else:
  	print("Negative number")
  ```

## Pass Statement:

- If statements can't be empty
- So to avoid error, we can use pass statement.

```py
for i in range(5):
    if i != 3:
        pass
    else:
        print("Found it")
print("Loop finished")
```
