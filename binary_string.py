string=input("Enter the binary String:-")
length=len(string)
count=0
flag=0
maximum=0
for x in range(0,length):
    if(string[x]=="0"):
        count=count+1
    elif(string[x]=="1"):
        maximum=max(maximum,count)
        count=0
    else:
        print("Invalid Input.Binary Number should contain only 1 and 0")
        flag=-1
        break
        
if(flag!=-1):
    print("The maximum length of consecutive 0's is ",maximum)