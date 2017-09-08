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
import customer

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
    
    def get_account(self, customer):
        """ Get the list of accounts from a member """
    def add_account(self, customer, account):
        """ Create new account for customer """
        pass

    def deposit_funds(self, amount, account):
        """ Add funds to a customers account """
        pass

    def withdrawl_funds(self, amount, account):
        """ Remove funds from a customers account """
        pass


    def welcome(self):  # Move to I/O utility functions
        welcome_msg = "Welcome to Bank of Nerds"
        try:
            while True:
                option = input("1 )\tSign in\n2 )\tExit\n> ")
                if option == "1":
                    print(option)
                    current_customer = self._get_customer()
                    self.option_menu(current_customer)
                elif option == "2":
                    exit()
                else:
                    print(self.customers)
                    print("Invalid Option")
        except:
            pass

    def _get_customer(self):  # Move to I/O utility functions
        try:
            first_name, last_name, age = self._get_info()
            current_customer = customer.Customer(first_name, last_name, int(age))
            print(current_customer)
            if current_customer not in self.members:
                join = input("Would you like to become a member at our bank? ")
                if join in Bank.yes:
                    print("add new account")
                    self.add_member(current_customer)
                    print("after getting customer")
                    return current_customer
                else:
                    print("Sorry but we can't help unless you open an account")
                    exit()
            else:
                print("Already in there")
                print(current_customer.accounts)
                return current_customer

        except ValueError:
            print("Input for age not a integer")
            return

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
        # menu_options = {"1":self.deposit_funds(), "2":self.withdraw_funds, "3":
        print("inside option menu " + str(current_user))
        while (self.print_menu(current_user.first_name)):
            print(current_user)
            print(current_user.accounts)
            option = input("> ")

    def print_menu(self, first_name):   # Move to bank utility functions
        """ The menu output """
        print("Welcome {},\nWhat can we help you with today? ".format(first_name))
        print(" 1) Deposit Funds")
        print(" 2) Withdraw Funds")
        print(" 3) List Accounts ")
        print(" 4) Create new account \n")

        return True













