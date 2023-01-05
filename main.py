
# Python Set discard() method.

# The syntax of discard() method is: a.discard(x)
# Here, a is the set and x is the item to discard.

numbers = {2, 3, 4, 5}

# discards 3 from the set
numbers.discard(3)

print('Set after discard:', numbers)
# Output : Set after discard: {2, 4, 5}

numbers.discard(10)

print('Set after discard:', numbers)
# Output : Set after discard: {2, 4, 5}