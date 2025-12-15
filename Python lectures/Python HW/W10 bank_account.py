class bank_account: 

    def __init__(self, account_owner,balance=0):
        self.account_owner = account_owner
        self.balance = balance
   
    def deposit(self, amount):
       if amount > 0:
          self.balance += amount 
          print(f"deposited $ {amount}. new_balance: $ {self.balance}")
       else: 
          print("Deposit amount must be positive!")
      
    def get_balance(self):
          return f"Current Balance: ${self.balance}"
    
    def withdrawal(self, amount):
       if amount > 0:
          if self.balance >= amount:
             self.balance -= amount
             print(f"withdrawal ${amount}. new_balance: $ {self.balance}")
          else: 
             print("Not enough funds :(")
                   
    def display_account_details(self):
        print(f"Account Owner: {self.account_owner}")
        print(f"Balance: ${self.balance}")
    #def new_balance(self):
        
    
    #def display_info(self):
        #print(f"{self.account_owner} {self.balance} {self.deposit} {self.withdrawal}")

     
my_account = bank_account("Batman", 10000)

my_account.display_account_details()
print("-" * 20)
#my_account.deposit(2000)
#my_account.withdrawal(5000)
#my_account.display_info()
#print("-" * 20) 

#p1 = bank_account ("Batman",10000,2000,5000)
#p2 = bank_account ("Spiderman",20000, 3000,4000)  
#p3 = bank_account ("Catwoman", 50000, 5000, 20000) 

#p1.display_info()
#p2.display_info()
#p3.display_info()
                                             
