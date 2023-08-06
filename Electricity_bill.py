units = int(input("Enter the consumption units:"))
rate = [[0, 3], [100, 3.75], [250, 4], [300, 4.25], [400, 5]]
bill = 0
loop_counter = 0
while(units > 0):
    bill += rate[loop_counter][0]
    if loop_counter==4:
        bill += units * rate[loop_counter][1]
        break
    else:
        n = min(units, 150)
        bill += n * rate[loop_counter][1]
        units = units - 150
        loop_counter+=1   
print("The electricity Bill is Rs.",bill)

    
