from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_len = 0
        
        for number in numbers:
            # check if it the start of a sequence
            if number - 1 in numbers:
                continue
            else:
                sequnce_lenght = 1
                last_item = number
                while last_item + 1 in numbers:
                    sequnce_lenght += 1
                    last_item += 1
                max_len = max(max_len, sequnce_lenght)
        return max_len
    
solution = Solution()
result = solution.longestConsecutive([-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9])
print(result)