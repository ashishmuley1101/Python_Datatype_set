
# Python Set update() method.

# The syntax of update() method is: A.update(B)
# Here, A is a set and B can be any iterable like list, set, dictionary, string, etc.

A = {'a', 'b'}
B = {1, 2, 3}

# updates A after the items of B is added to A
A.update(B)

print(A)
# Output: {1, 2, 3, 'b', 'a'}

c = {1, 3, 5}
d = {2, 4, 6}
e = {0}

print('Original A:', A)

# adds items of B and C to A and updates A
c.update(d, e)

print('c after update()', c)
# Output :
# Original A: {1, 2, 'a', 3, 'b'}
# c after update() {0, 1, 2, 3, 4, 5, 6}

# -------------update() to add String and Dictionary to Set-----

# string
alphabet = 'odd'

# sets
number1 = {1, 3}
number2 = {2, 4}

# add elements of the string to the set
number1.update(alphabet)

print('Set and strings:', number1)

# dictionary
key_value = {'key': 1, 'lock' : 2}

# add keys of dictionary to the set
number2.update(key_value)

print('Set and dictionary keys:', number2)

# Output
# Set and strings: {1, 3, 'o', 'd'}
# Set and dictionary keys: {'lock', 2, 4, 'key'}