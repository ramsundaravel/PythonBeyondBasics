# defining a class
class Employee:
    # __init__ is used to initialize instance variables
    # equivalent of constructor in Java
    # automically called when defining instance of a class

    def __init__(self, first, last, pay): # self defines passing instance of a class
        self.fname = first   # these are all instance variables
        self.lname = last    # which means specific to one instance
        self.pay = pay
        self.email = self.fname + "."+self.lname+"@company.com"

    def get_fname(self):# self defines passing instance of a class
        return '{} {}'.format(self.fname,self.lname)

# class instance 
# variables and functions inside a class are instance variables 
# and instance methods

emp1 = Employee('Ram','Kumar','70000')
emp2 = Employee('Test','User','80000')

print(emp1.get_fname()) # here instance is automatically passed
print(Employee.get_fname(emp2)) # equivalent of above statement. 
# Passing instance manually. this is behind the scene how instance method works.