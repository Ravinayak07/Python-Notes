# Arrays:

- Python does not have built-in support for Arrays.
- To work with Arrays, need to import NumPy library
- But Python Lists can be used instead
- Ex:

```py
# creating an array(list) containing city names:

cities = ["Delhi","Mumbai","Pune"]
print(cities)
print(type(cities))
```

```
['Delhi', 'Mumbai', 'Pune']
<class 'list'>
```

- Accessing elements of an array using index Number

```py
cities = ["Delhi","Mumbai","Pune"]
print(cities[0]) # Delhi

cities[1] = "Bombay"
print(cities)  # ['Delhi', 'Bombay', 'Pune']
print(len(cities))  # 3
```

- Looping Array elements:

```py
cities = ["Delhi","Mumbai","Pune"]

for x in cities:
    print(x)
```

```
Delhi
Mumbai
Pune
```

- Adding and removing Array Elements

```py
cities = ["Delhi","Mumbai","Pune"]

cities.append("BBSR")
cities.pop(0)
cities.remove("Mumbai")

print(cities) # ['Pune', 'BBSR']
```

## Built-in Methods:

- Arrays/lists has the following built-in methods:
