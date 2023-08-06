menu={"Rice":":-Rs.30","Dal":":-Rs.50","Roti":":-Rs.5","Panner":":-Rs.100","Chicken curry":":-Rs.120","Mutton curry":":-Rs.200"}
print("MENU:-")
count=1
bill=0
for x,y in menu.items():
    print(x,y)
n=int(input("Enter the number of orders:-"))
while(count<=n):
    order=input("Enter your Order:-")
    if order in menu:
        bill=bill+int(menu[order][5:])
        count=count+1
    else:
        print("Order is not present in menu")
        print("Kindly Reorder")
print("The Final Bill is:-Rs.",bill)

        
        
        

