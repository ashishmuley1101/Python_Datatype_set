
# Python Set Operations

# 1. Union of Two Sets
# The union of two sets A and B include all the elements of set A and B.

# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using " | " symbol
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B))

# Output
# Union using |: {0, 1, 2, 3, 4, 5}
# Union using union(): {0, 1, 2, 3, 4, 5}

