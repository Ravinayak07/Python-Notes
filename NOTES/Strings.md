# String formatting:

## format() method:

- used to format selected parts of string
- Ex:

```py
age = 23
msg = "My age is {}"
print(msg.format(age)) # My age is 23
```

- Add paramters inside {} to convert values in case of decimals

```py
price = 99
msg = "The price of this product is  {:.3f}"
print(msg.format(price)) #The price of this product is  99.000
```

- Multiple Values:

```py
name = "Ravi"
age = 22
year = 2023
msg = "My name is {}. I am {} years old. I graduated in the year {}"
print(msg.format(name,age,year))
```

```
My name is Ravi. I am 22 years old. I graduated in the year 2023
```

- Index Numbers can be used inside {} for correct placeing of values

```py
name = "Ravi"
age = 22
year = 2023
msg = "My name is {0}. I am {1} years old. I graduated in the year {2}"
print(msg.format(name,age,year))
```

```
My name is Ravi. I am 22 years old. I graduated in the year 2023
```

```py
age = 23
name = "Ravi"
msg = "My name is {1}. {1} is {0} years old."
print(msg.format(age, name)) # My name is Ravi. Ravi is 23 years old.

```

```py
price = 199
product = "Medicine"
msg = "The price of this {0} is  {1:.3f}"
print(msg.format(product, price)) #The price of this Medicine is  199.000
```

- We can't copmbine both ways of formatting. It will generate Error

```py
price = 199
product = "Medicine"
msg = "The price of this {0} is  {:.3f}"
print(msg.format(product, price))
```

> Named Indexes:

- names can be added inside {}
- Also need to pass the names in parameter values

```py
msg = "The Capital of {state} is {city}"
print(msg.format(city="Bhubaneswar",state="Odisha"))
```

```
The Capital of Odisha is Bhubaneswar
```
