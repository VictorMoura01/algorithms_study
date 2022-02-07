def count(arr):
  if(arr == []):
    return 0
  else:
    arr.pop(0)
    return 1 + count(arr)
  
print(count([1, 2, 3, 4, 5]))