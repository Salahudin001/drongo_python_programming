class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
        
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in youraccount')
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def TransferCash(self ,AcountNumber , amountToBeSent ,password ):
         if password != self.password:
            print('Incorrect password for this account')
            return None
         
         if amountToBeSent > self.balance :
            print('insuffient balance')
            return None
         
         self.balance -=amountToBeSent
        #  print(amountToBeSent'was sent account ',Accout)
         return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
    
        return self.balance

    def show(self):
        print('Name:', self.name)
        print('Balance:', self.balance)
        print('Password:', self.password)
        print()

a1 = Account("drongo",1000 ,1234)
a1.deposit(5000, 1234)
a1. show()

a1.withdraw(2500, 1234)
a1.show()

a1.TransferCash(2153,500,1234) 
a1.show()

bal = a1.getBalance(1234)
print(bal)
