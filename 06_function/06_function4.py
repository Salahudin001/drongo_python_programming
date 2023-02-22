# python code to demonstrate call by reference

def append_to_list(list1):
    list1.append(35)
    print("Inside Fuction: ",list)

multiples_of_5=[5,10,15,20,25,30]
append_to_list(multiples_of_5)
print("Outside fuction: ",multiples_of_5)
