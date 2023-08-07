"""
word=str(input("Enter the word:-"))
i=len(word)-1
reverse=""
while(i>=0):
    reverse=reverse+word[i]
    i=i-1
print(reverse)
"""
"""
word=str(input("Enter the word:-"))
i=len(word)-1
reverse_word=""
def reverse(i):
    if i>0:
        reverse_word=reverse_word+reverse(i-1)  
reverse(word)
print(reverse_word)
"""
"""
num=int(input("Enter the number:-"))
def fact(num):
   if num<0:
       return 0
   if num==1:
       return num
   else:
       return num*fact(num-1)
x=fact(num)
if x==0:
    print("negative number")
else:
    print(x)
"""
"""
def fact(n):
if n<0:
print("Enter non-negative integer")
elif n==0 or n==1:
return(1)
else:
return(n*fact(n-1))

n=int(input("Enter number: "))
print("Factorial=",fact(n))
"""

num=int(input("Enter the number:-"))
def factorial(num):
    fac=1
    if num==0 or num==1:
        return 1
    elif num<0:
        print("Non negative number entered")
    else:
        while(num>0):
            fac=fac*num
            num=num-1
        return  fac
print(factorial(num))


        
