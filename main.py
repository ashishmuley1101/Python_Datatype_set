
# Python Set len() method.

# The syntax of len() is: len(s) where s is set
# The len() function returns the number of items (length) in an object..

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))

# Output
# {1, 2, 3} length is 3
# set() length is 0
# {1: 'one', 2: 'two'} length is 2
# {} length is 0
# frozenset({1, 2}) length is 2