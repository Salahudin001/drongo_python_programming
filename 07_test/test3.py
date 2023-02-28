
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10
    print(f"Number is {num}")

    # increment counter by 1
    count = count + 1
    print(f"Count is {count} ")
    print("\n\n")
    
print("Total digits are:", count)