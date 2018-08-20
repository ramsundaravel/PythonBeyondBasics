# Generators - 
# Regular function returns all the values at a time and goes off
# but generator provides one value at a time and waits for next value to get off. function will remain live
# it basically yields or stops for next call
# basically not returning all values together. returning one value at a time

def generator_example(num):
    for i in range(1,num):
        print('Loop started for {}'.format(i))
        yield i
        print('Loop end for {}'.format(i))

test = generator_example(10)
# print('1*********')
# print(next(test),'\n')

# print('2*********')
# print(next(test),'\n')

# print('3*********')
# print( next(test),'\n')
# print('*********')

# alternative way of call
for x in test:
    print(x)
    print('\n')


#****************************************#
print('Square example using generators')
def square(num):
    for i in num:
        yield i * i

sq = square([1,2,3,4,5,6])
# sq is  a generator object pointing to the function square
# now call sq till end of iteration using for loop or through next method method
# advantage memory saving and performance
for i in sq:
    print (i)
# it yields one value 