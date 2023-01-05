
# Python set any() method.

# The any() function returns True if any element of an iterable is True. If not, it returns False.
# The syntax of any() is: any(iterable)



# False since both are False
l = {0, False}
print(any(l))

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))