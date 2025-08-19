from datetime import datetime

class Bank:
    
    def __init__(self, balance=7500):
        self.balance = balance
        print(f"\n\tWelcome to the Banking App.\n\tYour initial bank balance was {self.balance}\n")

    def get_balance(self):
            with open ("Bank_statement.txt", "r") as file:
                line=file.readlines()
                last_object=line[-1]
                split_word = last_object.split()
                self.balance=int((split_word[-1]))
                
                date= datetime.now()
                formatted_date=date.strftime("%d %b %Y %H:%M")
                print(f"\tas of {formatted_date}")
                print(f"\tYour current balance is {self.balance}\n")

    def deposit(self, amount):                
                self.balance += amount
                print(f"Deposit successful. Your new balance is {self.balance}")
                try:
                    with open("Bank_statement.txt", "a") as file:
                        file.write(f"Deposit\t\t:\t{amount}\t Balance: {self.balance}\n")
                except Exception as e:
                     print(f"Error writing to file: {e}")
                
    def withdrawal(self, amount):

        if amount > self.balance:
                 print("Insufficient funds for this withdrawal.")
                 print(f"Current balance is remains unchanged")
        else:
            self.balance -= amount
            print(f" Withdrawal successful. Your new balance is {self.balance}")
        try:
             with open("Bank_statement.txt", "a") as file:
                  file.write(f"\nWithdrawal\t:\t{amount}\t\tBalance: {self.balance}\n")
        except Exception as e:
             print(f"Could not add transaction to bank statement")

    def write_to_file(self):
        try:
             
            with open("Bank_statement.txt", "a") as file:
                file.write(f"Balance:{self.balance}\n")
        except Exception as e:
                print("File could not be written")

        except Exception as e:
                    print(f"Error reading from file: {e}")
    def exit_message(self):
         print("please type 'exit' to exit the banking service")

#read balance before creating bank object

#open bank account with initial balance

bank_account = Bank()
bank_account.get_balance()

while True:

    prompt= input("Do you want to make a withdrawal or deposit? (d/w): " ) .lower()
    
    if prompt == 'w':
        withdrawal_amount = int(input("How much would you like to withdraw?"))
        bank_account.withdrawal(withdrawal_amount)
        bank_account.exit_message()
    elif prompt =="d": 
        deposit_amount = int(input("How much would you like to deposit?"))
        deposit=bank_account.deposit(deposit_amount)
        bank_account.exit_message()
    elif prompt == 'exit':
        print("Exiting the banking service. Thank you!")
        break
    else:
        print("Invalid option selected. Please choose 'd' for deposit or 'w' for withdrawal.")
        print("Thank you for using our banking service!")
        break  

