
# Python Set Operations

# 2. Python Set intersection()
# The intersection() method returns a new set with elements that are common to all sets.
# The syntax of intersection() in Python is: A.intersection(*other_sets)

# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using " & "
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# Output :
# Intersection using &: {1, 3}
# Intersection using intersection(): {1, 3}
