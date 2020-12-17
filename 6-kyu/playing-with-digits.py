"""
Playing with digits

The link: https://www.codewars.com/kata/5552101f47fc5178b1000050

Problem Description:
we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
  
Examples:
        dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
        dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
        dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
        dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

def dig_pow(n, p):
    numbers = [int(x) for x in str(n)]
    sum = 0
    for number in numbers:
        sum+=number**p
        p+=1
    if sum % n == 0:
        return sum/n
    else:
        return -1
