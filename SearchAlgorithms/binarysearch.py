# Assumes list is sorted
def binary_search(list, target):
  """
  Returns the index of the target (numeric) if found, else return -1
  """
  
  # Define the first and last positions of the list
  first = 0
  last = len(list) - 1
  while first <= last:
    midpoint = (first + last) // 2
    if list[midpoint] == target: # If found, point
      return midpoint
    elif list[midpoint] < target: # If less, redefine first as the midpoint
      first = midpoint + 1
    else: # if more, redefine last as the midpoint
      last = midpoint -1
  else:
    return -1

try:
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  target = 5

  print(binary_search(numbers, target))
except:
  return -1
