"""
Land perimeter

The link: https://www.codewars.com/kata/5839c48f0cf94640a20001d3

Problem Description:
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. 
Each piece of land will be marked with 'X' while the water fields are represented as 'O'. 
Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:
  
Examples:
          ['XOOXO',
           'XOOXO',
           'OOOXO',
           'XXOXO',
           'OXOOO']
           
           should return 24.
"""

def land_perimeter(arr):
    perimeter = 0
    n_col = len(arr[0])
    n_row = len(arr)
 
    for i in range(n_row):
        for j in range(n_col):
            if arr[i][j] == 'X':
                if i == 0 or arr[i-1][j]== 'O': 
                    perimeter += 1
                if i == n_row - 1 or arr[i+1][j] == 'O':
                    perimeter += 1
                if j == 0 or arr[i][j-1] == 'O':
                    perimeter += 1
                if j == n_col - 1 or arr[i][j+1] == 'O':
                    perimeter += 1

    
    return "Total land perimeter: " + str(perimeter)
