# Assumes list is sorted
def recursive_binary_search(list, target):
  """
  Returns a boolean value on whether the target (numeric) is within the list
  """

  if len(list) == 0:
    return False
  else:
    midpoint = len(list)//2
  
  if list[midpoint] == target:
    return True
  else:
    if list[midpoint] < target:
      return recursive_binary_search(list[midpoint+1:], target)
    else:
      return recursive_binary_search(list[:midpoint], target)

try:
  if __main__ == "__name__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 8

    print(recursive_binary_search(numbers, target))
except:
  return -1
