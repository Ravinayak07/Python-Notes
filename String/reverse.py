word=input("Enter the word:-")
i=len(word)-1
reverse=""
while(i>=0):
    reverse=reverse+word[i]
    i=i-1
print(reverse)