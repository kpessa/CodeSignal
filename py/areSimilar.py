"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

"""
#%%

a = [1, 1, 4] 
b = [1, 2, 3]

def areSimilar(a, b):
  from collections import Counter
  same_items = Counter(a) == Counter(b)
  number_of_differences = sum(a != b for a, b in zip(a,b)) < 3

  return same_items and number_of_differences

print(areSimilar(a, b))

#%%

a = [1, 1, 4] 
b = [1, 2, 3]

def areSimilar(a, b):
  if a == b:
    return True
  else:
    a_x, b_x = [], []

    for i, item in enumerate(a):
      if item != b[i]:
        if len(a_x) == 2:
          return False
      a_x.append(item)
      b_x.append(b[i])

    if len(a_x) < 2 or len(b_x) < 2:
      return False  
    elif a_x == [b_x[1], b_x[0]]:
      return True
    else:
      return False

print(areSimilar(a,b))

# %%
