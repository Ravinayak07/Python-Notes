def factorial(small):
    if small==1 or small==0:
        return 1
    else:
        return small*factorial(small-1)
num1=int(input("Enter the 1st number:-"))
num2=int(input("Enter the 2nd number:-"))
small=0
if num1+num2>200:
    print("The sum is greater")
else:
    small=min(num1,num2)
    print("The factorial of %i is:-"%small,factorial(small))