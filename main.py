
# Python set enumerate() method.

# The enumerate() method adds a counter to an iterable and returns it (the enumerate object).
# You can convert enumerate objects to list and tuple using list() and tuple() method respectively
# The syntax of enumerate() is: enumerate(iterable, start=0)
# iterable - a sequence, an iterator, or objects that supports iteration
# start (optional) - enumerate() starts counting from this number.
# If start is omitted, 0 is taken as start.

languages = {'Python', 'Java', 'JavaScript'}

enumerate_lang = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_lang))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)  # start with 10
print(list(enumerateGrocery))
# Output
# <class 'enumerate'>
# [(0, 'bread'), (1, 'milk'), (2, 'butter')]
# [(10, 'bread'), (11, 'milk'), (12, 'butter')]