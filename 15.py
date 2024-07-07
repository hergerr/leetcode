from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        input = sorted(nums)
        length = len(nums)
        result = []
        for i in range(length):
            if i > 0 and input[i] == input[i-1]:
               # prevents duplicates
               continue
            left_pointer = i + 1
            right_pointer = length - 1
            first_element = input[i]
            while left_pointer < right_pointer:
                sum = first_element + input[left_pointer] + input[right_pointer]
                if sum == 0:
                    result.append([first_element, input[left_pointer], input[right_pointer]])
                    # if sum is correct, only one pointer must be moved. Other if statement should do the job with the right
                    left_pointer += 1
                    while input[left_pointer] == input[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
                elif sum > 0:
                    right_pointer -= 1
                elif sum < 0:
                    left_pointer += 1
        return result
    
x = Solution()
y = x.threeSum([-1,0,1,2,-1,-4])
print(y)