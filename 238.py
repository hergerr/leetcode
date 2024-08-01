from typing import List

class Solution:
    def pre_sums(self, nums):
      length = len(nums)
      self.prefix_list = [None for _ in range(length)]
      self.suffix_list = [None for _ in range(length)]
      prefix_sum = nums[0]
      suffix_sum = nums[length - 1]
      self.prefix_list[0] = prefix_sum
      self.suffix_list[length - 1] = suffix_sum
      
      for i in range(1, length):
        prefix_sum *= nums[i]
        self.prefix_list[i] = prefix_sum
        
        suffix_sum *= nums[length - i - 1]
        self.suffix_list[length - i - 1] = suffix_sum
      
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      self.pre_sums(nums)
      length = len(nums)
      output = [None for _ in range(length)]
      for i in range(length):
        if i == 0:
          output[i] = self.suffix_list[1]
        elif i == length - 1:
          output[length - 1] = self.prefix_list[length - 2]
        else:
          output[i] = self.prefix_list[i - 1] * self.suffix_list[i + 1]
      return output
    

x = Solution()
y = x.productExceptSelf([1,2,3,4])
print(y)
