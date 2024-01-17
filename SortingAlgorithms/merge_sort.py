# list version
def merge_sort_list(list):
  """
  Sorts list in ascending order
  - Recursively divide list into sublist containing a single node
  - Merge repeatedly to produce sublist until only one sublist
  - Returns sorted list
  """

  # if cannot be divided, automatically sorted; return
  if len(list) == 1:
    return list

  left_half, right_half == #split list; use list comprehension
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  

def split(list):
  """
  Divide list given containing more than one element
  """
  if list


# linked list version
def merge_sort_linked_list(linked_list):
  """
  Same procedure as list version, using defined methods of the linked_list class
  """

  if len(

    
  return merge(left, right) # define merge function 

def merge(left, right):
