string=input("enter the string:-")
length=len(string)
letter=""
i = 0
upper,lower=0,0
while(i<length):
    letter=string[i]
    if letter>="A" and letter<="Z":
        upper=upper+1
    elif letter>="a" and letter<="z":
        lower=lower+1
    i=i+1
print("Number of uppercase letters are ",upper)
print("Number of lowercase letters are ",lower)
    
    
    