# File Handling:

- File Handling means the process of handling files i.e read, write files, etc.
- Several Programming Languages have the concept of file handling and its implementation is little complicated.
- But in python, its easy and short
- Python treats files in two ways: text or binary
- Each line of code includes a sequence of characters and they form a text file.
- Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.
- There are both advantages and disadvantages of file handling

## Advantages:

- It allows to perform many operations like: creating, reading, writing, appending, renaming and deleting files
- Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
- File-handling functions work across different platforms (e.g. Windows, Mac, Linux).

## Disadvantages:

- Can cause a lot of errors when the code is not carefully written.
- Can cause security risks in case of modifying sensitive files on the system.
- File handling operations in Python can be slower than other programming languages when dealing with large files.

## open() function:

- The key function for handling files is: open()
- Because Before performing any operation on the file like reading or writing, first, we have to do is open that file
- open() is an inbuilt function in Python
- Takes two parameters: filename and mode of opening
- Syntax:

```
f = open(filename, mode)
```

## Types of modes for opening file:

- "r" : (Default). opens an existing file for Reading. Error if file not exist
- "a" : opens an existing file for Appending. Creates new file if not exist. It won’t override existing data.
- "w" : opens an existing file for writing. Creates new file if not exist. If the file already contains some data then it will be overridden
- "x" : for creating file. Error if file already exists
- "t" : (Default) for handling file in text mode
- "b" : for handling file in Binary mode(e.g images)
- "r+" : To read and write data into the file. The previous data in the file will be overridden.
- "w+"": To write and read data. It will override existing data.
- "a+": To write and read data. It will override existing data.

# SYNTAX:

## 1. Open a file for reading:

```py
f = open("fileName.txt")

# same as

f = open("fileName.txt","rt")

# r for read , t for text-mode
# both are default values
```

## 2. Open a file on the server:

> In this file is located in the same folder as python

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
#output
My name is Ravi. I am a computer Science Student
```

> If file is in different location, mention path:

```py
# Error
f = open("C:\Users\ASUS\Ravi.txt","r")
print(f.read())
```

- The above code will show Error because the backslashes in the file path are being interpreted as escape characters.

- So either double the backslashes in the file path or use a raw string by adding an 'r' prefix before the string.

```py
# Using double backslah:
f = open("C:\\Users\\ASUS\\Desktop\\Ravi2.txt")
print(f.read())
```

```py
# using raw string
f = open(r"C:\Users\ASUS\Desktop\Ravi2.txt")
print(f.read())
```

- Always close() when done
- Alternatively, you can use the with statement to ensure proper handling of file closure:

```py
with open(r"C:\Users\ASUS\Desktop\Ravi2.txt") as f:
    print(f.read())
```

- This will automatically close the file when the block is exited, even if an exception is raised

## 3 . Reading File:

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

## 4. Writing in a File:

- Two modes:

```
1. "a" : Append at the end of file
2. "w" : overwrite entire file
```

> 1 . Append("a")

```
# Ravi.txt
My name is Ravi. I am a computer Science Student
```

```py
# Appending
f = open("Ravi.txt","a")
f.write("I am From Bhubaneswar")
f.close()

#open and raed after appending:
f = open("Ravi.txt","r")
print(f.read())
```

```
# Ravi.txt

My name is Ravi. I am a computer Science Student. I am From Bhubaneswar

```

> 2 . Overwrite("w")

```py
f = open("Ravi.txt","w")
f.write("All content deleted")

f = open("Ravi.txt", "r")
print(f.read())
```

```
# Ravi.txt

