"""
A rule of Divisibility by 13

The link: https://www.codewars.com/kata/564057bc348c7200bd0000ff

Problem Description:
"A divisibility rule is a shorthand way of determining whether a given integer is divisible by a fixed divisor without performing the division, usually by examining its digits."
When you divide the successive powers of 10 by mod 13 you get the following remainders of integers divisions: 1,10,9,12,3,4.

Because:
10^0 mod 13 = 1
10^1 mod 13 = 10
10^2 mod 13 = 9
10^3 mod 13 = 12
10^4 mod 13 = 3
10^5 mod 13 = 4

Examples:
    What is the emainder when 1234567 is divided by 13?
    7      6     5      4     3     2     1  (digits of 1234567 from the right)
    ×      ×     ×      ×     ×     ×     ×  (multiplication)
    1     10     9     12     3     4     1  (the repeating sequence)
    
    Therefore, we get = 7x1 + 6x10 + 5x9 + 4x12 + 3x3 + 2x4 + 1x1 = 178
"""

def thirt(n):
    digit_count = len(str(n))
    digits = list(map(int, str(n)))
    digits[:] = digits[::-1]

    sum = 0
    previous = n
    for i in range(digit_count):
        sum+= ((10**i) % 13) * digits[i]
    if previous == sum:
        return sum
    else:
        return thirt(sum)        
                     
