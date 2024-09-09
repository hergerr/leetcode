from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    j = 1 # write pointer
    i = 1 # read pointer
    count = 1
    
    while i < len(nums):
      if nums[i] == nums[i - 1]:
        count += 1
      else:
        count = 1
      
      if count <= 2:
        nums[j] = nums[i]
        j += 1
      i += 1
    return j

solution = Solution()
result = solution.removeDuplicates([0,0,0,0,1,2,2,2,3])
print(result)