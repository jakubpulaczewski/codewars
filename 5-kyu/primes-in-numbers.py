"""
Primes in numbers

The link: https://www.codewars.com/kata/54d512e62a5e54c96200019e


Problem Description:
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form : "(p1**n1)(p2**n2)...(pk**nk)"

Examples:
    Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):
    p = 2
    count=0
    new_dict  = {}
    while n >= p:
        if n % p == 0:
            count+=1
            new_dict[p] = count
            n = n/p
        else:
            count = 0
            p+=1
    
    string = ""
    for key, value in new_dict.items():
        if value == 1:
            string = string +  "(" + str(key) + ")"
        else:
            string = string + "(" + str(key) + "**" + str(value) + ")"
            
