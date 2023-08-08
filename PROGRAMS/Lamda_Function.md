# Check Even or Odd:

Using Lamda Function

```py
check_number = lambda num: "even" if num % 2 == 0 else "odd"

number = int(input("Enter a number: "))
result = check_number(number)

print(number, "is an", result, "number.")
```

```
1. Define a lambda function named check_number that takes a parameter num.
2. The lambda function checks if num is divisible by 2 by using the modulo operator %.
3. If the remainder is 0, it returns the string “even”; otherwise, it returns the string “odd”.
4. Prompt the user to enter a number and store it in the variable number using int(input(“Enter a number: “)).
5. Call the lambda function check_number with number as the argument, and store the result in the variable result.
6. Print the number along with the result using the print function, indicating whether it is an odd or even number.
7. Example output: “12 is an even number.” or “17 is an odd number.”
```
