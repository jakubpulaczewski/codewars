  
"""
Who likes it?

The link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362

Problem Description:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
It must return the display text as shown in the examples:
  
Examples:
    likes([]) # must be "no one likes this"
    likes(["Peter"]) # must be "Peter likes this"
    likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
    likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
    likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""

def likes(names):
    size = len(names)
    if size == 0:
        return 'no one likes this'
    elif size == 1:
        return names[0] + ' likes this'
    elif size == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif size == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(size-2) + ' others like this'
