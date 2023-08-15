# Dictionaries

- Items are Ordered(From ver 3.7), Changeable, No Duplicates allowed.
- Stores data in key-value pairs
- Ex:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age":23
}
print(student) # {'name': 'Ravi', 'college': 'Silicon', 'age': 23}
```

- values can be accessed using key names:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age":23
}
print(student["name"]) # Ravi
print(student["college"]) # Silicon
print(student["age"]) # 23
```

- Duplicates Not Allowed. Means There can't be keys with same name
- If there, then the last value will override the previous one

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age":23,
    "age":24
}
print(student["age"]) #24
```

- But there can be duplicate values:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Institute": "Silicon",
    "age":23,
}
print(student) # {'name': 'Ravi', 'college': 'Silicon', 'Institute': 'Silicon', 'age': 23}
```

> Dictionary Length:

- using len() function:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Institute": "Silicon",
    "age":23,
}
print(len(student)) #4
```

> Dictionary values can be of any data type:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}

print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'Graduate': True, 'age': 23, 'year': 2023, 'skills': ['Python', 'React', 'Javascript']}
```

> type():

- Dictionaries are objects with data type 'dict'

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}

print(type(student)) #<class 'dict'>
```

> dict() constructor:

```py
student = dict(name="ravi", age=23, college="Silicon")
print(student) # {'name': 'ravi', 'age': 23, 'college': 'Silicon'}
```

## ACCESS ITEMS:

- Items of a dictionary can be accessed by referring the key name:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}
x = student["name"]
y = student["skills"]
print(x) # Ravi
print(y) # ["Python","React","Javascript"]
```

- get() method can also be used:

```py
z = student.get("year")
print(z) #2023
```

> Keys() Method:

- Returns a list of all keys

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}
x = student.keys()
print(x)  # dict_keys(['name', 'college', 'Graduate', 'age', 'year', 'skills'])
```

- The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
- Add a new item to the original dictionary, and see that the keys list gets updated as well:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.keys()
print(x)

student["year"] = 2023

print(x)
```

```py
dict_keys(['name', 'college', 'Graduate', 'age'])
dict_keys(['name', 'college', 'Graduate', 'age', 'year'])
```

> values() Method:

- returns a list of values in the dictionary

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.values()

print(x)  # dict_values(['Ravi', 'Silicon', True, 23])
```

- The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
- Make a change in the original dictionary, and see that the values list gets updated as well:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.values()

print(x)  # dict_values(['Ravi', 'Silicon', True, 23])

student["age"] = 22

print(x)
```

```
dict_values(['Ravi', 'Silicon', True, 23])
dict_values(['Ravi', 'Silicon', True, 22])
```

- Add a new item to the original dictionary, and see that the values list gets updated as well:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.values()

print(x)  # dict_values(['Ravi', 'Silicon', True, 23])

student["year"] = 2023

print(x)
```

```
dict_values(['Ravi', 'Silicon', True, 23])
dict_values(['Ravi', 'Silicon', True, 23, 2023])
```

> Items():

- returns each item in a dictionary as tuples inside a list

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.items()
print(x)
```

```
dict_items([('name', 'Ravi'), ('college', 'Silicon'), ('Graduate', True), ('age', 23)])
```

- The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
- Make a change in the original dictionary, and see that the items list gets updated as well:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.items()

print(x)

student["age"] = 22

print(x)

```

```
dict_items([('name', 'Ravi'), ('college', 'Silicon'), ('Graduate', True), ('age', 23)])
dict_items([('name', 'Ravi'), ('college', 'Silicon'), ('Graduate', True), ('age', 22)])
```

- Add a new item to the original dictionary, and see that the items list gets updated as well:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
x = student.items()

print(x)

student["year"] = 2023

print(x)
```

# CHECK IF KEY EXISTS:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

if "name" in student:
    print("YES")          # YES
```

## CHANGHE ITEMS IN DICTIONARY:
