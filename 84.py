from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    max_area = 0
    
    # areas computed to all bars, which cannot continue to the end of histogram
    for index, height in enumerate(heights):
      start = index
      while stack and stack[-1][1] > height:
        poped_index, poped_height = stack.pop()
        max_area = max(max_area, poped_height * (index - poped_index))
        start = poped_index
      stack.append((start, height))
      
    # areas computed to all bars, which continue to the end of histogram
    for index, height in stack:
      max_area = max(max_area, height * (len(heights) - index))
    
    return max_area


solution = Solution()
result = solution.largestRectangleArea([2,1,2])
print(result)