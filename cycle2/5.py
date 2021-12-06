#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:16:00 2021

@author: sjcet
"""
import numpy as np
arr = np.arange(0, 32, 2)
print("Array is:",arr)
print("elements from 2 to 8 :",arr[2:9])
x = slice(2,9)
print("elements from 2 to 8 using slice:",arr[x])
print("Last 3 elements:",arr[-3:])
b=arr[::2]
print("Alternate elements :",b)
print("Last 3 alternate elements:",b[-3:])
