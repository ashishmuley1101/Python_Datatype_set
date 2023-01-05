
# Python Set add() method.

# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing.
# Set data type does not support it.

# The syntax of add() method is: set.add(elem)

numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers)
# Output
# Initial Set: {34, 12, 21, 54}
# Updated Set: {32, 34, 12, 21, 54}

# -------Adding  tuple to a set--------------

# set of vowels
vowels = {'a', 'e', 'u'}

# a tuple ('i', 'o')
tup = ('i', 'o')

# adding tuple
vowels.add(tup)

print('Vowels are:', vowels)

# adding same tuple again
vowels.add(tup)

print('Vowels are:', vowels)

# Output
# Vowels are: {('i', 'o'), 'e', 'u', 'a'}
# Vowels are: {('i', 'o'), 'e', 'u', 'a'}
