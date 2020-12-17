"""
What's a Perfect Power anyway?

The link: https://www.codewars.com/kata/54d4c8b08776e4ad92000835

Problem Description:
In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. 
More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n. Otherwise, return none.

Examples:
      isPP(4) => [2,2]
      isPP(9) => [3,2]
      isPP(5) => None
"""

import math

def floateq(a, b, tolerance=0.00000001):
    return abs(a-b) < tolerance

def has_integer_cube_root(n, i):
    floatroot = (n ** (1.0 / i))
    introot = int(round(floatroot))
    return floateq(floatroot, introot), introot

def isPP(n):
    for i in range(2,100):
        isTrue, value = has_integer_cube_root(n, i)
        if isTrue:
            if(value == 1):
                return None
            return [value, i ]
    return None
