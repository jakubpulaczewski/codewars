  
"""
Last digit of a large number

The link: https://www.codewars.com/kata/5511b2f550906349a70004e1

Problem Description:
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b.

Note that a and b may be very large!

Examples:
              last_digit(4, 1)                # returns 4
              last_digit(4, 2)                # returns 6
              last_digit(9, 7)                # returns 9
              last_digit(10, 10 ** 10)        # returns 0
              last_digit(2 ** 200, 2 ** 300)  # returns 6
"""
def last_digit(n1,n2):
    
    # if the remainder is 0 then return 0
    if n1 % 10 == 0:
        return 0
    # if the power is equal to 0 then return 0
    if n2 == 0:
        return 1
    # if the power is equal to 1 then find the remainder of 10.
    if n2 == 1:
        return n1 % 10

    # dictionary is used for hashing the values.
    dictionary = {} 
    
    # the k is the starting power.
    k = 1
    
    # computes the modular arithmetic
    next =(n1 ** k) % 10
    dictionary[k] = next
    
    # initiates two variables
    # sum is used to multiply different values from different powers 
    sum = 1
    # sum_k_values is used to 
    sum_k_values = n2

    while True:
        if k*2 <= n2:
            k =k*2
        else:
            for k_coefficient, value in reversed(list(dictionary.items())):
                if sum_k_values == 0:
                    return sum % 10
                if sum_k_values - k_coefficient >= 0:
                    sum = sum * dictionary.get(k_coefficient)
                    sum_k_values = sum_k_values - k_coefficient

            return sum % 10
        next = (next ** 2) % 10
        dictionary[k] = next
