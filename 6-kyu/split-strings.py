"""
Split Strings

The link: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Problem Description:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters
then it should replace the missing second character of the final pair with an underscore ('_').
  
Examples:
        solution('abc') # should return ['ab', 'c_']
        solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    if len(s) == 0:
        return []
    else:
        if len(s) % 2 != 0:
            s+="_"
        split_list = []
        i = 0
        while len(s) > i:
            split_list.append(str(s[i] + s[i+1]))
            i+=2
        return split_list
