"""
Two to One.

The link: https://www.codewars.com/kata/5656b6906de340bd1b0000ac

Problem Description:

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
It is important to note that only each token can be taken only once - coming from s1 or s2.
  
Examples:
      a = "xyaabbbccccdefww"
      b = "xxxxyyyyabklmopq"
      longest(a, b) -> "abcdefklmopqwxy"

      a = "abcdefghijklmnopqrstuvwxyz"
      longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def delete_duplicates(string):
    result = ""
    for character in string:
        if character not in result:
            result+=character
    return result

def longest(s1, s2):
    s3 = delete_duplicates(s1+s2)
    s3 = ''.join(sorted(s3))
    return s3
