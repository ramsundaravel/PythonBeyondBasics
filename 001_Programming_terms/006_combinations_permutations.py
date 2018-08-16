# Combinatins - different ways to arrange a group and not considering orders
# Premutations - different ways to arrange a group with considering orders
# Example for combinations and premutations
import itertools
name_list = [1,2,3]

combinations = itertools.combinations(name_list,2)
premutations = itertools.permutations(name_list,2)
print('Combinations :')
for p in combinations:
    print(p)

print('Permutations')
for p in premutations:
    print(p)

# Combinations : here group of 2 without considering order
# (1, 2)
# (1, 3)
# (2, 3)

# Permutations : here group of 2 by considering order
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)

# use case for combination for combination and premutation
# combination
# find the different groups with each group contains 3 elements 
# sum of 3 elements in each group should result to 10
# order of the elements within group doesnt mater
print('\n')
print('Use case for combination')
my_list = [1,2,3,4,5,6,7,8]
combinations = itertools.combinations(my_list,3)
for group in combinations:
    if sum(group) == 10:
        print(group)

# Use case for combination
# (1, 2, 7)
# (1, 3, 6)
# (1, 4, 5)
# (2, 3, 5)


# permutation
# find weather word 'sample' present in the letter combination of 'lemaps'
print('\n')
print('Use case for permutation')
match_word = 'sample'
given_word = 'lempsta'
permutations = itertools.permutations(given_word,6)
for permutation in permutations:
    word = "".join(permutation)
    if word == match_word:
        print(permutation)
        print('Match found')
        break
else:
    print('No Match found')

# Use case for permutation
# ('s', 'a', 'm', 'p', 'l', 'e')
# Match found

# careful to use permutation because it takes more computation power