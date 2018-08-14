# First class citizen - treat function as smiliar to objects and variables
# higher order function  - passing function as an arguement to another function

# Example for assigning function to a variables
def square(x):
    return x * x

def cube(x):
    return x * x * x

f = square  # assigning a function without variable wont execute
# it will just assign the function to a variable. first class citizen
# then use that variable to execute a function
print(square)
print(f(10))

################################################
# Example - passing a function to a function
# map is a example of passing a function over function
def my_map(func, numbers):
    result = []
    for i in numbers:
        result.append(func(i))
    return result
print("square using map function : ", my_map(square,[1,2,3,4,5]))
# square function is sent to my_map and assgining to func and will get execute
print("cube using mapping function :" , my_map(cube, [1,2,3,4,5]))
################################################

# Example - returning function as return type
# use case - logging
def logging(tag):
    def tag_wrapper(msg):
        return ('<{0}> {1} </{0}>'.format(tag,msg)) # by default inner function takes outer functions value
    return tag_wrapper # here tag_wrapper is a function return

print_log = logging('h1')  # print_log stores the function - tag_wrapper. first class function
print(print_log('Test of tag!!'))  # now executing the function using print_log
# same concept as first class citizen





