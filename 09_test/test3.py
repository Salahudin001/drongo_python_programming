# vals = {1: 12, 2: 12, 3: 13}
# print(vals[1])


#  provided input
values = [10, 20, 30, 10, 30, 10] 
# answer to this input: 3, 1
def most_least_frequent(values):
    # 1. compute the frequencies
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1
    # 2. compute the minimum and maximum
    max_freq = None
    min_freq = None
    for v in freq:
        if max_freq is None or freq[v] > max_freq:
            max_freq = freq[v]
        if min_freq is None or freq[v] < min_freq:
            min_freq = freq[v]
    return max_freq, min_freq

print(most_least_frequent(values))