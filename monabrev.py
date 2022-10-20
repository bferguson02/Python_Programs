# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:23:33 2022

@author: BFERGU32
"""

def main():
    num = int(input("What number abbreviations do you want?"))
    months = ["JAN", "FEB", 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
              'SEP', 'OCT', 'NOV', 'DEC']
    print(months[num -1])
    
main()
