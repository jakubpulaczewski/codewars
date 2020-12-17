"""
Get the mean of an array

The link: https://www.codewars.com/kata/563e320cee5dddcf77000158

Problem Description:
It's the academic year's end, fateful moment of your school report. The averages must be calculated. 
All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
Return the average of the given array rounded down to its nearest integer.
The array will never be empty.
  
Examples:
      get_average([2,5,13,20,16,16,10]) ---> 11
      get_average([1, 5, 87, 45, 8, 8]) ---> 25
"""


import numpy as np
import math

def get_average(marks):
    return math.floor(np.mean(marks))
