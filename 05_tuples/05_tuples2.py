temptuple = ('apple', 'mango', 'oranges', 'bananas')
result = temptuple+(1, 2, 3)
print('concatenation of a tuple', result)

result = temptuple*3
print('repetition of a tuple', result)

result = len(result)
print('length of temptuple:', result)

result = 'apple' in temptuple
print('membership check', result)

sum = 0
for fruit in temptuple:
    print("for loop", fruit)
    sum = sum+1

print(sum)


m = 5
n = m + 6
