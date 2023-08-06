list1=[]
num=0
n=int(input("How many numbers you want to enter:-"))
print("Now enter the numbers one by one")
for x in range(0,n):
    num=int(input("Number for index %i is :-"%x))
    list1.append(num)
list2=[]
for x in range(0,n):
    if list1[x] not in list2:
        list2.append(list1[x])
print(list1)
print(list2)

    