"""
Program to print * * * * * *
                 * * * * * *
                 * * * * * *
                 * * * * * *
                 * * * * * *
                 * * * * * *
                 * * * * * *
"""


"""
n=int(input("Enter the value of n:-"))
for x in range(n):
    print(n*"* ")
"""



#another method
for i in range(1,8):
    for j in range(1,8):
        print("* ",end="")#end is for printing horizontally
    print()#prints nothing,used to transfer the cursor to the next line
