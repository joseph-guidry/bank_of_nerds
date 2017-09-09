#! /usr/bin/env python3


"""
Module: bank.py
Auther: Joseph Guidry
Date  : 07/09/2017

Description:  THis module contains the functions and class to operate the bank object.

================== =================================================
    FUNCTION                            DESCRIPTION
================== =================================================
1.
2.
3.
4.

Examples: 

"""
import os
from customer import BankCustomer
from accounts import *
from utility import AgeRequirementException

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
        print("in list_accounts")
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
        print("in add_accounts")
        fmt = "{} ) {}"
        account_types = {"1":Saving, "2":Checking,
                         "3":Retirement_401k , "4":Money_Market}
        for x in range(1, 5):
            print(fmt.format(x, str(account_types[str(x)].__name__)))
        selection = input("> ")
        print(selection)
        account = account_types[selection]()
        print(type(account))
        customer.accounts[account.name] = account
        print(customer.accounts)

    def deposit_funds(self, customer):
        """ Add funds to a customers account """
        try:
            print("deposit funds")
            if len(customer.accounts) == 0:
                print("[ No Accounts ]")
                print("Consider creating a new account from the menu option")
                
            else:
                options = self.list_accounts(customer)
                print(options)
                selection = input("> ")
                account_name = options[selection]
                print(type(account_name))
                # Convert the amount into  a integer value!!!!
                amount = input("Deposit Amount: ")
                account = customer.accounts[account_name]
                account.make_deposit(float(amount) * 100)
                print(account.balance)
        except ValueError as ex:
            print("Error: ", ex)
        
    def withdraw_funds(self, customer):
        """ Remove funds from a customers account """
        try:
            print("withdraw funds")
            if len(customer.accounts) == 0:
                print("[ No Accounts ]")
                print("Consider creating a new account from the menu option")
            else:
                options = self.list_accounts(customer)
                print(options)
                selection = input("> ")
                account_name = options[selection]
                print(type(account_name))
                amount = input("Withdraw Amount: ")
                account = customer.accounts[account_name]
                print(float(amount) * 100)
                print(customer.age)
                if isinstance(account, Retirement_401k) and self._check_age_requirement(customer.age):
                    raise AgeRequirementException
                account.make_withdraw(float(amount) * 100)
                print(account.balance)
        except ValueError as ex:
            print("Error: ", ex)
        except NonSufficentFundsException:
            print("Executing Overdraft Protection...")

    def welcome(self):  # Move to I/O utility functions
        welcome_msg = "Welcome to Bank of Nerds"
        while True:
            try:
                print(self.members)
                option = input("1 )\tSign in\n2 )\tExit\n> ")
                if option == "1":
                    print(option)
                    current_customer = self._get_customer()
                    print("after getting customer")
                    self.option_menu(current_customer)
                    print("after option menu")
                elif option == "2":
                    exit()
                else:
                    print(self.customers)
                    print("Invalid Option")
            except ValueError:
                print("Input for age not a integer")
            except Exception as ex:
                print(ex)
                pass

    def _get_customer(self):  # Move to I/O utility functions
        first_name, last_name, age = self._get_info()
        current_customer = BankCustomer(first_name, last_name, int(age))
        print(current_customer)
        nerd = next( (x for x in self.members if x == current_customer), None)
        print(nerd)
        if nerd != None:
            input("Already in there")
            return nerd
        else:
            join = input("Would you like to become a member at our bank? ") or "y"
            if join in Bank.yes:
                print("add new account")
                self.add_member(current_customer)
                return current_customer
            else:
                print("Sorry but we can't help unless you open an account")
                exit()
        

    def _get_info(self):  # Move to I/O utility functions
        try:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = input("Age: ")
            return first_name, last_name, age

        except KeyboardInterrupt:
            print("Dont Do that")
            pass
        
    def option_menu(self, current_user):  # Move to I/O to utility functions
        """ The menu for member customer options """
       
        print("inside option menu " + str(current_user))

        options = {"1":self.deposit_funds, "2":self.withdraw_funds, 
                   "3":self.list_accounts, "4":self.add_account, 
                   "5": self.signed_in }

        x = True
        while self.signed_in(x) :
            self.print_menu(current_user.first_name)
            # print(current_user)
            # print(current_user.accounts)
            selection = input("> ")
            if selection == "5":
                x = options[selection](False)
            else:
                try:
                    print(selection)
                    options[selection](current_user)
                    input("Press any key to continue...")
                except AgeRequirementException:
                    print("Customer does not meet minimum age requirement")
                    print("Must be 67 years old to withdraw from 401k account")
                    input("Press any key to continue...")
                except KeyError as ex:
                    print("Please enter a valid option number", ex)


    def print_menu(self, first_name):   # Move to bank utility functions
        """ The menu output """
        os.system("clear" if os.name == "posix" else "cls")
        print("Welcome {},\nWhat can we help you with today? ".format(first_name))
        print(" 1) Deposit Funds")
        print(" 2) Withdraw Funds")
        print(" 3) List Accounts ")
        print(" 4) Create new account")
        print(" 5) Sign out\n")

    def signed_in(self, option):
        """ change value to logout of the customers menu """
        return option

    def _check_age_requirement(self, customer_age):
        return customer_age < 67  # 67 is the minimum age to withdraw from 401k






