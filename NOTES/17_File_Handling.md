# File Handling:

- The key function for handling files is: open()

## open() function:

- Takes two parameters: filename and mode

> Types of modes for opening file:

- "r" : (Default). opens file for Reading. Error if file not exist
- "a" : for Appending. Creates new file if not exist
- "w" : for writing. Creates new file if not exist
- "x" : for creating file. Error if file already exists
- "t" : (Default) for handling file in text mode
- "b" : for handling file in Binary mode(e.g images)

> SYNTAX:

- Open a file for reading:

```py
f = open("fileName.txt")

# same as

f = open("fileName.txt","rt")

# r for read , t for text-mode
# both are default values
```

## Opening file on the server:

- For example the below file is located in the same folder as python

```
# Ravi.txt
My name is Ravi. I am a computer Science Student
```

- open() fun returns a file object which has read() method for reading the content of file:

```py
f = open("Ravi.txt","r")
print(f.read())
```

```
My name is Ravi. I am a computer Science Student
```

- If file is in different location, mention path:

```py
f = open("C:\Users\ASUS\Ravi.txt","r")
print(f.read())
```

> FOR READING PARTS OF FILE:

- By default read() methods returns whole text
- We can specify how many characters to return:

```py
# Returns first 10 characters
f = open("Ravi.txt","r")
print(f.read(10))
```

> readline() Method:

- returns one line

```py
# Reads one line of file
f = open("Ravi.txt", "r")
print(f.readline())
```

- For reading two lines:

```py
f = open("Ravi.txt", "r")
print(f.readline())
print(f.readline())
```

- For reading entire file line by line:

```py
f = open("Ravi.txt", "r")
for x in f:
  print(x)
```

> CLOSING FILES:

- Always close file when you are done. Its a good practice

```py
f = open("Ravi.txt", "r")
print(f.readline())
f.close()
```

- Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file

> Writing in a File:

- open() fun is used
- Two modes:

```
1. "a" : Append at the end of file
2. "w" : overwrite entire file
```

> Append("a")

```
# Ravi.txt
My name is Ravi. I am a computer Science Student
```

```py
# Appending
f = open("Ravi.txt","a")
f.write("I am From Bhubaneswar")
f.close()

#open and after appending:
f = open("Ravi.txt","r")
print(f.read())
```

```
# Ravi.txt

My name is Ravi. I am a computer Science Student. I am From Bhubaneswar

```

> Overwrite("w")

```py
f = open("Ravi.txt","a")
f.write("All content deleted")

f = open("demofile3.txt", "r")
print(f.read())
```

```
# Ravi.txt

All content deleted
```

## Creating New File:

- Function used: open()
- Three modes:

```
1. "x" : creates new file. Error if file exists
2. "a" : Append. Creates a new file if file doesnot exists
3. "w" : Write. Craetes a new file if doesnot exist
```

- EX:

```py
# creates a new empty file
f = open("fileName.txt","x")
```

```py
# creates a new file if it does not exist
f = open("fileName.txt","w")
```

## DELETE FILE:

- to delete a file, first import OS module
- Run os.remove() function
- Ex:

```py
# Remove the file "Ravi.txt"

import os
os.remove("Ravi.txt")
```

- If File doesnot exist, it will show Error.
- To avoid it, check if file exist before deleting:

```py
import os

if os.path.exists("Ravi.txt"):
    os.remove("Ravi.txt")
else:
    print("File doesnot exists")
```

## DELETE FOLDER:

- os.rmdir() method is used to delete entire folder

```py
import os
os.rmdir("folderName")
```

- Only Empty Folders can be removed.
