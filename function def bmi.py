#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:11:24 2018

@author: MASTER
"""

name = 'mp'
height_m = 2
weight_kg = 90

name1 = 'mp1'
height_m1 = 1.8
weight_kg1 = 70

name2 = 'mp2'
height_m2 = 2.5
weight_kg2 = 160

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print('bmi is: ')
    print(bmi)
    if bmi < 25:
        return name + ' is not overweight'
    else:
        return name + ' is overweight'
    
result = bmi_calculator (name, height_m, weight_kg)
result1 = bmi_calculator (name1, height_m1, weight_kg1)
result2 = bmi_calculator (name2, height_m2, weight_kg2)

print(result)
print(result1)
print(result2)

