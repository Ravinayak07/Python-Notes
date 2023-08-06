sentence=input("Enter the sentence:-")
sentence=sentence+" "
length=len(sentence)
i,i2=0,0
both,count=0,0
upper,lower=0,0
index1,index2=0,0
u,l=0,0
j=0
word=""
reverse=[]
new_sentence=""
while(i<length):
    i2,length2=0,0
    if sentence[i].isspace()==True:
        index2=i
        word=sentence[index1:index2]
        length2=len(word)
        while(i2<length2):
            if(word[i2].isupper()==True):
                upper=1
                new_sentence=new_sentence+word[i2].lower()
            elif(word[i2].islower()==True):
                lower=1
                new_sentence=new_sentence+word[i2].upper()
            i2=i2+1
        if upper==1 and lower==1:
            both=both+1
        elif upper==1 and lower==0:
            u=u+1
        elif upper==0 and lower==1:
            l=l+1
        upper=lower=0
        new_sentence=new_sentence+" "
        index1=index2+1
        if word[::-1].lower()==word.lower():
            reverse.append(word)
    i=i+1
print("Number of Words having Only Uppercase Letters :-",u)
print("Number of Words having Only Lowercase Letters :-",l)
print("Number of Words having both Uppercase and lowercase Letters :-",both)
print("Palindromes are:- ",reverse)
print("After Changing  the case,the new sentence is:-")
print(new_sentence)
        
    
    