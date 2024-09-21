import math
from typing import List

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)
    min_speed = max(piles)
    
    # binary search over potential solutions
    while left <= right:
      mid = (left + right) // 2
      hours = self.count_hours(piles, mid)
      if hours <= h:
        min_speed = min(min_speed, mid)
        right = mid - 1
      if hours > h:
        left = mid + 1
    return min_speed


  # computing how long would it take to consume bananas with give speed
  def count_hours(self, piles, speed):
    hours = 0
    for pile in piles:
      hours += math.ceil(pile / speed)
    return hours
  

solution = Solution()
result = solution.minEatingSpeed([312884470], 312884469)
print(result)
