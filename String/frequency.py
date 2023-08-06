string=input("Enter the String:-")
character=input("Enter the character whose frequency is to be checked:-")
length=len(string)
lower=character.lower()
upper=character.upper()
count,i=0,0
while(i<length):
    if string[i]==upper or string[i]==lower:
        count=count+1
    i=i+1
print(count)
