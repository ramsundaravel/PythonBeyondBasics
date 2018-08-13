class Employee:
    # class variables are common across all classes
    # use case - sharing same information for all instance of a class
    # example - annual pay raise should be same for all employees
    # example 2 - count number of variables

    pay_raise_pct = 0.04 # this is a class variables
    num_of_employees = 0

    def __init__(self, first, last, pay): # self defines passing instance of a class
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = self.fname + "."+self.lname+"@company.com"
        Employee.num_of_employees += 1 # this is defined with class.
        # because count at class level. (read this at end)

    def get_fname(self):# self defines passing instance of a class
        return '{} {}'.format(self.fname,self.lname)
    def raise_pay(self):
        return '{}'.format(float(self.pay) * self.pay_raise_pct)
        # to access class variable inside a method
        # either use class name - Employee.pay_raise_pct
        # or instance by using self - self.pay_raise_pct
        # self is better because - instance object by default inherits class variables
        # overriding concepts can be applied. when override happens, 
        # it will be part of instance variables list

print(Employee.num_of_employees)
emp1 = Employee('Ram','Kumar','70000')
emp2 = Employee('Test','User','80000')
print(emp1.raise_pay())
print(Employee.num_of_employees)

# overriding concepts of class variables
print('******Before overriding***** ' )
print('\t Value :',emp1.pay_raise_pct)
print('\t Variables :', emp1.__dict__)


# after override
emp1.pay_raise_pct = 0.05
print('******After overriding***** ' )
print('\t Value :',emp1.pay_raise_pct)
print('\t Variables :', emp1.__dict__)

emp1.num_of_employees = 10
print(Employee.num_of_employees)
print(emp1.num_of_employees)
# hierachy here  - instance variable, class variable.
# changes made through instance can't get change if we call that variable
# using class name

