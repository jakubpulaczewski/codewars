"""
[Code Golf] Length of Month

The link: https://www.codewars.com/kata/5fc4e46867a010002b4b5f70

Problem Description:
Return the length of the given month in the given year. [Your code must be shorter than 90 characters.]

Examples:
        last_day(2020,11) ---> 30
        last_day(1945,5) ----> 31
"""
from calendar import monthrange

def last_day(y, m):
    return monthrange(y, m)[1]
