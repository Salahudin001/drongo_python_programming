b = ['data', 'and', 'book','structure', 'hello', 'st']
# adding 32 to the list
b += [32]
b = b + [32]
# print(b)

# removing an element from the list
b[2:4] = []
print(b)

new_list = b[5:]
print(new_list)

# delete the element at the first index
del b[0]
print(b)

# access elements at different indexes
a = ['data', 'structures','using', 'python', 'happy','learning']
print(a[0])
print(a[2])
print(a[-1])
print(a[-5])
print(a[1:5])
print(a[-3:-1])