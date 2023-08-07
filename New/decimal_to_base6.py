import math
num=int(input("Enter the decimal integer :- "))
y=0
base_num,last_rem=0,0
while(num!=0):
    rem=num%6  #to get the remainders
    base_num=int(math.pow(10, y))*rem+base_num
    y=y+1  #increments y
    last_rem=int(num) #for storing the last remainder
    num=int(num/6)
print("The base 6 representation is:-",base_num)