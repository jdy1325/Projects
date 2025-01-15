# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:44:23 2024

@author: JackD
"""
import re

def validNumber(phoneNumber):
    return type(phoneNumber) == str and re.match(r'^\d{3}-\d{3}-\d{4}$', phoneNumber)

def main():
    number = input("Please enter a phone number: ").strip()
    if validNumber(number):
        print("\"{}\" is a valid phone number".format(number))
    else:
        print("that is not a valid phone number")

main()