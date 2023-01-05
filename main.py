
# Python Set Operations

# 4. Python Set symmetric_difference()
# The symmetric_difference() method returns all the items present in given sets,
# except the items in their intersections
# The syntax of the symmetric_difference() method is: A.symmetric_difference(B) or A ^ B

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using " ^ "
print('using ^ :', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# Output :
# using ^ : {1, 3, 5, 6}
# using symmetric_difference(): {1, 3, 5, 6}}
