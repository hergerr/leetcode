from typing import List

class Solution:
  
  def prefix_sums(self, nums):
    left_sum = right_sum = 0
    length = len(nums)
    self.prefix_left = [None for i in range(length)]
    self.prefix_right = [None for i in range(length)]
    for i in range(length):
      left_sum += nums[i]
      self.prefix_left[i] = left_sum
      
      right_sum += nums[length - i - 1]
      self.prefix_right[length - i - 1] = right_sum
  
  def pivotIndex(self, nums: List[int]) -> int:
    self.prefix_sums(nums)
    for i in range(len(nums)):
      if self.prefix_left[i] == self.prefix_right[i]:
        return i
    return -1
    

x = Solution()
y = x.pivotIndex([1,7,3,6,5,6])
print(y)