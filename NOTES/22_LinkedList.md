# TYPES OF DATA STRUCTURES:

# Linear Data Structure:

- Data are organized sequentially or linearly
- Lists
- Arrays
- Linkedlist
- Stacks
- Queues

# Non-Linear Data Structure:

- The data elements are not organized sequentially but have a hierarchical or interconnected relationship
- Trees : Trees are hierarchical data structures with a root node and a structure of nodes connected by edges.
- Graphs : non-linear data structure consisting of vertices and edges.The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph

# LINKED LIST:

- collection of nodes that are linked with each other
- Each node has two elements: data and refernce to another node (link that connects it with another node)
- First Node is where Head points
-

> How to implement:

## Creating a Linkedlist in Python:

- To implement linked list, classes are used.
- We will use Node class
- We will use init method to initliaze a linked list with an empty head.

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Inserting at the Beginning in Linked list:

- Create an insert() method to insert a node at the beginning of the linked list,

```py
def insert(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node
```

- traversing the list:

```py
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

- Full code:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.traverse()
```

```
30 -> 20 -> 10 -> None
```

- Print in original order:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()
```

```
10 -> 20 -> 30 -> None
```

# Insertion at the end:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()

# Inserting a new node at the end
new_data = 40
linked_list.append(new_data)

print("Linked list after insertion:")
linked_list.display()
```

```
10 -> 20 -> 30 -> None
Linked list after insertion:
10 -> 20 -> 30 -> 40 -> None
```

# Update any elment:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print(f"{old_data} not found in the linked list.")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Original linked list:")
linked_list.display()

# Update an element
old_value = 20
new_value = 25
linked_list.update(old_value, new_value)

print("Linked list after update:")
linked_list.display()
```

```
Original linked list:
10 -> 20 -> 30 -> None
Linked list after update:
10 -> 25 -> 30 -> None
```

# DELETION

## Remove first node from the linkedlist

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_first(self):
        if not self.head:
            print("Linked list is empty.")
            return
        self.head = self.head.next

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Original linked list:")
linked_list.display()

# Remove the first node
linked_list.remove_first()

print("Linked list after removing the first node:")
linked_list.display()


```

```
10 -> 20 -> 30 -> None
Linked list after removing the first node:
20 -> 30 -> None
```

## Remove the last node:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_last(self):
        if not self.head:
            print("Linked list is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Original linked list:")
linked_list.display()

# Remove the last node
linked_list.remove_last()

print("Linked list after removing the last node:")
linked_list.display()
```

```
Original linked list:
10 -> 20 -> 30 -> None
Linked list after removing the last node:
10 -> 20 -> None
```

# Remove from a given position:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_at_position(self, position):
        if not self.head:
            print("Linked list is empty.")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
            if current is None:
                print("Position out of range.")
                return
        if current.next:
            current.next = current.next.next
        else:
            print("Position out of range.")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("Original linked list:")
linked_list.display()

# Remove node at position 2 (index 2)
position_to_remove = 2
linked_list.remove_at_position(position_to_remove)

print(f"Linked list after removing node at position {position_to_remove}:")
linked_list.display()
```

```
Original linked list:
10 -> 20 -> 30 -> 40 -> None
Linked list after removing node at position 2:
10 -> 20 -> 40 -> None
```

## Remove a specific node from a given linked list:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_node(self, value_to_remove):
        if not self.head:
            print("Linked list is empty.")
            return
        if self.head.data == value_to_remove:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value_to_remove:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node with value {value_to_remove} not found in the linked list.")

# Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("Original linked list:")
linked_list.display()

# Remove node with value 20
value_to_remove = 20
linked_list.remove_node(value_to_remove)

print(f"Linked list after removing node with value {value_to_remove}:")
linked_list.display()
```

```
Original linked list:
10 -> 20 -> 30 -> 40 -> None
Linked list after removing node with value 20:
10 -> 30 -> 40 -> None
```
