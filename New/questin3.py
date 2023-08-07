def pattern(N):
    x,y=0,0
    z=0
    for x in range(1,N+2):
        if(x%2!=0):
            y=1
            while(y<=x):
                print(y,end="")
                y=y+1
        else:
            z=65+x
            for y in range(65,z):
                print(chr(y),end="")
        print()
N=int(input("Enter the value of N:- "))
pattern(N)