n=int(input("Enter the total numbers to be entered in the List:-"))
print("Now Enter the numbers one by one")
thislist=[]
def myfunc(n):
    multi=1
    for x in range(0,n):
        element=int(input("Number for index %i is:-"%x))
        thislist.append(element)
    for x in range(0,n):
        multi=multi*thislist[x]
    return multi
print(myfunc(n))