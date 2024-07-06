from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [num*num for num in nums]
        sorted = []
        left_pointer = 0
        right_pointer = len(squared_nums) - 1
        while left_pointer <= right_pointer:
          if squared_nums[left_pointer] > squared_nums[right_pointer]:
             sorted.insert(0, squared_nums[left_pointer])
             left_pointer += 1
          else:
             sorted.insert(0, squared_nums[right_pointer])
             right_pointer -= 1
        return sorted
    
x = Solution()
y = x.sortedSquares([-4,-1,0,3,10])
print(y)