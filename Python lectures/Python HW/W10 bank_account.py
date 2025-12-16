class bank_account: 

    def __init__(self, account_owner,balance):
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
     
my_account = bank_account("Batman", 10000)
my_account = bank_account("Spiderman", 3000)
my_account.display_account_details()
my_account.deposit(3000)
print(my_account.get_balance())
my_account.withdrawal(5000)
print(my_account.get_balance())


#p1 = bank_account ("Batman",10000,2000,5000)
#p2 = bank_account ("Spiderman",20000, 3000,4000)  
#p3 = bank_account ("Catwoman", 50000, 5000, 20000) 


                                             
