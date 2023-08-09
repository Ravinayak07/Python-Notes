# LOOPS

- Python has two loops: for loop and while loop.

## Diff bet While and For loop:

- While loop iterates over a condition
- For loop iterates over a sequence(list,tuple,dictionary,set, string)

## WHILE LOOP:

- Executes the code as long as the condition is true.

```py
i = 0
while i<5:
  print(i)
  i=i+1
```

- If we don't add the updation statement, it will be an infinite loop.

# Control Statements:

- Manages the flow of program by determining which code should be executed next.

> Break :

- can stop the loop even if the condition is true

```py
i=0
while i<5:
  print(i)
  if i==4:
    break
  i = i+1
```

> Continue

- can stop the current iteration and continue with the next.
- Question: Write a while loop that prints from 1 to 5 except 3:

```py
# Wrong Code
i = 0
while i < 5:
  if i == 3:
    continue
  print(i)
  i = i + 1

# it will print 0, 1, 2 and after that it will go to infinite loop
```

- Right code

```py
i=0
while i<5:
  i = i+1
  if i==3:
    continue
  print(i)
```

## FOR LOOP

- iterates over a sequence(list, tuple, dictionary, set, string)
- Ex: Create a list and print its items using for loop:

```py
colors= ["red", "blue", "green"]
for x in colors:
  print(x)
```

- Ex: Create a string and print its characters using for loop in one line.

```py
collegeName = "Silicon Institute"
for x in collegeName:
  print(x, end="")
```

- Ex: Create a list and print its items using for loop except the any one item

```py
colors = ["red","blue","green"]
for x in colors:
  if x=="red":
    continue
  print(x)
```

- Ex: Create a list and demonstrate the working of for loop using break

```py
colors = ["red","blue","green"]
for x in colors:
  if x == "blue":
    break
  print(x)
```

> range() function:

- helps to loop for a speceified number of times
- it returns a sequence of numbers starting from 0(by default), increments by 1(by default) till reaches at a specified number
- Ex: range(6) means values from 0 to 5.
- Question: print first 10 whole numbers using for loop and range() function

```py
for x in range(10):
  print(x)
```

- Starting avlue can be specified by adding parameter:

```py
for x in range(3, 10):
  print(x)
```

- Range() fun increments bydefault by 1
- Increment value can be specified by adding third parameter

```py
for x in range(2,10,3):
  print(x)
```

```
2
5
8
```

> Else in For Loop:

- executes when the loop is finished

```py
for x in range(10):
  print(x)
else:
  print("Loop Over")
```

- If break is used else will not work:

```py
for x in range(10):
  if x==5:
    break
  print(x)
else:
  print("Loop over")
```

> pass in For loop:

- for loops can't be empty:

```py
# error:
for x in range(6):
```

- So we can use pass here

```py
for x in range(6):
  pass
```

## Do while loop

- In c

```c
do {
  //Code
} while(condition);
```

- In Python?
- Python doesnot has do while to reduce complexity
- The same functionality of do while can be achieved through
  'while' and 'break'
- In C:

```c
int num = 0;
do {
  printf("%d",num);
  num = num+1;
} while(num<=0);
```

- In Python:

```py
num = 0
while True:
  print(num)
  num=num-1
  if num<=0:
    break;
```
