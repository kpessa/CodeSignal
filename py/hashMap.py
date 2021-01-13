"""
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.
"""


#%%


queryType = ["addToKey", 
 "addToKey", 
 "insert", 
 "addToValue", 
 "addToValue", 
 "get", 
 "addToKey", 
 "insert", 
 "addToKey", 
 "addToValue"]
query = [[-3], 
 [-1], 
 [0,-3], 
 [3], 
 [-1], 
 [0], 
 [-1], 
 [-4,-5], 
 [-1], 
 [-4]]

def hashMap(queryType, query):
  _dict = {}

  sum = 0
  for method, value in zip(queryType,query):
    if method == "addToValue" or method == "addToKey" or method == "get":
      value = value[0]
    if method == "insert":
      _dict[value.pop(0)]=value.pop()
    if method == "addToValue":
      for key in _dict.keys():
        _dict[key] = _dict[key] + value
    if method == "addToKey":
      max = 0
      for key in _dict.keys():
        if key > max:
          max = max
      
      for key in range(0, max):
        _dict[key + value] = _dict[key]
        _dict[key] = 0 
    if method == "get":
      sum += _dict[value]

    print(_dict)
  
  return sum
  
print(hashMap(queryType, query))
# %%
