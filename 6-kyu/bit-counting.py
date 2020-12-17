"""
Bit Counting

The link: https://www.codewars.com/kata/526571aae218b8ee490006f4

Problem Description:
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
  
Examples:
     The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def count_bits(n):
    return bin(n)[2:].count('1')
