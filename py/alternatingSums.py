#%%

def alternatingSums(a):
  x, y = [], []
  for index, item in enumerate(a):
    if index % 2 == 0:
      x.append(item)
    else:
      y.append(item)

  return [sum(x), sum(y)]
  
a = [50, 60, 60, 45, 70]
print(alternatingSums(a))

#%%

# %%
