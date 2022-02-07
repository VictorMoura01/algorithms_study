def quicksort(arr):
  if(len(arr) < 2):
    return arr
  else:
    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot]
    higher = [i for i in arr[1:] if i > pivot]
  return quicksort(smaller) + [pivot] + quicksort(higher)

print (quicksort([10, 5, 2, 3, 7, 19, 85]))
