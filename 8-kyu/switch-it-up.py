"""
Switch it Up!

The link: https://www.codewars.com/kata/5808dcb8f0ed42ae34000031

Problem Description:
When provided with a number between 0-9, return it in words.

Examples:
    Input :: 1

    Output :: "One".
"""

def switch_it_up(number):
    list = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    return list[number]
