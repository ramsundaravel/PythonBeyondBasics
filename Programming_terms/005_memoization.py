# Memoization is a concept of memorizing the result of costly  function calls as cache
# looking back into cache for availability of answer before proceeding into actula function call

import time
res_cach = {}

def func(num):
    print('Calculating square for {}'.format(num))

    if num in res_cach:
        return res_cach[num]
    time.sleep(1)
    result = num * num
    res_cach[num] = result
    return result


print(func(10))
print(func(20))
# Below function calls takes result from res_cach and not doing costly function calls
print(func(10))
print(func(20))
# This will be mostly helpful when same function multiple times
    
    