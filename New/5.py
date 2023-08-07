n=int(input("Enter no. of terms:-"))
x,y,i=0,1,1
print("The Fibonacci Series upto %d terms is" %n)
print(x ,y ,end="")
while(i<=n):
    sum=x+y
    print(" %d" %sum,end="")
    x=y
    y=sum
    i=i+1
