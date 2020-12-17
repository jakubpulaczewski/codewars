"""
Find the unique number

The link: https://www.codewars.com/kata/585d7d5adb20cf33cb000235

Problem Description:
There is an array with some numbers. All numbers are equal except for one. Try to find it!

Examples:
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
"""

# Solution 1

def find_uniq(arr):
    n = len(arr)   #size of the array
    arr.sort()   #sorting the array 
    
    #checking for the first element
    if arr[0] != arr[1]:
        return arr[0]
    
    for i in range(1, n-1):
        if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            return arr[i]
    
    #last element
    if arr[n-2] != arr[n-1]:
        return arr[n-1]
        
 # More Robust Solution
 def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
