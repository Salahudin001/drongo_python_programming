# The Python map() function is mostly used to modify the items in the list.

# It takes two arguments, the first argument is the lambda function as an anonymous function, and the second argument is the list.

# Syntax : map( function, list)

# The map() function iterates over the list provided as a parameter and each value is passed as a parameter to evaluate with the expression of the lambda function. Then these evaluated values get returned one after another.

# Suppose we want to create a list of squares of numbers from the given list of numbers.

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# One liner code to create the list of squares of the numbers using map() function
sq_numbers = list(map((lambda x : x*x), numbers))
 
# Printing the new list
print(sq_numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
