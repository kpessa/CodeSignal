"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
Example
For
picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

#%%

picture = ["abc", "ded"]

def addBorder(picture):
  picture_size = len(picture[0])
  top_and_bottom = "*"*(1 + picture_size + 1) 
  result = []
  
  result.append(top_and_bottom)
  for row in picture:
    result.append("*" + row + "*")
  result.append(top_and_bottom)
  
  return result  

print(addBorder(picture))





# %%
