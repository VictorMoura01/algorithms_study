def binary_search(list, item):
  lowest_index = 0
  highest_index = len(list) - 1
  
  while(lowest_index <= highest_index):
    midle_index = (lowest_index + highest_index) // 2
    guess = list[midle_index]
    if(guess == item):
      return midle_index
    if(guess > item):
      highest_index = midle_index - 1
    else:
      lowest_index = midle_index + 1
  return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))