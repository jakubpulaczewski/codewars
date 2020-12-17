  
"""
Sum of pairs

The link: https://www.codewars.com/kata/54d81488b981293527000c8f

Problem Description:
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.


  
Examples:
          sum_pairs([11, 3, 7, 5],         10)
                         ^--^      3 + 7 = 10
          == [3, 7]
          
          sum_pairs([4, 3, 2, 3, 4],         6)
                     ^-----^         4 + 2 = 6, indices: 0, 2 *
                        ^-----^      3 + 3 = 6, indices: 1, 3
                            ^-----^   2 + 4 = 6, indices: 2, 4

entire pair is earlier, and therefore is the correct answer
== [4, 2]
          
"""
def sum_pairs(ints, s):
    # create an empty Hash Map
    dict = {}
    # do for each element
    for i, e in enumerate(ints):
        # if difference is seen before, print the pair
        if s - e in dict:
            return [ints[dict.get(s-e)], ints[i]]
        # store index of current element in the dictionary
        dict[e] = i
    return None
