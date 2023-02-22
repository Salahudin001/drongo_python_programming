def hello(fname,lname):
    print('hello', fname,lname)

hello('okumu','kelvin')

def hello(fname,lname):
    print('hello',fname,lname)

    
hello(lname='okumu',fname='kelvin')


def hello(**name):
    print("hello",name['fname'],name['lname'])

hello(fname="Drongo",lname="college")
hello(lname="google",fname="pixel")
hello(mname="google",fname="pixel")
hello(fname="kenya",mname="nairobi", lname="kisumu")
