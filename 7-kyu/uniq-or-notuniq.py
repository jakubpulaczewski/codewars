"""
Thinking & Testing: Uniq or not Uniq

The link: https://www.codewars.com/kata/56d949281b5fdc7666000004

Problem Description:
No Story
No Description
Only by Thinking and Testing
Look at result of testcase, guess the code!
  
Examples:
      testit([0],[1]) ----> [0,1]
      testit([1,2],[3,4]) ---> [1,2,3,4]
      testit([1,2],[1,2]) ----> [1,1,2,2]
"""

def testit(a, b):
    a = list(set(a))
    b = list(set(b))
    a.extend(b) 
    a.sort()
    return a
