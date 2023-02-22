# python code to demonstrate call by value

string="Good Evening"

def greet(string):
    string="Good Morning"
    print("inside fuction:", string)

greet(string)
print("Outside Fuction:",string)    