"""
Array plus array

The link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151

Problem Description:
I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
  
Examples:
      array_plus_array([1, 2, 3], [4, 5, 6]) -----> 21)
"""
def array_plus_array(arr1,arr2):
    a = sum(arr1)
    b = sum(arr2)
    return a + b
