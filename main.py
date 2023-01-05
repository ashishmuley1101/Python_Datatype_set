
# Creating set datatype in python

# Sets by placing all the elements inside curly braces {}, separated by comma.

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Output :
# Student ID: {112, 114, 115, 116, 118}
# Vowel Letters: {'i', 'u', 'e', 'o', 'a'}
# Set of mixed data types: {'Hello', 'Bye', 101, -2}

# --------Create an Empty Set in Python----------------

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# O/p : Data type of empty_set: <class 'set'>

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
# Data type of empty_dictionary <class 'dict'>

set1 = set(range(1, 6))  # Create set using range
print(set1)   # O/p : {1, 2, 3, 4, 5}


# ----Duplicate Items in a Set------------------------------
#  no duplicate items in the set as a set cannot contain duplicates.

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # O/p :  {8, 2, 4, 6}

