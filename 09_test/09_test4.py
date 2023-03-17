def palindrome ():
    x=input('Enter the name : ')
    y=x[::-1]
    
    if (y==x):
        print('name is palindrome ')
        return True
    else:
        print('name is not palindrome ')
        return False
    
palindrome()