Firstlist = []
Secondlist = []
if Firstlist == Secondlist:
    print("Both are equal")
else:
    print("Both are not equal")

if Firstlist is Secondlist:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")

thirdList = Firstlist

if thirdList is Firstlist:
    print("Both are pointing to the same object")
else:
    print("Both are not pointing to the same object")
