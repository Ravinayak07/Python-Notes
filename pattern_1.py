n=int(input("Enter the value of n:-"))
y1=2*n-2
x1=0
space=" "
for x in range(0,n):
    print(y1*space,end="")
    i=x
    while(i>=0):
        print(i+1,end="")
        i=i-1
    print(x1*space,end="")
    for j in range(x+1):
        if x!=0:
            print(j+1,end="")
    print()
    y1=y1-2
    if x==0:
        x1=x1+1
    else:
        x1=x1+2
z=2
diff=n-5
x1=n+diff
for x in range(n-1,0,-1):
    print(z*space,end="")
    z=z+2
    i=x
    while(i>0):
        print(i,end="")
        i=i-1
    print(x1*space,end="")
    if x!=1:
        j=1
        while(j<=x):
            print(j,end="")
            j=j+1
        print()
    x1=x1-2
    

    




