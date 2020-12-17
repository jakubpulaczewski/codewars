"""
Sort the odd

The link: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

Problem Description:
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
  
Examples:
    sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""
def sort_array(source_array):
    data = [x if x % 2 == 0 else None for x in source_array]
    odd_list = sorted([x for x in source_array if x % 2 != 0])
    i = 0
    for index,x in enumerate(data):
        if x == None:
            data[index] = odd_list[i]
            i=i+1
    return data

