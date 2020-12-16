"""
Reversed sequence.

The link: https://www.codewars.com/kata/5a00e05cc374cb34d100000d

Problem Description:

Build a function that returns an array of integers from n to 1 where n>0.
  
Examples:
    Example : n=5 >> [5,4,3,2,1]
"""
def reverse_seq(n):
    if n == 0 or None:
        return []
    else:
        return [int(x) for x in range(n,0,-1)]
