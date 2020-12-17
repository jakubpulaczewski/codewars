"""
Sorting by bits

The link: https://www.codewars.com/kata/59fa8e2646d8433ee200003f

Problem Description:

In this kata you're expected to sort an array of 32-bit integers in ascending order of the number of on bits they have.

Examples:
    E.g Given the array [7, 6, 15, 8]

    7 has 3 on bits (000...0111)
    6 has 2 on bits (000...0011)
    15 has 4 on bits (000...1111)
    8 has 1 on bit (000...1000)
    
    So the array in sorted order would be [8,6,7,15].
"""

def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def sort_by_bit(arr): 
    arr.sort()
    dictionary = {}
    a =  [str(bin(element)[2:]).count('1') for element in arr]

    for index, count in enumerate(a):
        dictionary = add_values_in_dict(dictionary, count, [arr[index]])
    dic = (sorted(dictionary.items()))
    new_list = []
    for key, value in dic:
        for value2 in value:
            new_list.append(value2)
    return new_list
