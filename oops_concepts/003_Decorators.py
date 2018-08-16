# Decorators - comes when a function is passed 
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
    def wrapper(*args, **kwargs):
        print('Executing function - {}'.format(original_function.__name__))
        original_function(*args,**kwargs)
    return wrapper

@decorator_function
def display_info(name, age):
    print('My name is {name} and age is {age}'.format(name=name, age=age))


display_info(name = 'ram',age = 30)



