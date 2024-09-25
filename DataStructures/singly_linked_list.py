# expands into stacks, queues, graphs

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# possible methods: insert/delete beginning/node/end, search
def insert_start(self, data):
  new_Node = Node(data)
  if self.head:
    new_node.next = self.head
    self.head = new_node
  else:
    self.tail = new_node
    self.head = new_node

def search(self, data):
  current = self.head
  while current_node:
    if current_node.data == data:
      return (f"True at{current_node}")
    else:
      current_node = current_node.next
  return False

