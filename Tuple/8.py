mytuple=(1,2,3,4,5)
print(mytuple)
newtuple=mytuple[::-1]
print(newtuple)

"""
#2nd method
mytuple=(1,2,3,4,5)
print(mytuple)
list1=list(mytuple)
list2=[]
i=len(list1)-1
while(i>=0):
    list2.append(list1[i])
    i=i-1
mytuple=tuple(list2)
print(mytuple)
"""
    
