"""
Reversed Strings.
The link: https://www.codewars.com/kata/5168bb5dfe9a00b126000018
Problem Description: Implement the function that takes reverss the string passed into it.
  
Examples:
    'world'  =>  'dlrow'
"""



def solution(string):
    return string[len(string)::-1]
