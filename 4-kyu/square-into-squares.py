"""
Square into Squares. Protect trees!

The link: https://www.codewars.com/kata/54eb33e5bc1a25440d000891

Problem Description:
Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².
If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:

Examples
  
Examples:
    decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], 
    since 9 is smaller than 10.
    
    For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
"""
def decompose(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        goal = goal + current**2
        for i in range(current -1, 0, -1):
            if(i**2 <= goal):
                goal = goal - i**2
                result.append(i)
                if goal == 0:
                    result.sort()
                    return result
    return None
