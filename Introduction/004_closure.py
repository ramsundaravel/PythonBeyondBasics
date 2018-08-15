# closure - storing function as a record along with associated environment variables
# refer example 3 for detailed information
def logging(tag):
    tag_info  = tag # free variable
    def tag_wrapper(msg):
        return ('<{0}> {1} </{0}>'.format(tag_info,msg)) # by default inner function takes outer functions value
    return tag_wrapper # here tag_wrapper is a function return

print_log = logging('h1')  # print_log stores the function - tag_wrapper. first class function
print(print_log('Test of tag!!'))  # now executing the function using print_log
# same concept as first class citizen

#---------------------------------------------------------#
#Example 2
import logging
logging.basicConfig(filename = 'example.log',level = logging.INFO)

def logging1(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(*args): 
    return sum(args) 

add_logger = logging1(add)
add_logger(1,2,3,4,5,6,7)
#---------------------------------------------------------#
# Exampl - 3
# how function within a function works
# closure comes into picture  when an outer function returns inner function
# closure involved when returned inner function is not self contained
# when an inner function relies on variables present on outer function, 
# closure ensures outer function variables are stored even outer function is gone away
# closure = function + outer context
# function is returned by outer function
# outer context are variables which inner function relies from outer function
import datetime
def stopwatch():
    starttime = datetime.datetime.now()

    def getdelay():
        return datetime.datetime.now() - starttime
        # here start time depends on outer function 
    return getdelay
    


timer = stopwatch()


# create artifical delay
for i in range(100000):
    pass

print('Time Elapsed - {}'.format(timer()))