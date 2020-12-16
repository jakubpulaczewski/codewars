"""
Descending Order.

The link: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

Problem Description:
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples:
    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
    split_words = (text.split(" "))
    list = []
    for element in split_words:
        list.append(element[::-1])
    return ' '.join(list)    
