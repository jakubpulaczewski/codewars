  
"""
Maximum Multiple.

The link: https://www.codewars.com/kata/5aba780a6a176b029800041c

Problem Description:

Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions:
(1) N is divisble by divisor
N is less than or equal to bound
N is greater than 0.
  
Examples:
      maxMultiple (2,7) ==> return (6)
"""
def max_multiple(divisor, bound):
    for i in range(bound,0, -1):
        if(i % divisor == 0):
            return i
        if(i == 1):
            return i
