# Decorators with arguments
# here prefix decorator returns decorator function which in turn takes display function as argumemt 

def prefix_decorator(prefix, subfix):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            print(prefix + subfix+ ' Executing before start of {} function'.format(func.__name__))
            func(*args, **kwargs)
            print(prefix + subfix +  ' Executing after end of {} function'.format(func.__name__))
        return wrapper
    return decorator_function

@prefix_decorator('Log : ','Sucess')
def display_info(name, age):
    print('Name is {} and age is {}'.format(name, age))

display_info('Ram',32)

# evaluation display info = prefix_decorator--> decorator_function(display_info)

# Result 
# Log :Executing before start of display_info function
# Name is Ram and age is 32
# Log :Executing after end of display_info function