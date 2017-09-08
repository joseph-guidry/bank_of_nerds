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
        self.customers = []


    def add_customer(self, customer):
        """ Add new customer to bank record of customers """
        
        self.customers.append(customer)

    def add_account(self, customer, account):
        """ Create new account for customer """
        pass

    def deposit_funds(self, amount, account):
        """ Add funds to a customers account """
        pass

    def withdrawl_funds(self, amount, account):
        """ Remove funds from a customers account """
        pass


    def welcome(self):
        welcome_msg = "Welcome to Bank of Nerds"
        try:
            while True:
                option = input("1 )\tSign in\n2 )\tExit\n> ")
                if option == "1":
                    print(option)
                    current_customer = self._get_customer()
                    option_menu(current_customer)
                elif option == "2":
                    exit()
                else:
                    print(self.customers)
                    print("Invalid Option")
        except:
            pass

    def _get_customer(self):
        try:
            first_name, last_name, age = self._get_info()
            current_customer = customer.Customer(first_name, last_name, int(age))
            print(current_customer)
            if current_customer not in self.customers:
                join = input("Would you like to become a member at our bank? ")
                if join in Bank.yes:
                    print("add new account")
                    self.add_customer(current_customer)
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

    def _get_info(self):
        try:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = input("Age: ")
            
            return first_name, last_name, age

        except KeyboardInterrupt:
            print("Dont Do that")
            pass
        
    
