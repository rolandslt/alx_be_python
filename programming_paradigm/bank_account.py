class BankAccount: 
    def __init__(self,balance = 0):
        self.account_balance = balance   

    def deposit(self, amount):
            
        self.account_balance += amount
       
        return self.account_balance    

    def withdraw(self, amount):
        if amount <= self.account_balance :
            self.account_balance -= amount
           
            return True
        else:    
          
           return False 
    def display_balance(self):
        
        print (f"current balance ${self.account_balance}")   
  

      