All content deleted
```

> writelines:

- method expects a list of strings to overide the existing data.

```py
f = open("Ravi.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
f.writelines(L)
f.close()
```

```py
mylist = ["My name is Ravi \n","I live in Bhubaneswar \n", "My age is 23\n"]

file = open("Ravi.txt", "w")
file.writelines(mylist)
file.close()

file = open("Ravi.txt","r")
print(file.read())
```

## 5. Closing File:

- Always close file in the end

```py
f = open("Ravi.txt", "r")
print(f.readline())
f.close()
```

- Due to buffering, changes made to a file may not show until you close the file

## 6. Creating New File:

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

## 7. Deleting File:

- first import OS module
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
    print("file deleted")
else:
    print("File doesnot exists")
```

## 8. Deleting Folder:

- os.rmdir() deletes entire folder

```py
import os
os.rmdir("folderName")
```

- Only Empty Folders can be removed.
- To avoid getting error, check whether folder exists before deleting it.

```py
import os
if os.path.exists("demo"):
    os.rmdir("demo")
    print("folder deleted")
else:
    print("File doesnot Exists")

```

## Creating Folder:

- os.mkdir() creates folder

```py
import os
os.mkdir("demo")
```

```py
import os
if not os.path.exists("demo"):
    os.mkdir("demo")
    print("folder created")
else:
    print("Folder Already Exists")
```

## 9. with Statement:

- Another way of dealing with filr handling:

> without with statement:

```py
f = open('file_path', 'w')
f.write('hello world !')
file.close()
```

> Using with statement:

```py
# using with statement
with open('file_path', 'w') as f:
    f.write('hello world !')
```

- Automatically closes the file

# QUESTIONS:

> Read Each line present in a file

```py
file = open('Ravi.txt', 'r') # opening with the reading mode.

# Printing every line one by one in the file
for each in file:
    print(each)
```

> Extract a string that contains all characters in the file.

```py
file = open("Ravi.txt", "r")
print (file.read())
```

> Read a file using the with statement.

```py
with open("Ravi.txt") as file:
    data = file.read()

print(data)
```

> Read the first five characters of stored data and return it as a string:

```py
file = open("Ravi.txt", "r")
print (file.read(5))
```

> Split lines while reading files in Python.

- The split() function splits the variable when space(default) is encountered.

```py
with open("Ravi.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
```

> Creating a File. Write two lines and then close the file

```py
file = open('Ravi.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
```

> Open a file and append one line

```py
file = open('Ravis.txt', 'a')
file.write("This will add this line")
file.close()
```

> Using the written statement along with the with() function.

```py
with open("Ravi.txt", "w") as f:
    f.write("Hello World!!!")
```

# Other Methods used in File Handling:

- rstrip(): strips each line of a file off spaces from the right-hand side.
- lstrip(): strips each line of a file off spaces from the left-hand side.

# PROGRAMS:

## Progrm to read entire file:

```py
"""
# first Method
file = open("Ravi.txt","r")
print(file.read())
print(" ----------------")
"""
# Second Method
file = open("Ravi.txt","r")
lines = file.readlines()
print(lines)

for line in lines:
    print(line)
```

# Program to read file line by line:

```py
file = open("Ravi.txt", "r")

for i in file:
    print(i)

```

## Program to Copy One File to Another File:

```py
"""
f = open("Ravi.txt")
print(f.read())
"""

with open("Ravi.txt") as f:
    with open("Copy.txt", "w") as f1:
        for line in f:
            f1.write(line)

f = open("copy.txt")
print(f.read())
```

```py
file = open("Ravi.txt","r")
file2 = open("copy.txt","w")
lines = file.readlines()

for line in lines:
    print(line)
    file2.write(line)

file3 = open("copy.txt")
print(file3.read())
```

## Program to Count the Number of Lines in Text File

```py
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:",num_lines)
```

## Program to Count the Number of Blank Spaces in a Text File

```py
fname = input("Enter file name: ")
count = 0

with open(fname, 'r') as f:
    print(f.read())
    for line in f:
        words = line.split()
        count=count+len(words)-1
print("Occurrences of blank spaces:", count)
```

```py
filename = input("Enter file name: ")
count=0
space=0
with open(filename, "r") as file:
    for line in file:
        words = line.split()
        print(words)
        count = count+len(words)-1
        print(count)
    space = space+count

print(space)
```

## Program to Count the Occurrences of a Word in a Text File:

```py
fname = input("Enter file name: ")
word=input("Enter word :")
count = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                count=count+1
print("Occurrences of the {} in {} file is:  {}".format(word,fname,count))
```

## Program to Count total Number of Words in a Text File:

```py
fname = input("Enter file name: ")

num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
```

## Program to Capitalize First Letter of Each Word in a File:

- For this title() function will be used: returns a string where the first character in every word is upper case and rest are lowercase

```py
msg = "we are learning python"

x = msg.title()

print(x) # We Are Learning Python

```

```py
fname = input("Enter file name: ")

with open(fname, 'r') as f:
    lines = f.readlines()

print(lines)

newLines = []
for line in lines:
    newLines.append(line.title())

with open(fname, 'w') as f:
    f.writelines(newLines)

f = open(fname, 'r')
print(f.read())
```

## Program to Counts the Number of Times a Letter Appears in the Text File:

```py
fname = input("Enter file name: ")
letter = input("Enter file name: ")
count=0
with open(fname, 'r') as f:
    lines = f.readlines()

for line in lines:
    for i in line.lower():
        if i==letter:
            count+=1
print(count)
```

## Program to Extract and print all unique Numbers from Text File:

```py
fname = input("Enter file name: ")
unique = set()
with open(fname, 'r') as f:
    lines = f.readlines()

for line in lines:
    for i in line:
        if i.isdigit():
            unique.add(i)

sortedList = sorted(unique)
for i in sortedList:
    print(i," ",end="")
```

## -----------------------------------------------------------------------------------------------------------

## Program to print each word of a file one by one:

```py

with open('Ravi.txt','r') as file:
    for line in file:
        for word in line.split():
            print(word)


```

## program to read character by character from a file:

```py
file = open('Ravi.txt', 'r')

while True:
    char = file.read(1)
    if not char:
        break
    print(char)

file.close()
```

# Program to Get number of characters, words, spaces and lines in a file

## Program to Append the Content of One File to the End of Another File:

```py
fname1 = input("Enter file to be read from: ")
fname2 = input("Enter file to be appended to: ")

f = open(fname1, "r")
text1 = f.read()
f.close()

f2 = open(fname2, "a")
f2.write(text1)
f2.close()
```

## Program to Read a String from the User and Append it into a File:

```py
fname = input("Enter file name: ")

myStr=input("Enter string to append: ");

f=open(fname,"a")

f.write("\n")
f.write(myStr)
f.close()

print("Contents of appended file:")

f=open(fname,'r')
print(f.read())
f.close()

```

# Implementing all the functions in File Handling

- using all concepts of file hnadling in this example:

```py
import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
```

```
File example.txt created successfully.
Hello, world!

Text appended to file example.txt successfully.
Hello, world!
This is some additional text.

File example.txt renamed to new_example.txt successfully.
Hello, world!
This is some additional text.

File new_example.txt deleted successfully.
```
