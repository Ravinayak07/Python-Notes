# Check Whether a number is poistive, Negative or Zero

```py
num = int(input("Enter number: "))
if num>0:
    print("Positive")
elif num<0:
    print(Negative")
else:
    print("Zero")
```

# Check Even or Odd:

Using Modulus Operator(%)

```py
num = int(input("Enter the number: "))

if num%2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
```

Using Bitwise AND (&)

```py
num = int(input("Enter the number: "))

if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")
```

```py
"""
2. The program then uses the bitwise AND operator (&) with 1 to check the least significant bit of the binary representation of the number.
3. If the result is non-zero, it means the number is odd.
"""
```

# Program to Find the Grade of a student:

```
Total 4 subjects (Eng, Math, history, Science)
If Avg >= 90 : Grade A
If Avg >= 80 and < 90 : Grade B
If Avg >= 70 and <80 : Grade C
If Avg <= 70 : Grade d
```

```py
eng = int(input("Enter marks of English: "))
math = int(input("Enter marks of math: "))
his = int(input("Enter marks of History: "))
sci =int(input("Enter marks of Science: "))

Avg = (eng + math + his + sci) / 4
if Avg >= 90:
    result = "A"
elif Avg >= 80 and Avg < 90:
    result = "B"
elif Avg >= 70 and Avg < 80:
    result = "C"
else:
    result = "D"

print("Average: ", Avg)
print("Grade: ", result)
```
