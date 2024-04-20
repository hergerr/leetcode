from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[nums[i]] = i 
  
x = Solution()
y = x.twoSum2([3,3], 6)
print(y)