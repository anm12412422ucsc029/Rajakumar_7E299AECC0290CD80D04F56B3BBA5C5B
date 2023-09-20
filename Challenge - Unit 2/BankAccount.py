class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0) :
        self.__account_number=account_number
        self.__account_holder_name=account_holder_name
        self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance+=amount
      print("deposited: ₹{}\nNew balance: ₹{}".format(amount,self.__account_balance))
    else:
       print("Invalid deposit amount.please deposit a positive amount.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance-=amount
      print("withdrew: ₹{}\nNew balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insuufficient balance.")
  def display_balance(self):
    print("Account holder name: {}\nAccount number: {}\naccount balance: ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
account=BankAccount(account_number="123456789",account_holder_name="rajakumar",initial_balance=5000.00)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()