  
"""
Unique string characters.

The link: https://www.codewars.com/kata/5a262cfb8f27f217f700000b

Problem Description:
In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

Examples:
    solve("xyab","xzca") = "ybzc" 
    --The first string has 'yb' which is not in the second string. 
    --The second string has 'zc' which is not in the first string. 
"""
def solve(a,b):
    result = []
    for e in a:
        if e not in b:
            result.append(e)
    for e in b:
        if e not in a:
            result.append(e)
    return ''.join(result)
