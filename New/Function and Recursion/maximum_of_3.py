num1=int(input("Enter the number 1:-"))
num2=int(input("Enter the number 2:-"))
num3=int(input("Enter the number 3:-"))
def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("Maximum is ",num1)
    elif num2>num1 and num3>num1:
        print("Maximun is ",num2)
    else:
        print("Maximum is ",num3)
maximum(num1,num2,num3)
