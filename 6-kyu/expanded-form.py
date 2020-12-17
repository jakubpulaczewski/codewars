"""
Write Number in Expanded Form

The link: https://www.codewars.com/kata/5842df8ccbd22792a4000245

Problem Description:
You will be given a number and you will need to return it as a string in Expanded Form. 
  
Examples:
      expanded_form(12) # Should return '10 + 2'
      expanded_form(42) # Should return '40 + 2'
      expanded_form(70304) # Should return '70000 + 300 + 4'
"""
def expanded_form(num):
    
    numbers = [int(x) for x in str(num)]
    size = len(numbers)
    i = 0
    list_ = []
    while i < size:
        if numbers[i] != 0:
            list_.append(numbers[i] * (10 ** (size-i-1)))
        i+=1 
    
    return ' + '.join(str(x) for x in list_)
