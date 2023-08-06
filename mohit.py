N=int(input("Enter the value of N:- "))
x,y=0
z=0
for x in range(1,N+2):
    if(x%2!=0):
        y=1
        while(y<=x):
            print(y,end="")
            y=y+1
        print()
    else:
        z=97+x
        for y in range(97,z):
            print(chr(y),end="")