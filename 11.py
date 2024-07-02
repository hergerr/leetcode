from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer <= right_pointer:
            area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(area, max_area)
            if height[left_pointer] >= height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
        return max_area

    

x = Solution()
y = x.maxArea([1,8,6,2,5,4,8,3,7])
print(y)