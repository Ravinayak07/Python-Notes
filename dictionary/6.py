dict1={1:10,2:20}
dict2={3:30,4:40}
def merge(dict1,dict2):
    return(dict1.update(dict2))
merge(dict1,dict2)
print(dict1)