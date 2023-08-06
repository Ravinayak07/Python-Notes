n=int(input("Enter the size of the pattern:-"))
range1 = 50 
def myfunction1(a, x):  
    for i in range(x):  
        for j in range(x): 
            print(a[i][j], end = '')
            print(" ",end="")
        print() 
def myfunction2(n):    
    x = 2 * n - 1
    y = 0
    z = x - 1
    a = [[0 for i in range(range1)]   
            for i in range(range1)] 
    while (n != 0):  
        for i in range(y, z + 1): 
            for j in range(y, z + 1): 
                if (i == y or i == z or
                    j == y or j == z): 
                    a[i][j] = n 
        y=y+1
        z=z-1
        n=n-1
    myfunction1(a, x);  
myfunction2(n) 
 