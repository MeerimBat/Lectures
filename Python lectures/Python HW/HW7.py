
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
words=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

#sorted_strings = sorted(words)
sorted_strings = sorted(words, key=lambda s: (s[0] != 'x', s))
print(sorted_strings)

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

tuples_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)



