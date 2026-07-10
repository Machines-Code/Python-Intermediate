# Simulate a banking system
# Give a prompt to the user asking if they wish to create a new Savings Account or access an existing one
# If the user would like to create a new account, accept their name and intial deposit, and create a 5 digit random number and make it as the account number of their new Savings Account
# If they are accessing an existing account, accept their name and account number to validate the user, and give them options to withdraw, deposit or display their available balance

# Self improvements
# The base task has no reason to include a base class, involve inheritance, or use abstract methods, since there is only one account type. But I want to put these concepts into practice
# I will therefore change the task in the following ways:
# 1. The user will be asked if they want to login, create a new account, or exit
# 2. If login, call access_account function, if create new, create_account function, if exit, then break
# 3. If the user logs in successfully, they will have access to the following menu - get_balance, withdraw, deposit, or exit. These will function in accordance with their account type
# 4. If the user creates new account, they will have access to the following menu - Savings Account, Cheque Account, or Investment Account
# 5. Upon choosing an account type, they will be asked for a username, and the program will generate an account number. These details, along with a 0 bank balance, will be added to the registry
# 6. Upon successful account creation, they will be directed back to the base menu, and from there, they can run through the program with an existing account same as step 3

from abc import ABCMeta, abstractmethod
import random


class Account(metaclass=ABCMeta):

    accounts = {}

    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = self.generate_account_number()
        Account.accounts[self.account_number] = self

    def get_balance(self):
        print(f"Available bank balance is: {self.balance}")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(
            f"Successfully deposited R{deposit_amount}. Available bank balance is: R{self.balance}")

    @abstractmethod
    def withdraw(self, withdraw_amount):
        return 0

    @classmethod
    def generate_account_number(cls):
        while True:
            account_number = random.randint(10000, 99999)
            if account_number not in Account.accounts:
                return account_number

    @abstractmethod
    def account_type(self):
        return ""


class Savings_Account(Account):
    interest_rate = 0.04

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= withdraw_amount
            print(
                f"Withdrawal of R{withdraw_amount} was successful. Available bank balance is: R{self.balance}")

    def account_type(self):
        return "Savings"


class Cheque_Account(Account):
    max_overdraft = 2000

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance + self.max_overdraft:
            print("Insufficient funds, you have exceeded your overdraft limit.")
        else:
            self.balance -= withdraw_amount
            print(
                f"Withdrawal of R{withdraw_amount} was successful. Available bank balance is: R{self.balance}")

    def account_type(self):
        return "Cheque"


class Investment_Account(Account):
    interest_rate = 0.08
    withdraw_period = 30

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            print(
                f"Withdrawal of R{withdraw_amount} was successful and will reflect in your account balance within {self.withdraw_period} days.")


def access_account():
    while True:
        try:
            user_account_name = str(
                input("Please provide your account name: "))

            user_account_number = int(
                input("Please provide your account number: "))

            account = Account.accounts.get(user_account_number)

            if account is not None and user_account_name == account.name:
                try:
                    if user_account_number in Account.accounts:
                        while True:
                            try:
                                print("""
                                        Enter 1 to check bank balance
                                        Enter 2 to make a deposit
                                        Enter 3 to make a withdrawal
                                        Enter 4 to exit
                                    """)
                                user_choice = int(input())

                                if user_choice == 1:
                                    account.get_balance()
                                elif user_choice == 2:
                                    deposit_amount = int(
                                        input("How much would you like to deposit?: "))
                                    account.deposit(deposit_amount)
                                elif user_choice == 3:
                                    withdraw_amount = int(
                                        input("How much would you like to withdraw?: "))
                                    account.withdraw(withdraw_amount)
                                elif user_choice == 4:
                                    exit()
                                elif user_choice >= 5:
                                    print(
                                        "Please select either 1, 2, 3, or 4 from the menu.")
                            except (ValueError, EOFError, KeyboardInterrupt):
                                print(
                                    "Please select either 1, 2, 3, or 4 from the menu.")
                    else:
                        print(
                            f"This account number does not exist. Please try again or create a new account.")
                except (ValueError, EOFError, KeyboardInterrupt):
                    print("Please provide a valid account number")
            else:
                print("This account does not exist.")
        except (ValueError, EOFError, KeyboardInterrupt):
            print("Please try again.")


def create_account():
    while True:
        try:
            user_name = str(input("Please select a username: "))
            if not all(char.isalpha() for char in user_name):
                print("Username should consist of letters only. Please try again.")
            else:
                while True:
                    try:
                        new_account_type = int(input("""What type of account would you like to create?
1. Savings
2. Cheque
3. Investment
"""))
                        if new_account_type == 1:
                            account = Savings_Account
                        elif new_account_type == 2:
                            account = Cheque_Account
                        elif new_account_type == 3:
                            account = Investment_Account

                        initial_deposit = int(
                            input("Please specify the amount of your initial deposit: "))
                        new_account = account(user_name, initial_deposit)
                        print(
                            f"Your new account number is: {new_account.account_number}")
                        break
                    except (ValueError, EOFError, KeyboardInterrupt):
                        print("Invalid response.")
            break
        except (ValueError, EOFError, KeyboardInterrupt):
            print("Usernames should consist of letters only. Please try again.")


def user_interaction():
    while True:
        try:
            print("""
Enter 1 to login to your account
Enter 2 to create a new account
Enter 3 to exit
            """)
            user_choice = int(input())

            if user_choice == 1:
                access_account()
            elif user_choice == 2:
                create_account()
            elif user_choice == 3:
                break
            elif user_choice >= 4:
                print("Please select either 1, 2, or 3 from the menu.")
        except TypeError:
            print("Please select either 1, 2, or 3 from the menu.")


if __name__ == "__main__":
    user_interaction()
