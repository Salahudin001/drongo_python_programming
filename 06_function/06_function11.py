# The filter() function in Python will help us to filter the lists.

# The filter function takes two arguments: the first is the lambda function as an anonymous function, and the second argument is the list of numbers.

# Syntax: filter(function, list)

# When we call the filter function, it iterates over the provided list and passes every value one by one to the function, which returns true or false.

# If that particular value's result is true, it gets added to the list. The classic example of lambda functions with the filter() method is to filter out the even or odd numbers from a list of numbers.


#List of numbers
numbers = [1,2,3,4,5,6,7,8]
 
# one liner code to make list of even numbers using filter() function
even_no = list(filter((lambda x : x % 2 == 0), numbers))
 
# even numbers list
print(even_no) # [2, 4, 6, 8]
