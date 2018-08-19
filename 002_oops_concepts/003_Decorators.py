# Decorators - comes when a function is passed 
# maintain the additional functionalities in one place and resuse any number of times whereever needed
# For example,below we are passing display function --> orginal function parameter
# and display_decorator --> wrapper(). (as per first class function concept)
# per closure concept, wrapper holds information present in orginal function

# def decorator_function(original_function):
#     def wrapper():
#         print('Executing function - {}'.format(original_function.__name__))
#         original_function()
#     return wrapper


# def display():
#     print('display function ran')

# display_decorator = decorator_function(display)
# display_decorator() # executing wrapper function which inturn executes orginal function display

#----------------------------------------------------------------------------------------------

print('\n start of decorators')
# Decorators - does the above concept with different syntax
def decorator_function(original_function):
    def wrapper():
        print('Executing function - {}'.format(original_function.__name__))
        original_function()
    return wrapper

@decorator_function
def display():
    print('display function ran')


display()
# equivalent of display = decorator_function(display) . interms it points to wrapper
# advantage - extra functionalities can be added to a function without adding extra lines of code in calling function

#--------------------------------------------------------------------------------------------------
print('\ndecorators with arguments passed')

#  note in above example, initial display function is moved to orginial_function variable , then display points to wrapper. so now if we call display, its nothing but wrapper
# wrapper is defined with zero arguments. so if pass any args. to inital display function, problem comes
# solution - pass args, kwargs to wrapper and use it in orginal function

#Example 2
def decorator_function(original_function):
    def wrapper(*args, **kwargs): # advantage - optional params and not show error even if not passed
        print('Executing function - {}'.format(original_function.__name__))
        original_function(*args,**kwargs)
        print('\n')
    return wrapper

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('My name is {name} and age is {age}'.format(name=name, age=age))

display()
display_info(name = 'ram',age = 30)


#--------------------------------------------------------------------------------------------------
print('Decorator class')
# decorator class
# Rarely used

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self,*args, **kwargs): ## call method makes an instance executable
        # closure concepts applies over here
        print('call method executed before this {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)

#---------
# # information about __call__method__
# # call method makes the instance executable
# def display_info1(name, age):
#     print('My name is {name} and age is {age}'.format(name=name, age=age))

# a = decorator_class(display_info1)
# a('ram','test')
#---------


@decorator_class
def display_info(name, age):
     print('My name is {name} and age is {age}'.format(name=name, age=age))

display_info('Ram',31)
#--------------------------------------------------------------------------------------------------

# below examples shows how 2 decorators needs to be added
# will add content later
# when we give 2 decorators over a function , treat like nested function
# function1(function2(argument))
# execution is from outer to inner
# execute below code to under clearly 
# wraps helps to reassign the function name   
print('\n\n\nExample for decorators 4 ')

from functools import wraps

import time
def timeit_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Time Decorator started')
        starttime = time.time()
        func(*args, **kwargs)
        endtime = round((time.time() - starttime)*1000,4)
        print('"{}" function elapsed time - {} miliseconds'.format(func.__name__, endtime ))
        print('Time Decorator ended')
    return wrapper

import logging
logging.basicConfig(filename = 'example.log',level = logging.INFO)

def logging1(func):
    @wraps(func)
    def logger_func(*args,**kwargs):
        print('Log Decorator started')
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print('Running "{}" with arguments {}'.format(func.__name__, args))
        func(*args, **kwargs)  
        print('Log Decorator Ended')
    return logger_func


@timeit_decorator
@logging1
def dislay_information1(name, age):
    time.sleep(1)
    print('My name is {} and age is {}'.format(name, age))

dislay_information1('Ram',32)







