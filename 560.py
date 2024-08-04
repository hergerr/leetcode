from typing import List

# we look, if a certain prefix already existed, and if part of an array, which makes it
# can be substracted from the currently investigated
# also - later append the prefix of currently investigated array

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      prefixes = {0: 1}
      sum = 0
      result = 0
      for num in nums:
        sum += num
        needed_prefix = sum - k
        matching_subarrays = prefixes.get(needed_prefix, 0)
        result += matching_subarrays
        
        if sum in prefixes:
          prefixes[sum] += 1
        else:
          prefixes[sum] = 1
      return result
      

x = Solution()
y = x.subarraySum([1], 0)
print(y)