n=int(input("Enter any number which is divisible by 3:-"))
i=1
y=(n-n/3)
z=int(y)
b=(2*n)/3
x=y+1
while i<=n:
    if i==1 or i==n:
        print(z*"* ")
        
    elif  i>1 and i<=n/3:
        j=1
        while j<=x:
            if j==1 or j==x:
                print("*",end="")
            else:
                print("  ",end="")
            j=j+1
        x=x+1
        print()
    
    elif i>n/3 and i<b:
        j=1
        while j<=n:
            if j==1 or j==n:
                print("*",end="")
            else:
                print("  ",end="")
            j=j+1
        print()
    elif i>=b and i<=n:
         j=1
         while j<=x:
            if j==1 or j==x:
                print("*",end="")
            else:
                print("  ",end="")
            j=j+1
         x=x-1
         print()     
    i=i+1

    
      
                 
                 
                 
         
        
            
                
            
                
            
        
       
    
    