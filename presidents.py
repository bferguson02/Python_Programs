# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:50:31 2022

@author: BFERGU32
"""

import pandas as pd
import argparse

data = pd.read_csv('president_heights.csv')

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)

args = parser.parse_args()

a=data.iloc[args.x:args.y]
a1=a['height(cm)'].mean()
a2=round(a1,2)
print("The average height of presidents number", args.x, "to", args.y, "is",a2)

