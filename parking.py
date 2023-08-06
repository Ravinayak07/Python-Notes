def calculation(wait_time,vehicle):
    rate=0 
    if vehicle=="C":
        if wait_time<=3:
            rate=10*wait_time
        else:
            rate=20*wait_time
    elif(vehicle=="B"):
        if wait_time<=3:
            rate=20*wait_time
        else:
            rate=30*wait_time
    elif(vehicle=="S"):
        if wait_time<=3:
            rate=5*wait_time
        else:
            rate=10*wait_time
    print("Charge for %i hrs is:-"%wait_time,rate)

vehicle=""
hrs1=hrs2=min1=min2=0
wait_time=0         
print("Enter the  character for respective vehicle:-")
print("1.Enter 'C' for Car")
print("2.Enter 'B' for Bus/truck")
print("3.Enter 's' for scooter/cycle/motorcycle")
vehicle=input("Enter your choice:-")
print("Now enter the time in hrs and min.For example if time is 10:30,then enter 10 for hrs and 30 for minuites")
print("Enter the Entering time:")
hrs1=int(input("Enter the hours:- "))
min1=int(input("Enter the minuites:-"))
print()#nextline
if(hrs1>=1 and hrs1<=24 or min1>=1 and min1<=60):
    print("Enter the leaving time:")
    hrs2=int(input("Enter the hours:- "))
    min2=int(input("Enter the minuites:-"))
    if(hrs1>=1 and hrs1<=24 or min1>=1 and min2<=60):
        if(hrs1==hrs2):
            wait_time=min2-min1
        elif(hrs1<hrs2):
            if(hrs2-hrs1==1):
                wait_time=60-min1+min2
            else:
                wait_time=(hrs2-hrs1-1)*60+60-min1+min2  
        else:
            print("Invalid leaving time can't be less than entering time")
        wait_time=int(wait_time/60)
        calculation(wait_time,vehicle)
    else:
        print("Invalid input")
        print("hours should be less than 24 and minuites should be less than 60")   
else:
    print("Invalid input")
    print("hours should be less than 24 and minuites should be less than 60")