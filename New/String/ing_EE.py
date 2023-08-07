string=input("Enter the String:-")
length=len(string)
new=""
ing=""
if length<3:
    print(string)
else:
    ing=string[length-3:]
    if ing=="ing":
        new=string+"EE"
    else:
        new=string+"ing"
print(new)
