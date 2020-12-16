  
"""
Cat years, Dog years

The link: https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

Problem Description:
I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago. Return their respective ages now as [humanYears, catYears, dogYears].

Cat Years:
  +15 cat years for first year
  +9 cat years for second year
  +4 cat years for each year after that
  
Dog Years:
  +15 dog years for first year
  +9 dog years for second year
  +5 dog years for each year after that

Examples:
        human_years_cat_years_dog_years(1) -----> [1,15,15]
        human_years_cat_years_dog_years(2) ------> [2,24,24])
        human_years_cat_years_dog_years(10) ------> [10,56,64])
"""

def human_years_cat_years_dog_years(human_years):
    dog_years_list = [15,9,5]
    cat_years_list = [15,9,4]
    cat,dog = 0,0
    for i in range (human_years):
        if(i < 3):
            cat = cat + cat_years_list[i] 
            dog = dog + dog_years_list[i] 
        else:
            cat = cat + cat_years_list[2] 
            dog = dog + dog_years_list[2] 
            
    return [human_years,cat,dog]
