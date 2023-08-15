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

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student["age"] = 22

print(student)
```

> Using update() method:

- updates the dictionary with the items from the given argument.
- The argument must be a dictionary, or an iterable object with key:value pairs.

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student.update({"age":22})

print(student)
```

## ADDING ITEMS:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student["year"] = 2023

print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'Graduate': True, 'age': 23, 'year': 2023}
```

- Using update() method:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student.update({"year":2023})
print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'Graduate': True, 'age': 23, 'year': 2023}
```

## Remove items from Dictionary:

> 1 . pop() method:

- removes item with specified key name:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student.pop("Graduate")
print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'age': 23}
```

> 2 . popitem() method:

- removes the last inserted item

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

student.popitem()
print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'age': 23}
```

> 3 . del keyword:

- removes item with specified key name.

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

del student["Graduate"]
print(student)
```

```
{'name': 'Ravi', 'college': 'Silicon', 'age': 23}
```

- del can also delete entire dictionary:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

del student
print(student) # Error
```

> 4 . clear():

- Empties the dictionary:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

student.clear()
print(student) # {}
```

## Loop Through Dictionary:

- while looping a dictionary, return values are keys of dictionary.

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

for x in student:
    print(x)
```

```
name
college
age
Graduate
```

- keys() method can also be used:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

for x in student.keys():
    print(x)
```

```
name
college
age
Graduate
```

- To return values, need to mention keys:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

for x in student:
    print(student[x])
```

```
Ravi
Silicon
23
True
```

- values() method can be used:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

for x in student.values():
    print(x)
```

```
Ravi
Silicon
23
True
```

- To loop through both keys and values, use items() method:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

for x in student.items():
    print(x)
```

```
('name', 'Ravi')
('college', 'Silicon')
('age', 23)
('Graduate', True)
```

# COPY DICTIONARY:

- cannot copy simply by assigning(dict2 = dict1) because both refer to same memory location
- Any changes made to dict1 will automatically be made in dict2.
- Buil-in Methods:

> 1 . copy():

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

student2 = student.copy()
print(student2)
```

> 2 . dict():

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

student2 = dict(student)
print(student2)
```

## NESTED DICTIONARIES:

- Dictionaries containing dictionaries

```py
myClass = {
    "student1" : {
        "name" : "Ravi",
        "age"  : 23
    },
    "student2" : {
        "name" : "Deepak",
        "age"  : 22
    },
    "student3" : {
        "name" : "Hamid",
        "age"  : 21
    }
}
print(myClass)
```

```
{'student1': {'name': 'Ravi', 'age': 23}, 'student2': {'name': 'Hamid', 'age': 21}}
```

- Add three different dictionaries into a new dictionary

```py
student1 = {
  "name" : "Ravi",
  "age"  : 23
}
student2 = {
  "name" : "Deepak",
  "age"  : 22
}
student3 = {
  "name" : "Hamid",
  "age"  : 21
}

myClass = {
  "student1" : student1,
  "student2" : student2,
  "student3" : student3
}

print(myClass)
```

```
{'student1': {'name': 'Ravi', 'age': 23}, 'student2': {'name': 'Deepak', 'age': 22}, 'student3': {'name': 'Hamid', 'age': 21}}
```

- Access items in Nested Dictionaries

```py
myClass = {
    "student1" : {
        "name" : "Ravi",
        "age"  : 23
    },
    "student2" : {
        "name" : "Deepak",
        "age"  : 22
    },
    "student3" : {
        "name" : "Hamid",
        "age"  : 21
    }
}

print(myClass["student3"]["age"]) # 21
```

# Built-in Dictionary Methods:

- clear(): Removes all the elements from the dictionary
- copy(): Returns a copy of the dictionary
