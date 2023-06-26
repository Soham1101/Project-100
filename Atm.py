#Creating ATM object using class
import time

class Atm(object):

#Initializing object and creating Card number, pin number and balance variables
    def __init__(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance

#Printing current balance and fake loading time to add pizzazz
    def check_balance(self):
        print("Loading account balance...")
        time.sleep(1.5)
        print("Your current balance is: ", self.balance)

#Asking user for withdraw value and subtracting it from balance
    def withdraw(self):
        withdrawValue = int(input("How much would you like to withdraw: "))
#Checking if sufficient funds are available to withdraw
        if withdrawValue > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - withdrawValue
            print("Loading account balance...")
#Another fake loading time to add pizzazz
            time.sleep(1.5)
            print("Your current balance is: ", self.balance)
        
#Prompting user for deposit value and adding to user balance
    def deposit(self):
        depositValue = int(input("How much do you want to deposit: "))
        self.balance = self.balance + depositValue
        print("Your current balance is: ", self.balance)

#Creating variable account as an instance of an object in class ATM
account = Atm(input("Enter card number: "),input("Enter PIN number: "),50000)
print("Welcome to your bank account Ms.Ashwini!")

#Creating GUI for user to select a path
def prompt():
    print("\n\n")
    print("\t\t 1. View Account Balance")
    print("\t\t 2. Withdraw Cash")
    print("\t\t 3. Deposit Cash")
    print("\t\t 4. Exit")
    print("\n\n")
    choice = int(input("Enter number to proceed > "))
    
#Paths user can take:
    if choice == 1:
        account.check_balance()
        prompt()

    elif choice == 2:
        account.withdraw()
        prompt()

    elif choice == 3:
        account.deposit()
        prompt()
    
    elif choice == 4:
        exit()

    else:
        print("Invalid input!")
        time.sleep(0.2)
        prompt()


#First time asking prompt to start the loop
prompt()