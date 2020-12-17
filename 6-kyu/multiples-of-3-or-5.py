"""
Multiples of 3 or 5

The link: https://www.codewars.com/kata/514b92a657cdc65150000006

Problem Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
  
Examples:
    solution(10) ---> 23
"""
def solution(number):
      return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
