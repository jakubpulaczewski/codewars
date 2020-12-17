"""
The maximum and minimum difference -- Challenge version

The link: https://www.codewars.com/kata/583c592928a0c0449d000099

Problem Description:
Given two array of integers(arr1,arr2). Your task is going to find a pair of numbers(an element in arr1, and another element in arr2), 
their difference is as big as possible(absolute value); Again, you should to find a pair of numbers, their difference is as small as possible.
Return the maximum and minimum difference values by an array: [ max difference, min difference ]
  
Examples:
         Given arr1 = [3,10,5], arr2 = [20,7,15,8]
         should return [17,2] because 20 - 3 = 17, 10 - 8 = 2
"""

def max_and_min(seq1, seq2): 
    seq1.sort()
    seq2.sort()
    a = 0
    b = 0
    result = 9999999
    max_1 = abs(max(seq2) - min(seq1))
    max_2 = abs(max(seq1) - min(seq2))

    while( a < len(seq1) and b < len(seq2)):
        if abs(seq1[a] - seq2[b]) < result:
            result = abs(seq1[a] - seq2[b])
        if seq1[a] < seq2[b]:
            a = a + 1
        else:
            b = b + 1
            
    if max_1 > max_2:
        return (max_1, result)
    else:
        return (max_2, result)
