fruits={}
count=0
def AddMe():
    fruits={} 
    n=int(input("how many different fruits you want to sell:-"))
    for x in range(0,n):
        fruit_name=input("%i.Fruit name:- "%(x+1))
        quantity=int(input("  Quantity(in numbers):- "))
        fruits[fruit_name]=quantity
    print("stock is :-",fruits)
    print(FindMe(fruits))
    DelMe(fruits)  
def FindMe(fruits):
    print()
    fruit_name=input("Fruit name to find its quantity:- ")
    if fruit_name in fruits:
        print("The quantity of %s is:-"%fruit_name,end="")
        return fruits[fruit_name]
    else:
        print("Invalid Input")
        print("There is no fruit with name %s in the stock"%fruit_name)
def DelMe(fruits):
    print()
    delete_name=input("Fruit name to delete:- ")
    if delete_name in fruits:
        fruits.pop(delete_name)
        print("Stock after deleting is :-",fruits)
        SellMe(fruits)
    else:
        print("Invalid Input")
        print("There is no fruit with name %s in the stock"%delete_name)
def SellMe(fruits):
    name=input("Fruit that customer want to buy:- ")
    if name in fruits:
        quantity=int(input("how much quantity of %s want to buy:- "%name))
        if quantity<=fruits[name]:
            fruits[name]=fruits[name]-quantity
            print("Sold fruit: ",name)
            print("Sold quantity: ",quantity)
            print()
            print("Stock after selling:",fruits)
        else:
            print("Sorry,there is only %i in stock"%fruits[name])
    else:
        print("Invalid Input")
        print("There is no fruit with name %s in the stock"%name)
        Goto .end
AddMe()

        
        
    


        