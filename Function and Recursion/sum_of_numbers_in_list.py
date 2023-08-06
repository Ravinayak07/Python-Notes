n=int(input("Enter the total numbers to be entered in the List:-"))
print("Now Enter the numbers one by one")
thislist=[]
def myfunc(n):
    sum=0
    for x in range(0,n):
        element=int(input("Number for index %i is:-"%x))
        thislist.append(element)
    for x in range(0,n):
        sum=sum+thislist[x]
    return sum
print(myfunc(n))

    

    
