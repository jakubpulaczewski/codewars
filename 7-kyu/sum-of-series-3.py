"""
Beginner Series #3 Sum of Numbers

The link: https://www.codewars.com/kata/55f2b110f61eb01779000053

Problem Description:

Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. 
If the two numbers are equal return a or b.

Examples:
    get_sum(1, 0) == 1   // 1 + 0 = 1
    get_sum(1, 2) == 3   // 1 + 2 = 3
    get_sum(0, 1) == 1   // 0 + 1 = 1
    get_sum(1, 1) == 1   // 1 Since both are same
    get_sum(-1, 0) == -1 // -1 + 0 = -1
    get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

def get_sum(a,b):
    if a > b:
        higher = a
        lower = b
    else:
        higher = b
        lower = a
    result = 0
    for i in range(lower,higher+1):
        result+=i
    return result
