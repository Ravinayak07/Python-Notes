def myfunc(x,length,letter):  
    if x == length:# it means there is no more letters to swap.so print
        print(''.join(letter)) 
    else:  
        for y in range(x, length):  
            letter[x],letter[y]=letter[y],letter[x]# swapping the letter in the yth index with xith index and pass it to next func
            myfunc(x+1,length,letter) #here since string upto xth index is fixed.we pass x+1
            letter[x],letter[y]=letter[y],letter[x]# this is done to back track .That means the string which was there before swapping is restored again.
string=input("Enter the String:-")    
myfunc(0,len(string),list(string))


