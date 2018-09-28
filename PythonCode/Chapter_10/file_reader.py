#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Read data from file.
Just for practice!
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print line.rstrip()
