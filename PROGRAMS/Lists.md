## Program to find the Average of a list(Take user input):

```py
list=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    item=int(input("Enter Element: "))
    list.append(item)

avg = sum(list)/num
print("Average",avg)
```

## Program to find largest Number in a list. Take list from user input:

```py
list=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    item=int(input("Enter element:"))
    list.append(item)

print("List: ",list)
list.sort()
print("After sorting: ",list)
print("Largest is:",list[num-1])
```

## Program to find the second largest Number in a list:

```py
list=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    item=int(input("Enter element:"))
    list.append(item)

print("List: ",list)
list.sort()
print("After sorting: ",list)
print("Second Largest is:",list[num-2])
```

## Program to separate Even and odd in two different lists:

```py
list=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    item=int(input("Enter Element: "))
    list.append(item)
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even List :",even)
print("Odd List : ",odd)
```

## Program to Print Largest Even and Largest Odd Number in a List:

```py
list=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    item=int(input("Enter Element: "))
    list.append(item)
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print("Largest Even number:",even[len(even)-1])
print("Largest odd number: ",odd[len(odd)-1])

```

## Program to Count Occurrences of Element in List. Take user input:

```py
list=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    item=int(input("Enter Element: "))
    list.append(item)

num2=int(input("Enter the number :"))
count=0
for x in list:
    if(x==num2):
        count+=1
print(num2,"appears",count,"times in",list)

```

## Python Program to Merge Two Lists and Sort it

```py
list1=[]
num1=int(input("Enter number of elements for list1: "))
for i in range(num1):
    item1=int(input("Enter Element: "))
    list1.append(item1)

list2=[]
num2=int(input("Enter number of elements for list2: "))
for i in range(num2):
    item2=int(input("Enter Element: "))
    list2.append(item2)

newList = list1 + list2
newList.sort()
print("Merged Sorted list is:",newList)
```

## Program to Swap the First and Last Element in a List:

```py
list=[]
num=int(input("Enter number of elements for list1: "))
for i in range(num):
    item=int(input("Enter Element: "+str(i+1)+ " : "))
    list.append(item)

temp=list[0]
list[0]=list[num-1]
list[num-1]=temp
print("After Swapping : ")
print(list)
```

## Program to Swap the First and Last Element in a List without using third variable:

```py
list=[]
num=int(input("Enter number of elements for list1: "))
for i in range(num):
    item=int(input("Enter Element: "+str(i+1)+ " : "))
    list.append(item)

print("Before Swapping: ")
print(list)

list[0],list[num-1] = list[num-1],list[0]

print("After Swapping : ")
print(list)
```

## Program to print the longest word and its length in a list:

```py
list=[]
num=int(input("Enter number of elements for list: "))
for i in range(num):
    item=input("Enter Word: "+str(i+1)+ " : ")
    list.append(item)

max=len(list[0])
item=""
for i in list:
    if(len(i)>max):
       max=len(i)
       item=i
print("Longest Word : ", item)
print("Length: ",len(item))
```

## Do the above program using customized sort function

```py
list=[]
num=int(input("Enter number of elements for list: "))
for i in range(num):
    item=input("Enter Word: "+str(i+1)+ " : ")
    list.append(item)


def sortLength(list):
    return len(list)

list.sort(key=sortLength)
print("Longest Word : ", list[num-1])
print("Length: ",len(list[num-1]))
```

## Program to Remove the ith Occurrence of the Given Word in a List

```py
list=[]
num=int(input("Enter number of elements for list: "))
for i in range(num):
    item=input("Enter Word: "+str(i+1)+ " : ")
    list.append(item)

print(list)
newList=[]
count=0
word=input("Enter word to remove: ")
occurance=int(input("Enter the occurrence to remove: "))
for i in list:
    if i==word:
        count=count+1
        if(count != occurance):
            newList.append(i)
    else:
        newList.append(i)

if count==0:
    print("Word Not found")
else:
    print("The number of repetitions is No. of Occurance: ",occurance)
    print("New List: ",newList)

```
