# Reference implementation, for comparison against banking_system.py
# Same requirements: Account ABC, Savings/Cheque/Investment subclasses, shared registry, console menu

from abc import ABC, abstractmethod
import random


class Account(ABC):

    _registry = {}

    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = self._generate_account_number()
        Account._registry[self.account_number] = self

    @classmethod
    def _generate_account_number(cls):
        while True:
            candidate = random.randint(10000, 99999)
            if candidate not in cls._registry:
                return candidate

    @classmethod
    def find(cls, account_number, name):
        account = cls._registry.get(account_number)
        if account is not None and account.name == name:
            return account
        return None

    def get_balance(self):
        print(f"Available balance: R{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited R{amount}. New balance: R{self.balance}")

    @abstractmethod
    def withdraw(self, amount):
        ...

    @property
    @abstractmethod
    def account_type(self):
        ...


class SavingsAccount(Account):
    interest_rate = 0.04
    account_type = "Savings"

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew R{amount}. New balance: R{self.balance}")


class ChequeAccount(Account):
    overdraft_limit = 2000
    account_type = "Cheque"

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Insufficient funds, overdraft limit exceeded.")
            return
        self.balance -= amount
        print(f"Withdrew R{amount}. New balance: R{self.balance}")


class InvestmentAccount(Account):
    interest_rate = 0.08
    withdrawal_notice_days = 30
    account_type = "Investment"

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrawal of R{amount} requested. Funds available in {self.withdrawal_notice_days} days.")


ACCOUNT_TYPES = {
    "1": SavingsAccount,
    "2": ChequeAccount,
    "3": InvestmentAccount,
}


def prompt_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def create_account():
    name = input("Choose a username: ").strip()
    while not name.isalpha():
        name = input("Letters only, please try again: ").strip()

    print("1. Savings\n2. Cheque\n3. Investment")
    choice = input("Select an account type: ").strip()
    while choice not in ACCOUNT_TYPES:
        choice = input("Please enter 1, 2 or 3: ").strip()

    initial_deposit = prompt_int("Initial deposit: R")
    account_class = ACCOUNT_TYPES[choice]
    account = account_class(name, initial_deposit)
    print(f"Account created. Your account number is {account.account_number}.")


def access_account():
    name = input("Name: ").strip()
    account_number = prompt_int("Account number: ")
    account = Account.find(account_number, name)

    if account is None:
        print("Authentication failed.")
        return

    print(f"Welcome back, {account.name} ({account.account_type} account).")
    while True:
        print("1. Balance\n2. Deposit\n3. Withdraw\n4. Log out")
        choice = input("Select an option: ").strip()

        if choice == "1":
            account.get_balance()
        elif choice == "2":
            account.deposit(prompt_int("Deposit amount: R"))
        elif choice == "3":
            account.withdraw(prompt_int("Withdrawal amount: R"))
        elif choice == "4":
            break
        else:
            print("Please choose 1-4.")


def main():
    while True:
        print("1. Log in\n2. Create account\n3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            access_account()
        elif choice == "2":
            create_account()
        elif choice == "3":
            break
        else:
            print("Please choose 1-3.")


if __name__ == "__main__":
    main()
