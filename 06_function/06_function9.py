# # without parameters ,without return statement
def hello():
    print("Hello world!")

hello()

# with parameters,without return statement
def hello(fname):
    print("Hello"+fname)

hello("tina")

# without parameters,with the return statement
def isEven():
    x=10
    if(x%2==0):
        
        return "Even"
    else:
       
        return "Not Even"
       
    
        
    
even10=isEven()
print(even10)

#with parameters ,with return statement
def sum(a,b):
    c=a+b
    return c

total =sum(180,20)
print(total)