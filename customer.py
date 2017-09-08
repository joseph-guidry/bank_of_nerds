#! /usr/bin/env python3


"""
Module: bank.py
Auther: Joseph Guidry
Date  : 07/09/2017

Description:  THis module contains the functions and class to operate the customer object.

================== =================================================
    FUNCTION                            DESCRIPTION
================== =================================================
1.
2.
3.
4.

Examples: 

"""


class Customer():
    """ 
    This is the customer interface
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
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
