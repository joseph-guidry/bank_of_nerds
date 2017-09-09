#!/usr/bin/env python3


"""
Module: accounts.py
Auther: Joseph Guidry
Date  : 09-06-2017

Description: The API for an account.

================== =================================================
    FUNCTION                            DESCRIPTION
================== =================================================
1. 
2.
3.
4.

Examples: 

"""

import abc
from utility import NonSufficentFundsException

class Account(metaclass=abc.ABCMeta):
    """ The base bank account class """

    @abc.abstractmethod
    def _update_value(self, change):
        """ A change in value to an account """

class Checking(Account):
    """ this acts as the standard checking account """

    account_id = 10000

    def __init__(self, start=0):
        """ Creating a checking account """
        self.name = "Checking_Acct  #"
        self.balance = start

    def __str__(self):
        return self.name + " : " + str(self.balance)

    @property
    def name(self):
        """ The value of the checking account """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name + str(self.account_id)
        Checking.account_id +=  1

    @property
    def balance(self):
        """ The value of the checking account """
        return self._balance

    @balance.setter
    def balance(self, start):
        self._balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change

    def make_deposit(self, amount):
        """ Add value to a checking account """
        self._balance = self._update_value(self._balance, amount)

    def make_withdraw(self, amount):
        """ Take portion of checking account """
        if self.balance >= amount:
            self._balance = self._update_value(self._balance, (amount * -1))
        else:
            pass
            # raise NonSufficentFundsException


class Saving(Account):
    """ this acts as a savings account """

    account_id = 12000
    
    def __init__(self, start=0):
        """ Creating a checking account """
        self.name = "Saving_Acct #"
        self.balance = start

    def __str__(self):
        return self.name + " : " + str(self.balance)

    @property
    def name(self):
        """ The value of the checking account """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name + str(self.account_id)
        Saving.account_id +=  1

    @property
    def balance(self):
        """ The value of the checking account """
        return self._balance

    @balance.setter
    def balance(self, start):
        self._balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change

    def make_deposit(self, amount):
        """ Add value to a checking account """
        self._balance = self._update_value(self._balance, amount)

    def make_withdraw(self, amount):
        """ Take portion of checking account """
        if self._balance >= amount:
            self._balance = self._update_value(self._balance, (amount * -1))
        # raise InsufficentFundsException


class Retirement_401k(Account):
    """ The 401K account for retirement savings """

    account_id = 14000

    def __init__(self, start=0):
        """ create iniital account with a zero balance """
        self.name = "401k Acct #"
        self.balance = start

    def __str__(self):
        return self.name + " : " + str(self.balance)

    @property
    def name(self):
        """ The value of the checking account """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name + str(self.account_id)
        Saving.account_id +=  1

    @property
    def balance(self):
        """ The value of the checking account """
        return self._balance

    @balance.setter
    def balance(self, start):
        self._balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change

    def make_deposit(self, amount):
        """ Add value to a checking account """
        self._balance = self._update_value(self._balance, amount)

    def make_withdraw(self, amount):
        """ Take portion of checking account """
        if self._balance >= amount:
            self._balance = self._update_value(self._balance, (amount * -1))
        # raise InsufficentFundsException

class Money_Market(Account):
    """ The Money Market account for investment funds """
    account_id = 16000

    def __init__(self, start=0):
        """ create iniital account with a zero balance """
        self.name = "Money_Market_Acct #"
        self.balance = start

    def __str__(self):
        return self.name + " : " + str(self.balance)

    @property
    def name(self):
        """ The value of the checking account """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name + str(self.account_id)
        Saving.account_id +=  1

    @property
    def balance(self):
        """ The value of the checking account """
        return self._balance

    @balance.setter
    def balance(self, start):
        self._balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change

    def make_deposit(self, amount):
        """ Add value to a checking account """
        self._balance = self._update_value(self._balance, amount)

    def make_withdraw(self, amount):
        """ Take portion of checking account """
        if self._balance > amount:
            self._balance = self._update_value(self._balance, (amount * -1))
        # raise InsufficentFundsException


    
