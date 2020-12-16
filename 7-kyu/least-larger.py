  
"""
Least Larger.

The link: https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4

Problem Description:
Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 
if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Examples:
      least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
      least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
"""

def least_larger(a, i): 
    if a[i] == max(a):
        return -1
    else:
        target = a[i]
        new_a = sorted(a)
        for i,num in enumerate(new_a):
            if num == target:
                if new_a[i+1] > target:
                    return a.index(new_a[i+1])
