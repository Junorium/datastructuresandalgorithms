def merge_sort(list):
  """
  Sorts list in ascending order
  - Recursively divide list into sublist containing a single node
  - Merge repeatedly to produce sublist until only one sublist
  - Returns sorted list
  """

  # if cannot be divided, automatically sorted; return
  if len(list) == 1:
    return list

  left_half, right_half == #split list
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right) # define merge function 
