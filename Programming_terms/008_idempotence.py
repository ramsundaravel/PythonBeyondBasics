# this is for understanding purpose only
# not using in day by day cases

# definition : f(f(x)) = f(x)
# wich means if we pass output of a function to the same function again and if it yeilds same result, 
# then given function is idempotence

def add_ten(num):
    return num + 10

print(add_ten(add_ten(10)))
# this is not idempotence

print(abs(abs(abs(-10))))
# above one is idempotence

x = 10
# keep running x = 10 yeilds same value and this is idempotence