# args - refers to wrapping position arguments to tuple
# **kwargs - refers to wrapping key = value arguments to dict

def foo(required, *args, **kwargs):
    if required:
        print(required)
    if args:
        print(args)
        # print('unpacks :',*args) # unpacks to positional arguments
    if kwargs:
        print(kwargs)

foo('Ram')
foo('Ram',1,2,3,4,5)
foo('Ram',1,2,3,4,5,key1='value1',10,11)

# foo('Ram',1,2,3,4,5,key1='value1',10,11)                                   ^
# SyntaxError: positional argument follows keyword argument


# important to understand
# * and ** in function definition refers to packing positional or kv pairs to tuple or list
# * and ** infront of list or dictionary unpacks item to positional arguments 
