  
"""
Sort Out The Men From Boys.

The link: https://www.codewars.com/kata/5af15a37de4c7f223e00012d

Problem Description:
Now that the competition gets tough it will Sort out the men from the boys . Men are the Even numbers and Boys are the odd
Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .


Examples:
        menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3}) 
        menFromBoys ({-94, -99 , -100 , -99 , -96 , -99 }) ==> return ({-100 , -96 , -94 , -99})
"""

def men_from_boys(arr):
    men = []
    boys = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            men.append(i)
        else:
            boys.append(i)
    return men + boys[::-1]
