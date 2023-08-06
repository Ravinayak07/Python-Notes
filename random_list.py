import random
n=int(input("Enter how many numbers you want to generate randomly:-"))
mylist=[]
length=0
sum_of_digits=0
for x in range(0,n):
    n=random.randint(0,99)
    mylist.append(n)
length=len(mylist)
print("List before deleting and converting:-")
print(mylist)
print()
x=0
while(x<length):
    count=0
    if(mylist[x]%3==0):
        mylist.remove(mylist[x])
        x=x-1
        length=length-1
    else:
        while(int(mylist[x]/10)!=0):
            sum_of_digits=(mylist[x]%10)+int(mylist[x]/10)
            mylist[x]=sum_of_digits
    x=x+1
print("List after deleting and converting :-")
print(mylist)

                
            
            
        
    

        