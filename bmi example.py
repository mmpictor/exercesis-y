#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:21:48 2018

@author: MASTER
"""

name = 'mp'
height_m = 2
weight_kg = 110

bmi = weight_kg / (height ** 2)
print ('bmi: ', bmi)
if bmi < 25:
    print(name + 'is not overweight')
else:
    print(name + 'is overweight')