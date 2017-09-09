#!/usr/bin/env python3


"""
Module: accounts.py
Auther: Joseph Guidry
Date  : 09-06-2017

Description: The API for an account.

================== =================================================
    FUNCTION                            DESCRIPTION
================== =================================================
1. make_deposit     - account method to increase the account balance.
2. make_withdraw    - account method to decrease the account balance.
3. _update_value    - abstract method required to be a subclass.


"""

import abc
from utility import NonSufficentFundsException


class Account(metaclass=abc.ABCMeta):
    """ The base bank account class """

    @abc.abstractmethod
    def _update_value(self, change):
        """ A change in value to an account """

    def __str__(self):
        return self.name + " : " + str(self.balance)

    @property
    def name(self):
        """ The value of the checking account """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name + str(self.account_id)
        Checking.account_id += 1

    @property
    def balance(self):
        """ The value of the checking account """
        return self._balance

    @balance.setter
    def balance(self, start):
        self._balance = start

    def make_deposit(self, amount):
        """ Add value to a checking account """
        self._balance = self._update_value(self._balance, amount)

    def make_withdraw(self, amount):
        """ Take portion of checking account """
        if self.balance < amount:
            raise NonSufficentFundsException
        self._balance = self._update_value(self._balance, (amount * -1))


class Checking(Account):
    """ this acts as the standard checking account """

    account_id = 10000

    def __init__(self, start=0):
        """ Creating a checking account """
        self.name = "Checking_Acct  #"
        self.balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change


class Saving(Account):
    """ this acts as a savings account """

    account_id = 12000

    def __init__(self, start=0):
        """ Creating a checking account """
        self.name = "Saving_Acct #"
        self.balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change


class Retirement_401k(Account):
    """ The 401K account for retirement savings """

    account_id = 14000

    def __init__(self, start=0):
        """ create iniital account with a zero balance """
        self.name = "401k Acct #"
        self.balance = start

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change


class Money_Market(Account):
    """ The Money Market account for investment funds """
    account_id = 16000

    def __init__(self, start=0):
        """ create iniital account with a zero balance """
        self.name = "Money_Market_Acct #"
        self.balance = start

    def __str__(self):
        return self.name + " : " + str(self.balance)

    def _update_value(self, amount, change):
        """ Update the value of the account """
        return amount + change
