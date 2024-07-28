from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        last_number = None
        for i in range(length):
          if nums[i] == '_':
             continue
          
          if nums[i] != last_number:
             last_number = nums[i]
             count += 1
             nums[count - 1] = last_number
          elif nums[i] == last_number:
             nums[i] = '_'

        return count
    

    
x = Solution()
y = x.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(y)