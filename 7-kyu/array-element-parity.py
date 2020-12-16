  
"""
Array element partiy.

The link: https://www.codewars.com/kata/5a092d9e46d843b9db000064

Problem Description:
In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive.
Your task will be to find that integer.

Examples:
      [1, -1, 2, -2, 3] => 3
      [-3, 1, 2, 3, -1, -4, -2] => -4
      [1, -1, 2, -2, 3, 3] => 3
"""

def solve(arr):
    for a in arr:
        if -a not in arr:
            return a
