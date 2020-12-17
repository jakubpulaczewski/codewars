"""
Square Every Digit

The link: https://www.codewars.com/kata/546e2562b03326a88e000020

Problem Description:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

Examples:
      if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""
def square_digits(num):
    string = ""
    for value in list(str(num)):
        string = string + str(int(value)** 2)
    return int(string)
