def div(x,y):
    div=x/y
    return div

def rem(x,y):
    rem=x%y
    return rem

def get_input():
    num1=input(int('enter number of apples : '))
    num2=input(int('enter number of people : '))
    return get_integer_input()
    
def get_integer_input(message):
    value_as_string = input(message)

    while not value_as_string.isnumeric:
        print('Input must be an integer')
        value_as_string = input(message)

    return int(value_as_string)


def divide_apples():
   
   num1,num2=get_input()
   print('the number is',div)
   print('the number is ',rem)
divide_apples()

