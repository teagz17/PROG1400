#create a bank account by creating a dictionary
def create_account(owner, balance=0):
    return{"owner": owner, "balance": balance}

def deposit(account, amount):
    account['balance'] += amount
    print(f'Deposited ${amount}. New balance: ${account["balance"]}')

def withdraw(account, amount):
    if amount <= account['balance']:
        account['balance'] -= amount
        print(f'Withdrew ${amount}. New balance: ${account["balance"]}')
    else:
        print("Insufficient funds.")

def display_balance(account):
    print(f'Account owner: {account["owner"]}, Balance: ${account["balance"]}')

#example usage of functions

account1 = create_account('Tien Shinhan')
display_balance(account1)
deposit(account1, 1000)
withdraw(account1, 500)
display_balance(account1)

#object oriented approach
class BankAccount:
    #constructor (__init__ method):
    #initialize the attributes of the class
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance   
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ${amount}. New balance: ${self.balance}')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew ${amount}. New balance: ${self.balance}')
        else:
            print('Insufficient funds.')
    def display_balance(self):
        print(f'Account owner: {self.owner}, Balance: ${self.balance}')

account2 = BankAccount('Luffy')
account2.display_balance()
account2.deposit(1500)
account2.withdraw(700)
account2.display_balance()