
def hello(*names):
    # i = 0
    for i in range(10, 20, 2):
        print(i)

    print("Hello")
    for name in names:
        print(name)


hello("Drongo", "College", "Technology", "Innovations")