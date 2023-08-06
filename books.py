num=int(input("Enter the number of employees:-"))
mydict={}
for i in range(num):
    print()
    print("Enter the details of Employee %i "%(i+1))
    Name=input("enter the name of the employee:-")
    ID=int(input("enter Emplyoee id:-"))
    Qualification=input("enter the qualifiaction:-")
    Age=int(input("enter age:-"))
    address=input("Enter address:-")
    mydict[(Name,ID)]=(Age,Qualification,address)
print(mydict)
           
    