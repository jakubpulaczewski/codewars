"""

Array combinations

The link: https://www.codewars.com/kata/59e66e48fc3c499ec5000103

Problem Description:
In this Kata, you will be given an array of arrays and your task will be to return the number of unique arrays that can be formed by picking exactly one element from each subarray.

Examples:
      solve([[1,2],[4],[5,6]]) = 4, because it results in only 4 possiblites. They are [1,4,5],[1,4,6],[2,4,5],[2,4,6].
"""

import itertools
from itertools import chain

def solve(arr):
    new_list =[]

    #Delete duplicates within the subarrays - O(n)
    for x in arr:
        new_list.append(list(set(x)))

    size = 1
    for i in range(len(new_list)):
        size = size * len(new_list[i])
    return size
