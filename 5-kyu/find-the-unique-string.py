  
"""
Find the unique string

The link: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

Problem Description:
There is an array of strings. All strings contains similar letters except one. Try to find it!
  
Examples:
      find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
      find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
"""

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2) or set(lst1) >= set(lst2)

def find_uniq(a):
    a = [x for x in a if x]
    a.sort()
    n = len(a)
    if n == 1:
        return a[0]

    if sublist(a[0], a[1]) == False:
        return a[0]
    
    for i in range (1, n - 1):
    
        if sublist(a[i], a[i+1]) == False and sublist(a[i], a[i-1]) == False:
            return a[i]
    
    if sublist(a[n-2], a[n-1]) == False:
        return a[n-1]
