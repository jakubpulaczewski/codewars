  
"""
Sum of array singles.

The link: https://www.codewars.com/kata/59f11118a5e129e591000134

Problem Description:
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.

Examples:
repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
"""

def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])
