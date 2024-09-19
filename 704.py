from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left_pointer = 0
    right_poiner = len(nums) - 1
    while left_pointer <= right_poiner:
      mid = (left_pointer + right_poiner) // 2
      
      if nums[mid] < target:
        left_pointer = mid + 1
      elif nums[mid] > target:
        right_poiner = mid - 1
      else:
        return mid
    return -1

solution = Solution()
result = solution.search([-1,0,3,5,9,12], 9)
print(result)