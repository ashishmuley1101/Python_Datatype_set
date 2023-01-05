
# Python Set Operations

# 3. Python Set difference()
# The difference() method computes the difference of two sets and returns items that are unique to the first set.
# The syntax of the difference() method is: A.difference(B) or A - B

# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform difference operation using " - "
print('Difference using - :', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# Output :
# difference using - : {5}
# difference using difference(): {5}
