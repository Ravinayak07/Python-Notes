#given dictionary
mydict={'aa':111,'bb':112,'cc':113,'dd':114}
"""
The items() method returns a view object which contains the key-value pairs of
the dictionary as tuples in a list.For example,see the following code:-
"""
all_items= mydict.items()
print("1.All items(key-value pairs) in the given dictionary are:-",all_items)
print()#nextline
"""
The values() method returns a view object whichcontains the values of the
dictionary as a list.For example,see the following code:-
"""
all_values= mydict.values()
print("2.All values in the given dictionary are:-",all_values)
print()#nextline
"""
The get() method returns the value of the item with the specified key.
For example,see the following code:-
"""
specific_value = mydict.get("aa")
print("3.The value of the key aa is:- ",specific_value)
print()#nextline
#deleting the key "dd"
mydict.pop("dd")
print("The dictionary after deleting the key dd is:- ",mydict)
