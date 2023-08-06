def palindrome(word):
    i=len(word)-1
    reverse=""
    while(i>=0):
        reverse=reverse+word[i]
        i=i-1
    if reverse==word:
        print(word+" is a palindrome")
    else:
        print(word+" is not a palindrome")
word=input("Enter the word:-")
palindrome(word)