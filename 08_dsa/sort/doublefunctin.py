def function_in_a_function(s):
    s=[8,4,6,5,9,7,4,6,6,6,4,12,79,35,8]
    if s =='even':
        return lambda n : n%2 ==0
    elif s =='positive':
        return lambda n:n>0
    elif s =='negative':
        return lambda n:n<0
    else :
        raise ValueError ('Unknown request')

   