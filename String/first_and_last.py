string=input("Enter the String:-")
length=len(string)
new=""
if length<2:
    print("Empty String")
else:
    second_last_index=length-2
    for x in range(0,2):
        new=new+string[x]
    while(second_last_index<length):
        new=new+string[second_last_index]
        second_last_index=second_last_index+1
    print(new)

    
