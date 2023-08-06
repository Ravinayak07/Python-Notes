n=int(input("Enter the number of elements:-"))
print("Now enter each element one by one:-")
item,count=0,0
y=0
mylist=[]
for x in range(0,n):
    item=int(input("The Element for index %i is :-"%(x)))
    mylist.append(item)
mytuple=tuple(mylist)
print=(int(input("Enter the element whose occurance is to be calculated:-")))
range1=int(input("Enter the first index:-"))
range2=int(input("Enter the extreme index:-"))
while(range1<=range2):
    if item==mytuple[range1]:
        count=count+1
    range1=range1+1
print(count)



    
    