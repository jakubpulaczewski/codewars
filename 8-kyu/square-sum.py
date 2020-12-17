"""
Square(n) Sum

The link: https://www.codewars.com/kata/515e271a311df0350d00000f

Problem Description:
Complete the square sum function so that it squares each number passed into it and then sums the results together.
  
Examples:
        [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""
def square_sum(numbers):
    return sum(x **2 for x in numbers)
