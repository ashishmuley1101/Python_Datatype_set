
# Python set sum() method.

# The sum() function adds the items of an iterable and returns the sum.
# The syntax of sum() is: sum(iterable, start)
# The sum() function adds start and items of the given iterable from left to right.
# iterable - iterable (list, tuple, dict, etc). The items of the iterable should be *numbers*.
# start (optional) - this value is added to the sum of items of the iterable. The default value
# of start is 0 (if omitted).

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)

# Output
# 4.5
# 14.5