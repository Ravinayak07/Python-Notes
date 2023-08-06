dict={'x':100,'y':200,'z':300}
def add(dict):
    sum=0
    for x in dict:
        sum=sum+dict[x]
    return sum
print(add(dict))
    