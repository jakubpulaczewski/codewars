"""
Balanced Number (Special Numbers Series #1)

The link: https://www.codewars.com/kata/5a4e3782880385ba68000018

Problem Description:
Balanced number is the number that * The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal*.
  
Examples:
    (balanced-num 7) ==> return "Balanced"
    (balanced-num 295591) ==> return "Not Balanced"
    (balanced-num 959) ==> return "Balanced"
"""

def balanced_num(number):
    data = [int(x) for x in str(number)]
    size = len(data)
    if size == 1 or size == 2:
        return "Balanced"
    else:
        middle_digit = int(((size+1)/2) - 1)
  
        #Even size
        if size % 2 == 0: 
            left_side = data[0:middle_digit]
            right_side = data[middle_digit+2: size]
            sum_left = sum(left_side)
            sum_right = sum(right_side)
          
        #Odd size
        else:
            left_side = data[0:middle_digit]
            right_side = data[middle_digit+1: size]
            sum_left = sum(left_side)
            sum_right = sum(right_side)

        if sum_left == sum_right:
            return "Balanced"
        else:
            return "Not Balanced"
