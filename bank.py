#! /usr/bin/env python3


"""
Module: bank.py
Auther: Joseph Guidry
Date  : 07/09/2017

Description:  This module contains the functions and class to operate
              the bank object.

==================       =================================================
    FUNCTION                           DESCRIPTION
==================       =================================================
1.  add_member           - add additional member to the banks list of members.
2.  list_accounts        - display the accounts of member, return a dictionary.
3.  add_account          - create new account, add to member list of accounts.
4.  deposit_funds        - add funds to an existing account.
5.  withdraw_funds       - remove funds from an existing account.
6.  welcome              - display a welcome prompt for user to login.
7.  option_menu          - display a list of options for user to do.
8.  user_menu            - promput used by option_menu().
9.  signed_in            - allows user to exit account, return to main menu.
10. _check_age           - ensure age is within the boundaries implemented.
11. _get_account         - private method to resolve the individual account.
12. _get_customer        - private method to resolve customer account.
13. _get_info            - private method to get user information for account.

Examples:

"""
import os
from customer import BankCustomer
from utility import AgeRequirementException
from accounts import *


class Bank():
    """
    This is the bank interface providing user with menu of options
    that can be done with the users accounts
    """
    no = ["no", "n", "No", "NO"]
    yes = ["yes", "y", "Yes", "YES"]

    def __init__(self):
        """ bank constructor """
        self.name = "Bank of Nerds"
        self.members = []

    def add_member(self, customer):
        """ Add new customer to bank record of customers """
        self.members.append(customer)

    def list_accounts(self, customer):
        """ provide a out of the customers account summary """
        numbers = [str(x + 1) for x in range(0, len(customer.accounts))]
        options = dict(zip(numbers, customer.accounts))
        fmt = "{} ) {} : ${:0.2f}"
        if len(customer.accounts) == 0:
            print("[ No Accounts ]")
            print("Consider creating a new account from the menu option")
        else:
            for number, account in enumerate(customer.accounts):
                balance = customer.accounts[account].balance
                print(fmt.format(str(number + 1), account, balance/100))
        return options

    def add_account(self, customer):
        """ Create new account for customer """
        print("Choose from the following options:")
        fmt = "{} ) {}"
        account_types = {"1": Saving, "2": Checking,
                         "3": Retirement_401k, "4": Money_Market}
        for x in range(1, 5):
            print(fmt.format(x, str(account_types[str(x)].__name__)))
        selection = input("> ")
        account = account_types[selection]()
        customer.accounts[account.name] = account
        print("Created: ", account.name)

    def deposit_funds(self, customer):
        """ Add funds to a customers account """
        try:
            if len(customer.accounts) == 0:
                print("[ No Accounts ]")
                print("Consider creating a new account from the menu option")
            else:
                account = self._get_account(customer)
                amount = input("Deposit Amount: ")
                account.make_deposit(float(amount) * 100)
        except ValueError as ex:
            print("Error: ", ex)

    def withdraw_funds(self, customer):
        """ Remove funds from a customers account """
        try:
            if len(customer.accounts) == 0:
                print("[ No Accounts ]")
                print("Consider creating a new account from the menu option")
            else:
                account = self._get_account(customer)
                amount = input("Withdraw Amount: ")
                # Check to ensure customer is 67 prior to 401k withdraw
                if isinstance(account, Retirement_401k) and \
                   self._check_age(customer.age):
                    raise AgeRequirementException

                account.make_withdraw(float(amount) * 100)
        except ValueError as ex:
            print("Error: ", ex)
        except NonSufficentFundsException:
            print("Executing Overdraft Protection...")
            # Directly removes $35 from the account
            account.balance -= 3500

    def welcome(self):  # TO DO Move to utility functions
        """ Welcome prompt to stir bank implementation """
        welcome_msg = "Welcome to Bank of Nerds"
        while True:
            try:
                option = input("1 )\tSign in\n2 )\tExit\n> ")
                if option == "1":
                    current_customer = self._get_customer()
                    self.option_menu(current_customer)
                elif option == "2":
                    exit()
                else:
                    print(self.customers)
                    print("Invalid Option")
            except ValueError:
                print("Input for age not a integer")
            except Exception as ex:
                pass

    def option_menu(self, current_user):  # TO DO Move to utility functions
        """ The menu for member customer options """

        options = {"1": self.deposit_funds, "2": self.withdraw_funds,
                   "3": self.list_accounts, "4": self.add_account,
                   "5": self.signed_in}

        x = True
        while self.signed_in(x):
            self.user_menu(current_user.first_name)
            selection = input("> ")
            if selection == "5":
                x = options[selection](False)
            else:
                try:
                    options[selection](current_user)
                    input("Press any key to continue...")
                except AgeRequirementException:
                    print("Customer does not meet minimum age requirement")
                    print("Must be 67 years old to withdraw from 401k account")
                    input("Press any key to continue...")
                except KeyError as ex:
                    print("Please enter a valid option number", ex)

    def user_menu(self, first_name):   # TO DO Move to utility functions
        """ The menu output """
        os.system("clear" if os.name == "posix" else "cls")
        print("Welcome {},".format(first_name))
        print("What can we help you with today? ")
        print(" 1) Deposit Funds")
        print(" 2) Withdraw Funds")
        print(" 3) List Accounts ")
        print(" 4) Create new account")
        print(" 5) Sign out\n")

    def signed_in(self, option):
        """ change value to logout of the customers menu """
        return option

    def _check_age(self, customer_age):
        return customer_age < 67  # 67 is the minimum age to withdraw from 401k

    def _get_account(self, customer):
        """ Return the account selected """
        options = self.list_accounts(customer)
        selection = input("Select an account:\n> ")
        account_name = options[selection]
        return customer.accounts[account_name]

    def _get_customer(self):  # TO DO Move to utility functions
        """ Return the customer object found in member list or created new """
        first_name, last_name, age = self._get_info()
        current_customer = BankCustomer(first_name, last_name, int(age))
        nerd = next((x for x in self.members if x == current_customer), None)
        if nerd is not None:
            input("Already in there")
            return nerd
        else:
            string = ("You appear to be logging in for the first time...\n"
                      "Would you like to become a member at our bank?")

            join = input(string) or "y"
            if join in Bank.yes:
                self.add_member(current_customer)
                return current_customer
            else:
                print("Sorry but we can't help unless you open an account")
                exit()

    def _get_info(self):  # TO DO Move to utility functions
        """ Receive input about the user """
        try:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = input("Age: ")
            return first_name, last_name, age

        except KeyboardInterrupt:
            print("Dont Do that")
            pass
