  
"""
Max-min arrays

The link: https://www.codewars.com/kata/5a090c4e697598d0b9000004

Problem Description:
In this Kata, you will be given an array of unique elements, and your task is to rerrange the values so that the first max value is
followed by the first minimum, followed by second max value then second min value, etc.

Examples:
    solve([15,11,10,7,12]) = [15,7,12,10,11]
"""

import math

def solve(arr):
    arr.sort(reverse=True)
    size = len(arr)
    if size % 2 == 0: 
        #EVEN NUMBERS
        value = int(size/2)
        max_list = arr[:value]
        min_list = arr[-value:]
    else:
        #ODD NUMBERS
        max_list = arr[:math.ceil(size/2)]
        min_list = arr[-math.floor(size/2):]
        
    min_list = sorted(min_list)
    for i,num in enumerate(min_list):
        max_list.insert(int(2*i + 1),num)
    return max_list
