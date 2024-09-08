from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    if len(height) == 0:
      return 0
    max_right = [0] * len(height)
    max_left = [0] * len(height)
    result = 0
    
    current_max = 0
    for i in range(len(height)):
      if i == 0:
        max_left[i] = 0
      else:
        current_max = max(current_max, height[i-1])
        max_left[i] = current_max
    
    current_max = 0
    for i in range(len(height)):
      if i == 0:
        max_right[len(height) - i - 1] = 0
      else:
        current_max = max(current_max, height[len(height) - i])
        max_right[len(height) - i - 1] = current_max

    for i in range(len(height)):
      field_water = min(max_right[i], max_left[i]) - height[i]
      if field_water > 0:
        result += field_water
    return result

solution = Solution()
result = solution.trap([4,2,0,3,2,5])
print(result)