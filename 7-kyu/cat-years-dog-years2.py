  """
Cat Years, Dog Years (Version 2)

The link: https://www.codewars.com/kata/5a6d3bd238f80014a2000187

Problem Description:
I have a cat and a dog which I got as kitten / puppy. I forget when that was, but I do know their current ages as catYears and dogYears.
Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

Cat Years:
  +15 cat years for first year
  +9 cat years for second year
  +4 cat years for each year after that

Dog Years:
  +15 dog years for first year
  +9 dog years for second year
  +5 dog years for each year after that


Examples:
        owned_cat_and_dog(15,15) ---> [1,1]
        owned_cat_and_dog(24,24) ---> [2,2]
        owned_cat_and_dog(56,64) ---> [10,10]
"""

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years == 0 and dog_years == 0:
        return [0,0]
    dog_list = [15,9,5]
    cat_list = [15,9,4]
    cat = 0
    dog = 0
    while cat_years > 0 or dog_years > 0:
        if cat_years > 0:
            if cat <=2:
                cat_years = cat_years - cat_list[cat]
            else:
                cat_years = cat_years - cat_list[2]
            if cat_years >= 0:
                cat=cat+1

        if dog_years > 0:
            if dog <= 2:
                dog_years = dog_years - dog_list[dog]
            else:
                dog_years = dog_years - dog_list[2]
            if dog_years >= 0:
                dog=dog+1
                
    return [cat,dog] 
