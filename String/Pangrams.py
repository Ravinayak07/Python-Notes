string=input("Enter the String:-")
length=len(string)
i=0
count=0
new=string.lower()
alphabets=[]
while(i<length):
    character=new[i]
    if character>="a" and character<="z":
        if character not in alphabets:
            alphabets.append(character)
            count=count+1
    i=i+1
print(alphabets)
print(count)
if(count==26):
    print("Pangram")
    

        
           
    