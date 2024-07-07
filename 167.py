from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        sum = numbers[left_pointer] + numbers[right_pointer]
        while sum != target:
            if sum > target:
                right_pointer -= 1
            else:
                left_pointer += 1
            sum = numbers[left_pointer] + numbers[right_pointer]

        return [left_pointer + 1, right_pointer + 1] 
    
x = Solution()
y = x.twoSum([-1, 0], -1)
print(y)
