#! /usr/bin/env python3


"""
Module: bank.py
Auther: Joseph Guidry
Date  : 07/09/2017

Description:  THis module contains the functions and class
              to operate the customer object.

Customer class is an abstract base class which is used to create 
the BankCustomer class, which is used by the bank.py module.

"""
import abc


class Customer(metaclass=abc.ABCMeta):
    """
    This is the customer interface
    """

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class BankCustomer(Customer):
    """
    This is the customer interface for the bank_of_nerd application
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.accounts = {}

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.age)

    def __eq__(self, customer):
        return self.first_name == customer.first_name and \
               self.last_name == customer.last_name and \
               self.age == customer.age
