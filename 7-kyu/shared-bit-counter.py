"""
Shared Bit Counter.

The link: https://www.codewars.com/kata/58a5aeb893b79949eb0000f1

Problem Description:
Complete the method that returns true if 2 integers share at least two 1 bits, otherwise return false. For simplicity assume that all numbers are non-negative.

Examples:
         7  =  0111 in binary
        10  =  1010
        15  =  1111
        
        7 and 10 share only a single 1-bit (at index 2) --> false
        7 and 15 share 3 1-bits (at indexes 1, 2, and 3) --> true
        10 and 15 share 2 1-bits (at indexes 0 and 2) --> true
"""

import math

# This method computes the binary of each number.
def compute_binary(value):
    denary = value
    binary = ""
    while denary>0:  
        binary = str(denary%2) + binary  
        denary = denary//2
    return binary
    

def shared_bits(a, b):
    value = max(a,b)
    size = math.ceil(math.log(value,2))
    first = compute_binary(a).zfill(size)
    second = compute_binary(b).zfill(size)
    counter = 0
    for i in range(len(first)):
        if first[i:i+1] == '1' and second[i:i+1] == '1':
            counter = counter + 1
    if counter >= 2:
        return True
    return False
