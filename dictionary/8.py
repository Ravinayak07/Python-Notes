dict={'x':100,'y':200,'z':300}
def multi(dict):
    prd=1
    for x in dict:
        prd=prd*dict[x]
    return prd
print(multi(dict))
    