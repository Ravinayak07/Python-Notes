mytuple=(1,2,9,4,5,6)
print(mytuple)
mylist=list(mytuple)
mylist[2]=3 #changing 9 into 3
mytuple=tuple(mylist)
print("New Tuple after changing the value of 3rd element is:- ",mytuple)
print("Length is ",len(mytuple))