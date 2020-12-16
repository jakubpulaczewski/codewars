"""
Convert boolean values to strings 'Yes' or 'No'.

The link: https://www.codewars.com/kata/53369039d7ab3ac506000467

Problem Description: Implement the function that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
  
Examples:
    bool_to_word(True) /* returns 'Yes' */
    bool_to_word(False) /* returns 'No' */
"""

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    return 'No'
    
bool_to_word(True)
# The Expected result is 'Yes'.

