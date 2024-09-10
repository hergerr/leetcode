from typing import List

class Node:
  def __init__(self, value, current_min) -> None:
    self.value = value
    self.current_min = current_min

class MinStack:

  def __init__(self):
    self.stack: List[Node] = []

  def push(self, val: int) -> None:
    current_min = val if not self.stack else self._find_min_in_stack(val)
    self.stack.append(Node(value=val, current_min=current_min))

  def pop(self) -> None:
    self.stack.pop()

  def top(self) -> int:
    return self.stack[-1].value

  def getMin(self) -> int:
    return self.stack[-1].current_min
  
  def _find_min_in_stack(self, val):
    values = [elem.value for elem in self.stack]
    values.append(val)
    return min(values)
  


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2
