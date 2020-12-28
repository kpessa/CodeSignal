"""
You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

"""

#%%

a = [[3, 3, 4, 2],
      [4, 4],
      [4, 0, 3, 3],
      [2, 3],
      [3, 3, 3]]

def meanGroups(a):
  from statistics import mean
  
  my_dict = {}
  for i in range(len(a)):
    key = str(mean(a[i]))
    if key in my_dict.keys():
      my_dict[key].append(i)
    else:
      my_dict[key] = [i]

  result = []

  for el in my_dict.values():
    result.append(el)
  
  return result
  
print(meanGroups(a))

#%%     