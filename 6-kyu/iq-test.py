"""
IQ Test

The link: https://www.codewars.com/kata/552c028c030765286c00007d

Problem Description:
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers
finds one that is different in evenness, and return a position of this number.
  
Examples:
      iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
      iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""

def iq_test(numbers):
    odd_numbers = []
    even_numbers = []
    numbers = list(map(int, numbers.split(" ")))
    for i, x in enumerate(numbers):
        if x % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    
    if len(even_numbers) > len(odd_numbers):
        return odd_numbers[0] + 1
    else:
        return even_numbers[0] + 1
    
