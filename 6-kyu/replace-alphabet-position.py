"""
Replace with Alphabet Position

The link: https://www.codewars.com/kata/546f922b54af40e1e90001da

Problem Description:
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
  
Examples:
      alphabet_position("The sunset sets at twelve o' clock.")
      Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

def alphabet_position(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    char_list = []
    
    for char in text.lower():
        if char in alphabet:
            char_list.append(str(alphabet.index(char) + 1))
    if not char_list:
        return ''
    else:
        return ' '.join(char_list)
