class Node:
  def __init__(self, key, val) -> None:
    self.key = key
    self.val = val
    self.prev = None
    self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
      self.cache = {}
      self.cap = capacity
      # right prev POINTS to most recently used
      self.right = Node(-1,-1)
      # left next POINTS to least recently used
      self.left = Node(-2,-2)
      self.right.prev = self.left
      self.left.nxt = self.right
      
    def remove(self, node: Node):
      # removes a node
      prev, nxt = node.prev, node.nxt
      prev.nxt = nxt
      nxt.prev = prev
    
    def insert(self, node: Node):
      # inserts a node, so that right pointer points to it (most recently used)
      node.nxt = self.right
      node.prev = self.right.prev
      self.right.prev.nxt = node
      self.right.prev = node

    def get(self, key: int) -> int:
      if key in self.cache:
        node = self.cache[key]
        # node is now most recently used
        self.remove(node)
        self.insert(node)
        return self.cache[key].val
      return -1

    def put(self, key: int, value: int) -> None:
      if key in self.cache:
        self.remove(self.cache[key])
      self.cache[key] = Node(key, value)
      self.insert(self.cache[key])
      if len(self.cache) > self.cap:
          least_used = self.left.nxt
          del self.cache[least_used.key]
          self.remove(least_used)


lRUCache = LRUCache(2);
print(lRUCache.put(1, 1)) # cache is {1=1}
print(lRUCache.put(2, 2)) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
print(lRUCache.put(3, 3)) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
print(lRUCache.put(4, 4)) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4