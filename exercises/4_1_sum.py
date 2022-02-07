def sum(arr):
  if(len(arr) == 0):
    return 0
  else:
    return arr.pop(0) + sum(arr)

print(sum([2, 4, 6]))