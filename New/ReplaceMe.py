def ReplaceMe(n):
    mylist=[]
    print("Enter the elements in the list one by one:-")
    for x in range(0,n):
        element=int(input("Element for index %i is:-"%x))
        mylist.append(element)
    print("List before replacing:-",mylist)
    print()
    x=0
    sum=0
    for x in range(0,n):
        sum=sum+mylist[x]
        mylist[x]=sum
    print("List After replacing:-",mylist)
n=int(input("Enter how many elements you want to insert in list:-"))
ReplaceMe(n)