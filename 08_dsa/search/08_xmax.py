test_values = [1, 2, 3, 4, 5, 6, 0]

def maximum(values):
    answer = None
    for value in values:
        if answer == None or answer > value:
            answer = value
            print(answer)
    return answer

max_value = maximum(test_values)
# print(max_value)