def loops():
    print("Displace values between  1 and 10")
    for item in range(10):
        print(item)

    print("Display the values from 1 to 5 without including 5")
    for item in range ( 1, 5):
        print(item *10)

    print("Dispalce values between  1 and 10 skipping 2")
    for item in range(1, 10, 2):
        print(item)

loops()