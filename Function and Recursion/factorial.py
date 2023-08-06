def factorial(num):
    if num<0:
        print("You have entered a Negative Number")
    elif num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
        
num=int(input("Enter a non-negative integer:-"))
print(factorial(num))
