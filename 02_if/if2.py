def simpleif():
    first_input= int(input("Enter time : "))
    second_input= int(input("Enter time : "))
 
    if first_input > second_input:
        print("first input is greater")
   
    if first_input < second_input:
        print("second input is greater")

def dd():
   print("inside second function")

simpleif()      
print("hello")