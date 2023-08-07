"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  print("rvai")
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True,key=myFunc)

print(cars)
"""
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""
"""
#list can store homo and heterogenous dsts types
#nested list:- a=[1,2,3,[4,5,6],7]
#a=[]
a=list()
print(type(a))
b=[1,2,3,[4,5,6],7]
print(b[3][2])
print(b.index(2))#gives the index position
#reverse() just reversed
#sort.(reverse=True) first sorts and then reverse
append(3),extend([5,6])
"""
"""
mylist=[77,25]
x=0
sum_of_digits=""
while(len(sum_of_digits)!=1):
    sum_of_digits=int(sum_of_digits)
    sum_of_digits=(mylist[x]%10)+int(mylist[x]/10)
    mylist[x]=sum_of_digits
print(mylist[x])
"""
"""
mylist=[89,2]
x=1
while(int(mylist[x]/10)!=0):
    sum_of_digits=(mylist[x]%10)+int(mylist[x]/10)
    mylist[9x]=sum_of_digits
print(mylist[x])
                                
"""

"""
"""
"""
write a program in python having class name student consisting of both public
and private datamembers. Create a function which will display all the data members.
"""
"""
print("{0:03d}".format(2*4) ,end="")
"""
"""
Create a class name as sample having three different classes.
Implement the concept of multilevel inheritance by taking the values
in each of the class at runtime
"""

class sample:
name =" "
age = 0
class a(sample):
marks=" "
class b(a):
height=" "
def read(self):
print("Enter details;")
self.name=input("enter name")
self.age=int(input("enter age"))
self.marks=int(input("enter marks"))
self.height=int(input("enter height"))
def display(self):
print("values are:")
print("name is",self.name)
print("age is",self.age)
print("marks are",self.marks)
print("height is",self.height)
obj=b()
obj.read()
obj.display()

