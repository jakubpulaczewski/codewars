"""
Find the first non-consecutive number.

The link: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

Problem Description:
Your task is to find the first element of an array that is not consecutive. By not consecutive we mean not exactly 1 larger than the previous element of the array.
E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.
If the whole array is consecutive then return null.

Examples:
      first_non_consecutive([1,2,3,4,6,7,8]) -----> 6
      first_non_consecutive([4,5,6,7,8,9,11]) -----> 11
"""

def first_non_consecutive(arr):
    
    for element in range(len(arr)-1):
        next = arr[element+1]
        curr = arr[element]
        if curr + 1 != next:
            return next
    return None
