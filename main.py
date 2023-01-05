
# Python sorted() method.

# The sorted() function sorts the elements of a given iterable in a specific order
# (ascending or descending) and returns it as a list
# The syntax of sorted() is: sorted(iterable, key=None, reverse=False)
# sorted() can take a maximum of three parameters:
# iterable - A sequence (string, tuple, list) or collection
# (set, dictionary, frozen set) or any other iterator.
# reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order).
# Defaults to False if not provided.
# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

numbers = {4, 2, 12, 8}

sorted_numbers = sorted(numbers)
print(sorted_numbers)
# Output: [2, 4, 8, 12]

# vowels tuple
vowels = {'e', 'a', 'u', 'o', 'i'}
print(sorted(vowels))   # O/p : ['a', 'e', 'i', 'o', 'u']

# -------Sort in descending order----------------------

numbers = {4, 2, 12, 8}

sorted_numbers = sorted(numbers, reverse = True)
print(sorted_numbers)

# vowels tuple
vowels = {'e', 'a', 'u', 'o', 'i'}
print(sorted(vowels,reverse = True))

# Output :
# [12, 8, 4, 2]
# ['u', 'o', 'i', 'e', 'a']

