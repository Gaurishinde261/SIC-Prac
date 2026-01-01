
accounts = {}   # acc_no : [pin, balance]

def create_account(acc_no, pin):
    accounts[acc_no] = [pin, 0]
    print("Account created successfully.")

def check_pin(acc_no, pin):
    return accounts[acc_no][0] == pin

def deposit(acc_no, amount):
    accounts[acc_no][1] += amount
    print("Amount deposited successfully.")

def withdraw(acc_no, amount):
    if amount <= accounts[acc_no][1]:
        accounts[acc_no][1] -= amount
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")

def check_balance(acc_no):
    print("Current Balance:", accounts[acc_no][1])
