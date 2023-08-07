string=input("Enter the string to check for password:-")
length=len(string)
digit,letter=0,0
under_score=0
if(length<8):
    print("Invalid Password")
    print("A password must have atleast eight characters")
else:
    for x in range(0,length):
        if(string[x].isdigit()==True):
            digit=digit+1
        elif(string[x]=="_"):
            under_score=1
        elif(string[x]>="A" and string[x]<="Z" or string[x]>="a" and string[x]<="z"):
            letter=letter+1
    if(digit<2):
        print("Invalid Password")
        print("A password must have atleast two digits")
    elif(under_score==0):
        print("Invalid Password")
        print("A password must have underscore")
    elif(letter==0):
        print("Invalid Password")
        print("A password must have letters")
    else:
        print("%s is a Valid password"%string)
          