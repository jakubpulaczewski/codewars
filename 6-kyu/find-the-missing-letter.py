"""
Find the missing letter

The link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2


Problem Description:
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
  
Examples:
      ["a","b","c","d","f"] -> "e"
      ["O","Q","R","S"] -> "P"
"""
def find_missing_letter(chars):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    LOWER = True
    if chars[0].isupper():
        LOWER = False
        chars = [x.lower() for x in chars]
    index = alphabet.index(chars[0])
    new_list = alphabet[index:index+len(chars)]
    
    i = 0
    while i < len(chars):
        if new_list[i] != chars[i]:
            if LOWER == False:
                return new_list[i].upper()
            return new_list[i]
        i+=1
