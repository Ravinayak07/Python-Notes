print("Case1:printing pattern")
n=int(input("Enter the size of n:- "))
half=int(n/2)
for x in range(0,n):
    if(x==half):
        print("*"*n)
        continue
    y=1
    while(y<=n):
        if y==1 or y==n:
            print("*",end="")
        else:
            print(" ",end="")
        y=y+1
    print()
print()#nextline
print("Case2:concept of pop() in list")
#The pop() method removes the element at the specified position.
mylist=[10,50,45,99,89,78,90]
print("before using pop():- ",mylist)
mylist.pop(3)#This statement will remove the element at index 3 i.e'99' from list
print("After using pop():- ",mylist)



        

