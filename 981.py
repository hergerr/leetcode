
class Node:
  def __init__(self, value, timestamp) -> None:
    self.value = value
    self.timestamp = timestamp


class TimeMap:

  def __init__(self):
    self.store = {}

  def set(self, key: str, value: str, timestamp: int) -> None:
    node = Node(value, timestamp)
    if key in self.store:
      self.store[key].append(node)
    else:
      self.store[key] = [node]
    

  def get(self, key: str, timestamp: int) -> str:
    # binary search because the dict is sorted
    if key not in self.store:
      return ""
    else:
      return self.bin_search(self.store[key], timestamp)
  
  def bin_search(self, nodes: list, target: int):
    if nodes[0].timestamp > target:
      return ""
    
    min_node = None
    left = 0
    right = len(nodes) - 1
    while left <= right:
      mid = (left + right) // 2
      if nodes[mid].timestamp > target:
        right = mid - 1
      else:
        min_node = nodes[mid]
        left = mid + 1
    return min_node.value
  
timeMap = TimeMap()
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)
print(timeMap.get("love", 5))
print(timeMap.get("love", 10))
print(timeMap.get("love", 15))
print(timeMap.get("love", 20))
print(timeMap.get("love", 25))