# Recursion is the process in which a function calls itself. 
# Recursive functions are used mostly for sequence generation and are used to make the code look clean and elegant.

def rec_sum(n):
    if n <= 1:
        return n
    else:
        return n + rec_sum(n-1)


y = rec_sum(5)
print(y)
