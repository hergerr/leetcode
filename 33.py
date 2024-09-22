from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    index = -1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        index = mid
        break
      # left part of sorted array
      if nums[mid] >= nums[left]:
        if nums[left] <= target <= nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      # right part of sorted array
      else:
        if nums[mid] <= target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1          
    return index
  
solution = Solution()
result = solution.search([5,1,3], 5)
print(result)