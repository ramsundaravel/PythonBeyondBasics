# Iterable - list, tuples, dict, files, etc. 
# iterable is capable of creating iterator
# Example 
my_list = [1,2,3,4,5]

print('Providing list of methods present in my_list object')
print(my_list.__dir__())

# iter method is capable of making the list iteratable or creating iteration
# next method is used to move one element to another in iteration
print(my_list.__iter__())

itr = my_list.__iter__()
print(next(itr))
print("----")

for x in itr:
    print(x)

# above code equivalent given below
print(list(itr))
