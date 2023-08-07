"""
input_string=input("Enter the string:-")
length=len(input_string)-1
reverse=""
for x in range(length,0):
    reverse=reverse+input_string[length]
    
print(reverse)
"""
"""
word=str(input("Enter the word:-"))
i=len(word)-1
reverse_word=""
def reverse(n):
    if n>0:
        reverse_word=reverse_word+reverse(i-1)  
reverse(w)
print(reverse_word)
"""
"""
def my_func(my_list):
    for x in range(n):
        if my_list[x]>=0:
            p=p+1
        else:
            n=n+1
my_list=[1,-2,3,-4]
p,n=0,0
pos,neg="",""
my_func(mylist)
my_dict =   {"pos": p,"neg": n}
print(my_dict)
"""
"""
#write a program to compare two list and print the common elements along with the count
#of the common elements
list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
list1.extend(list2)
len1=len(list1)
common=[]
i,count=0,0
for x in range(len1):
    i=x+1
    while(i<len1):
        if list1[x]==list1[i]:
            count=count+1
            common.append(list1[x])
            break
        i=i+1
print(count)
print(common)




def demo(L):
d={}
d["pos"]=0
d["neg"]=0
for num in L:
if num>0:
d["pos"]+=1
else:
d["neg"]+=1
print(d)
L=[1,-2,-3,4]
demo(L)
"""
"""
child1={"name":"sibu"}
child2={"name":"sinu"}
myfamily={"child1":child1,"child2":child2}
print(myfamily)
"""
count=8
print(count)

