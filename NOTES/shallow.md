# Shallow copy vs deep copy in Lists

- When we use list2 = list1.copy(), we're creating a shallow copy of list1.
- This means that while the top-level structure of the list is duplicated, the inner lists themselves are not copied. As a result, if we modify the contents of the inner lists in list2, those changes will be reflected in the corresponding inner lists of list1.
- For example:

```py
list1 = [1,2,3,4,[1,2,3]]

list2 = list1.copy()

list2[4].append(56)

print("List 1: ",list1)
print("List 2: ",list2)
```

```
List 1:  [1, 2, 3, 4, [1, 2, 3, 56]]
List 2:  [1, 2, 3, 4, [1, 2, 3, 56]]
```

- if we want to create a truly independent copy of list1 where changes in one list don't affect the other, we need to perform a deep copy.
- This can be achieved using the copy module's deepcopy() function:

```py
import copy

list1 = [1,2,3,4,[1,2,3]]

list2 = copy.deepcopy(list1)

list2[4].append(56)

print("List 1: ",list1)
print("List 2: ",list2)
```

```
List 1:  [1, 2, 3, 4, [1, 2, 3]]
List 2:  [1, 2, 3, 4, [1, 2, 3, 56]]
```
