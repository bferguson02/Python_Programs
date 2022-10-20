# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:58:17 2022

@author: BFERGU32
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--verbosity', help ='increase output verbosity', action='store_true')

args = parser.parse_args()

if args.verbosity:
    print('verbosity turned on')