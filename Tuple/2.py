tuple1=(10,)
tuple2=(20,30,40)
print(tuple1)
print(tuple2)
list1=list(tuple1)
list2=list(tuple2)
y=len(list2)
for x in range(0,y):
    list1.append(list2[x])
tuple1=tuple(list1)
print(tuple1)


