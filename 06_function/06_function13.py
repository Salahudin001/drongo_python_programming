# The Python reduce() function is mostly used to reduce the entire list into a single result.

# The reduce() function needs to be imported from the functools module. Functools is one of the modules in python which contains some higher-order functions.

# The reduce() function takes the two arguments: the first is the function, and the second is the list.

# Syntax : reduce( function, list)

# The reduce() function iterates over the given list of numbers, and these numbers are passed to the lambda function as a parameter. When the entire list is iterated, the final result is returned by the reduce() function.

# Let’s suppose we have the list of numbers and do the addition of all these numbers.

#importing reduce() function from functools module
from functools import reduce
 
# Given list of numbers
numbers = [ 1, 2, 3, 4, 5, 6]
 
# One liner code to do the addition of all numbers using reduce() function
sum = reduce((lambda x, y: x + y), numbers)
 
# Result of addition
print(sum) #21


