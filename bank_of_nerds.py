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
from bank import *
from customer import *

def main():
    nerd_bank = Bank()
    nerd_bank.welcome()
    

    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        exit()
