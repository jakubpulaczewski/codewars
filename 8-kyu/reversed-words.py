"""
Reversed Words

The link: https://www.codewars.com/kata/51c8991dee245d7ddf00000e

Problem Description:
Complete the solution so that it reverses all of the words within the string passed in.

Examples:
        reverseWords("The greatest victory is that which requires no battle")
         should return "battle no requires which that is victory greatest The"
"""


#First Solution

def reverseWords(s):
    text = s.split()
    text.reverse()
    str = ""
    for word in range(len(text)):
        if word < len(text) - 1:
            str = str + text[word] + " "
        else:
            str = str + text[word]
    return str
    
# more robust solution

def reverseWords(str):
    return " ".join(str.split(" ")[::-1])
