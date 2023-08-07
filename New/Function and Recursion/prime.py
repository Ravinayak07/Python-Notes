def prime_func(num):
    i,count=1,0
    while(i<=num):
        if num%i==0:
            count=count+1 
        i=i+1
    return count
num=int(input("Enter the number:-"))
if prime_func(num)==2:
    print(num," is a prime number")
else:
    print(num," is not a prime number")
