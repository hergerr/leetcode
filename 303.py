from typing import List

class NumArray:

  def __init__(self, nums: List[int]):
    self.prefix_list = []
    sum = 0
    for i in range(len(nums)):
      sum += nums[i]
      self.prefix_list.append(sum)

  def sumRange(self, left: int, right: int) -> int:
    if left == 0:
      return self.prefix_list[right]
    return self.prefix_list[right] - self.prefix_list[left - 1]
  
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5)) # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5)) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3