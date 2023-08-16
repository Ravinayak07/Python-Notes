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

- how to access values ? : values can be accessed using key names:

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

> Dictionary Keys can also of any data types:

- Dictionary Keys can also of any immutable data types like intergers, floats, strings, tuples, strings,etc

```py
mixed_dict = { 1: "one",
               2 : "two",
               "three" : 3,
               ("apple","orange") : "fruits",
               True : "yes",
               3.14 : "pi",
             }
print(mixed_dict)
```

- Alhough set is unchangeable, still it can't be used as keys. This is because in set, we can add/remove items

```py
setDict = {
    {1,2} : "One Two",
    {3,4} : "Three Four"
    }
print(setDict)  # Error
```

- But frozenset(immutable version of set) can be used

```py
setDict = {
    frozenset({1,2}) : "One Two",
    frozenset({3,4}) : "Three Four"
    }
print(setDict)
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

- for mixed dictionary

```py
mixed_dict = dict({
    1: "one",
    2: "two",
    "three": 3,
    ("apple", "orange"): "fruits",
    True: "yes",
    3.14: "pi"
})

print(type(mixed_dict))
```

- without using {}. I provided a list of tuples, where each tuple represents a key-value pair for the dictionary

```py
mixed_dict = dict(
    [(1, "one"),
     (2, "two"),
     ("three", 3),
     (("apple", "orange"), "fruits"),
     (False, "yes"),
     (3.14, "pi")]
)

print(mixed_dict)
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

> Access using indexes

- Since dictionary is ordered. Can we access it using indexex??? Lets try

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}
print(student[0]) # Error
```

- This is because dictionaries are unindexed unlike lists and tuples
- We can't directly access dictionary elements usng integer indices.
- For that, first convert the dictionary keys into a list and the use list index to access the respective keys.

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}

key_list = list(student.keys())
print(key_list[5])
print(student[key_list[5]])
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

- using loop

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

for i in student:
    if student[i] == "Silicon":
        print("present")
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
# using another dictionary as argument
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student.update({"age":22})

print(student)
```

```py
# using any iterable object as argument
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
}

student.update([("age",22),("year",2023)])

print(student)
```

- changing items using indexes:

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "Graduate": True,
    "age": 23,
    "year":2023,
    "skills": ["Python","React","Javascript"]
}

key_list = list(student.keys())
print(key_list[5])
print(student[key_list[5]])
student[key_list[5]] = "CPP"
print(student[key_list[5]])
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

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
}
print(student)
student2 = student
student2["year"] = 2023
print(student)
```

- Buil-in Methods:

> 1 . copy():

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
}
print(student)
student2 = student.copy()
student2["year"] = 2023
print(student)
```

> 2 . dict():

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

print(student)
student2 = dict(student)
student2["year"] = 2023
print(student)
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

# PROGRAMS:

## Program to create Dictionary from an Object of a class.

```py
class A(object):
     def __init__(self):
         self.A=1
         self.B=2
obj=A()
print(obj.__dict__)
```

```
Program Explanation
1. A class named A is declared.
2. The keys are initialized with their values in the __init__ method of the class.
3. The dictionary is formed using the object of the class and by using the __dict__ method.
4. The dictionary formed from the object of the class is printed.
```

## Program to check whether a Key Exists in a Dictionary or Not.

```py
student = {
    "name": "Ravi",
    "college": "Silicon",
    "age": 23,
    "Graduate": True
}

key = input("Enter key to check: ")
if key in student.keys():
    print("Present")
else:
    print("Not present")
```

## Program to add a key value pair to a dictionary and print new Dictionary. Take key and value as user input

```py

key=input("Enter the key :")
value=int(input("Enter the value :"))
x ={}
x.update({key:value})
print("New dictionary is:")
print(d)
```

## Program to find sum of all values in a dictionary. Take userinput for key and values

```py
new_dict={}

num_pairs = int(input("Enter the number of key-value pairs: "))

for i in range(num_pairs):
    key = input("Enter key "+str(i+1)+" : ")
    value = int(input("Enter value of key "+str(i+1)+" : "))
    new_dict[key]=value

print(new_dict)
print(sum(new_dict.values()))
```

## Program to multiply all items values in a dictionary:

```py
new_dict={}

num_pairs = int(input("Enter the number of key-value pairs: "))

for i in range(num_pairs):
    key = input("Enter key "+str(i+1)+" : ")
    value = int(input("Enter value of key "+str(i+1)+" : "))
    new_dict[key]=value

print(new_dict)
prod=1
for i in new_dict:
    prod = prod*new_dict[i]

print(prod)
```

- using math.prod

```py
import math
new_dict={}

num_pairs = int(input("Enter the number of key-value pairs: "))

for i in range(num_pairs):
    key = input("Enter key "+str(i+1)+" : ")
    value = int(input("Enter value of key "+str(i+1)+" : "))
    new_dict[key]=value

print(new_dict)
print(math.prod(new_dict.values()))
```

## Program to concatenate two different dictionaries:

```py
student1 = {
    "name": "Ravi",
    "college": "Silicon",
}
student2 = {
    "age": 23,
    "Graduate": True
}
student1.update(student2)
print("Concatenated dictionary is:")
print(student1)
```

## Program to generate a dictionary that contains numbers (between 1 and n) in the form (x,x\*x)

```
if num = 5

output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```py
num = int(input("Enter a number:"))
new_dict={}
for i in range(1, num+1):
    new_dict[i] = i*i


print(new_dict)
```
