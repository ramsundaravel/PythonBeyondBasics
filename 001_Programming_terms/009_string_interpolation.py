# String Interpolation - 
# In computer programming, string interpolation (or variable interpolation, variable substitution, 
# or variable expansion) is the process of evaluating a string literal containing one or more placeholders,
# yielding a result in which the placeholders are replaced with their corresponding values.

# in simple terms - string interpolation is process of putting place holders in sting
# evaluating it later

name = 'Ram'
age = 32

greeting1 = 'my name is ' + name + '. My age is ' + str(age)
# this is not string interpolation but string concatenation. 
# here age needs to converted to str before concat

greeting2 = 'My name is {name}. My age is {age}'.format(name=name,age=age)
# above is string interpolation
# easy readability and easy to debug
# useful when we create strings from database

print(greeting1)
print(greeting2)
