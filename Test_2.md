# Programs:

- Program to print Sum of squares of first n natural numbers

```py
num = int(input("Enter The number: "))

def squareSum(num):
	sum = 0
	for i in range(1, num+1):
		sum = sum + (i * i)

	return sum
print(squareSum(num))
```

- Program to check whether a number is Strong Number or Not.

```
A Strong number is a special number whose sum of the all digit's factorial should be equal to the number itself.
Ex:
num = 145
1! = 1
4! = 4*3*2*1 = 24
5! = 120
sum = 1+24+120 = 145.

Hence, It is a Strong Number
```

- Print this Pattern:

```
* * * * *
  * * * *
    * * *
      * *
        *

(Here n=5)
```

- Print this Pattern

```
* * * * *
 * * * *
  * * *
   * *
    *

(Here n=5)
```

# OUTPUT:

- 1

```
for i in range(5):
    print(i)
```

- 2

```
for i in range(1,2,3):
    print(i)
```
